#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate evidence packets for explicit v1 localization-profile decisions."""

from __future__ import annotations

import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]
READINESS = ROOT / "release" / "profile-readiness.json"
PLAN = ROOT / "release" / "stable-plan.json"
LOCALIZATIONS = ROOT / "registry" / "localizations.json"

REQUIRED_CHECKS = {
    "independent-review-evidence-recorded",
    "all-13-full-aliases-derived",
    "all-short6-aliases-derived",
    "all-short4-aliases-derived",
    "aliases-unique-within-profile",
    "reverse-mapping-verified",
    "material-approximations-documented",
}
PROFILE_IDS = {"ru-Cyrl", "ja-Kana", "ko-Hang"}


def expected_registry_profile_status(profile_id: str, version: str, plan: dict) -> str:
    plan_entries = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    entry = plan_entries[profile_id]
    if version == plan["sourceRc"]["version"]:
        return entry["currentStatus"]
    assert version == plan["targetVersion"], version
    decision = entry["stableDecision"]
    assert decision in {"accepted", "rejected"}, f"stable candidate has unresolved profile decision: {profile_id}"
    policy = plan["profileDecisionPolicy"]
    return policy["acceptedStatus"] if decision == "accepted" else policy["rejectedStatus"]


def main() -> None:
    readiness = json.loads(READINESS.read_text(encoding="utf-8"))
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    localizations = json.loads(LOCALIZATIONS.read_text(encoding="utf-8"))
    version = citation_version()

    assert version in {plan["sourceRc"]["version"], plan["targetVersion"]}
    assert readiness["schemaVersion"] == 1
    assert set(readiness["requiredChecks"]) == REQUIRED_CHECKS

    packets = {entry["id"]: entry for entry in readiness["profiles"]}
    plan_entries = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    registry_entries = {entry["id"]: entry for entry in localizations["profiles"]}
    assert set(packets) == set(plan_entries) == set(registry_entries) == PROFILE_IDS

    for profile_id in sorted(PROFILE_IDS):
        packet = packets[profile_id]
        plan_entry = plan_entries[profile_id]
        registry_entry = registry_entries[profile_id]

        # The readiness packet records the status at which the stable decision
        # was made. The live registry stays at that status in RC2, then moves
        # to the exact accepted/rejected target maturity in the stable commit.
        assert packet["currentStatus"] == plan_entry["currentStatus"] == "reviewed"
        expected_status = expected_registry_profile_status(profile_id, version, plan)
        assert registry_entry["review"]["status"] == expected_status, (
            f"{profile_id}: expected registry maturity {expected_status}, got {registry_entry['review']['status']}"
        )
        assert packet["decision"] == plan_entry["stableDecision"]
        assert packet["decision"] in {"pending", "accepted", "rejected"}
        assert packet["readiness"] == "eligible-for-explicit-stable-decision"
        assert set(packet["checks"]) == REQUIRED_CHECKS
        assert all(packet["checks"].values())
        assert packet["nativeSpeakerUsabilityStudyClaimed"] is False
        assert packet["knownApproximation"].strip()
        assert len(packet["evidence"]) >= 3

        for evidence in packet["evidence"]:
            path = evidence.split("#", 1)[0]
            assert (ROOT / path).is_file(), f"{profile_id}: missing evidence path {path}"

        readiness_ref = f"release/profile-readiness.json#{profile_id}"
        assert readiness_ref in plan_entry["evidence"]
        assert any(item.startswith("rationale/localization-") for item in plan_entry["evidence"])

        if packet["decision"] != "pending":
            decision_evidence = packet.get("decisionEvidence")
            assert isinstance(decision_evidence, list) and len(decision_evidence) >= 3
            assert all(isinstance(item, str) and item.strip() for item in decision_evidence)

    # Stable publication still requires an explicit accept/reject decision for
    # every profile; mere readiness must never imply automatic promotion.
    if any(packet["decision"] == "pending" for packet in packets.values()):
        assert plan["publication"]["allowed"] is False

    print("Tredecadia localization profile readiness validation: OK")


if __name__ == "__main__":
    main()
