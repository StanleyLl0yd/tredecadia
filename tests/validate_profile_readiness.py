#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate evidence packets for the original v1.0 localization-profile decisions."""

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
    # At stable v1.0 and every later compatible v1 release, the already-made
    # v1.0 decision remains in force. A later minor must not demote it.
    decision = entry["stableDecision"]
    assert decision in {"accepted", "rejected"}, f"stable decision unresolved: {profile_id}"
    policy = plan["profileDecisionPolicy"]
    return policy["acceptedStatus"] if decision == "accepted" else policy["rejectedStatus"]


def main() -> None:
    readiness = json.loads(READINESS.read_text(encoding="utf-8"))
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    localizations = json.loads(LOCALIZATIONS.read_text(encoding="utf-8"))
    version = citation_version()

    assert readiness["schemaVersion"] == 1
    assert set(readiness["requiredChecks"]) == REQUIRED_CHECKS

    packets = {entry["id"]: entry for entry in readiness["profiles"]}
    plan_entries = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    registry_entries = {entry["id"]: entry for entry in localizations["profiles"]}
    assert set(packets) == set(plan_entries) == PROFILE_IDS
    assert PROFILE_IDS <= set(registry_entries)

    for profile_id in sorted(PROFILE_IDS):
        packet = packets[profile_id]
        plan_entry = plan_entries[profile_id]
        registry_entry = registry_entries[profile_id]

        # The readiness packet records the maturity at which the v1.0 stable
        # decision was made. RC2 retains it as reviewed; stable v1.0 and later
        # compatible releases retain the exact accepted/rejected outcome.
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

    # Stable publication at the time of M4 still required explicit decisions;
    # the historical plan must never claim authorization with a pending one.
    if any(packet["decision"] == "pending" for packet in packets.values()):
        assert plan["publication"]["allowed"] is False

    print("Tredecadia v1.0 localization profile readiness history: OK")


if __name__ == "__main__":
    main()
