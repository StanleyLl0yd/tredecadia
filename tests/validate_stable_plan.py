#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate M4 stable-promotion state and the RC2 -> stable transition contract."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def publication_allowed(plan: dict) -> bool:
    observation = plan["observation"]
    decisions = plan["localizationProfiles"]
    return (
        plan["sourceRc"]["publicationStatus"] == "published"
        and observation["status"] == "complete"
        and observation["stableDecision"] == "approved"
        and all(entry["stableDecision"] in {"accepted", "rejected"} for entry in decisions)
    )


def validate_observation(plan: dict) -> None:
    observation = plan["observation"]
    assert observation["status"] in {"awaiting-publication", "open", "complete"}
    assert observation["stableDecision"] in {"pending", "approved", "blocked"}
    assert isinstance(observation["evidence"], list)
    if observation["status"] in {"awaiting-publication", "open"}:
        assert observation["stableDecision"] == "pending"
    else:
        assert observation["stableDecision"] in {"approved", "blocked"}
        assert observation["evidence"], "completed RC2 observation requires recorded evidence"


def validate_profile_decisions(plan: dict) -> dict[str, dict]:
    policy = plan["profileDecisionPolicy"]
    assert policy == {
        "publicationRequiresNoPending": True,
        "acceptedStatus": "stable",
        "rejectedStatus": "reviewed",
    }
    decisions = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    assert set(decisions) == {"ru-Cyrl", "ja-Kana", "ko-Hang"}
    for entry in decisions.values():
        assert entry["currentStatus"] == "reviewed"
        assert entry["stableDecision"] in {"pending", "accepted", "rejected"}
        assert isinstance(entry["evidence"], list)
    return decisions


def synthetic_state_machine_checks(plan: dict) -> None:
    probe = copy.deepcopy(plan)
    probe["sourceRc"]["publicationStatus"] = "awaiting-publication"
    probe["observation"] = {"status": "awaiting-publication", "stableDecision": "pending", "record": "release/rc-observation.json", "evidence": []}
    for entry in probe["localizationProfiles"]:
        entry["stableDecision"] = "pending"
    assert publication_allowed(probe) is False

    probe["sourceRc"]["publicationStatus"] = "published"
    probe["observation"] = {"status": "complete", "stableDecision": "approved", "record": "release/rc-observation.json", "evidence": ["review-complete"]}
    for entry, decision in zip(probe["localizationProfiles"], ["accepted", "rejected", "accepted"]):
        entry["stableDecision"] = decision
    assert publication_allowed(probe) is True

    probe["localizationProfiles"][1]["stableDecision"] = "pending"
    assert publication_allowed(probe) is False
    probe["localizationProfiles"][1]["stableDecision"] = "accepted"
    probe["observation"]["stableDecision"] = "blocked"
    assert publication_allowed(probe) is False


def main() -> None:
    plan = load("release/stable-plan.json")
    baseline = load(plan["identityBaseline"])
    historical = load(plan["historicalIdentityBaseline"])
    current_release = load("release/publish.json")
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")

    assert plan["planVersion"] == 3
    assert plan["identityBaseline"] == "release/rc2-identity.json"
    assert plan["historicalIdentityBaseline"] == "release/v1-identity.json"
    assert plan["sourceRc"]["version"] == "1.0.0-rc.2"
    assert plan["sourceRc"]["tag"] == "v1.0.0-rc.2"
    assert plan["sourceRc"]["publicationStatus"] in {"awaiting-publication", "published"}
    if plan["sourceRc"]["publicationStatus"] == "awaiting-publication":
        assert plan["sourceRc"]["commit"] is None
        assert plan["sourceRc"]["archiveSha256"] is None
    else:
        assert isinstance(plan["sourceRc"]["commit"], str) and len(plan["sourceRc"]["commit"]) == 40
        assert isinstance(plan["sourceRc"]["archiveSha256"], str) and len(plan["sourceRc"]["archiveSha256"]) == 64

    assert plan["predecessorRc"] == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
        "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
        "observationRecord": "release/rc1-observation.json",
    }
    assert historical["sourceTag"] == plan["predecessorRc"]["tag"]
    assert historical["sourceCommit"] == plan["predecessorRc"]["commit"]
    assert baseline["release"]["version"] == plan["sourceRc"]["version"]
    assert baseline["release"]["tag"] == plan["sourceRc"]["tag"]

    assert plan["targetVersion"] == "1.0.0"
    assert plan["publication"]["targetTag"] == "v1.0.0"

    version = citation_version()
    assert version in {plan["sourceRc"]["version"], plan["targetVersion"]}
    assert current_release["version"] == version
    assert current_release["tag"] == f"v{version}"

    registry_by_path = {
        "registry/calendar.json": calendar,
        "registry/months.json": months,
        "registry/localizations.json": localizations,
    }
    assert {entry["path"] for entry in plan["registryPromotion"]} == set(registry_by_path)
    for entry in plan["registryPromotion"]:
        assert entry["currentStatus"] == "draft"
        assert entry["targetStatus"] == "stable"
        registry = registry_by_path[entry["path"]]
        assert registry["specVersion"] == version
        expected_status = entry["currentStatus"] if version == plan["sourceRc"]["version"] else entry["targetStatus"]
        assert registry["status"] == expected_status

    validate_observation(plan)
    decisions = validate_profile_decisions(plan)
    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == set(decisions)
    for profile_id, entry in decisions.items():
        if version == plan["sourceRc"]["version"]:
            expected_status = entry["currentStatus"]
        elif entry["stableDecision"] == "accepted":
            expected_status = plan["profileDecisionPolicy"]["acceptedStatus"]
        elif entry["stableDecision"] == "rejected":
            expected_status = plan["profileDecisionPolicy"]["rejectedStatus"]
        else:
            raise AssertionError(f"stable candidate has unresolved localization decision: {profile_id}")
        assert profiles[profile_id]["review"]["status"] == expected_status

    expected_allowed = publication_allowed(plan)
    assert plan["publication"]["allowed"] is expected_allowed

    notes = (ROOT / plan["stableReleaseNotes"]).read_text(encoding="utf-8")
    assert (ROOT / plan["archivePlan"]).is_file()
    if version == plan["sourceRc"]["version"]:
        assert current_release["prerelease"] is True
        assert current_release["notes"] == "release/notes/1.0.0-rc.2.md"
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" in notes
    else:
        assert expected_allowed is True
        assert current_release["prerelease"] is False
        assert current_release["notes"] == plan["stableReleaseNotes"]
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" not in notes

    synthetic_state_machine_checks(plan)
    print("Tredecadia RC2-aware stable-promotion plan validation: OK")


if __name__ == "__main__":
    main()
