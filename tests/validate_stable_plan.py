#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate M4 stable-promotion state and the RC -> stable transition contract."""

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
        observation["status"] == "complete"
        and observation["stableDecision"] == "approved"
        and all(entry["stableDecision"] in {"accepted", "rejected"} for entry in decisions)
    )


def validate_observation(plan: dict) -> None:
    observation = plan["observation"]
    assert observation["status"] in {"open", "complete"}
    assert observation["stableDecision"] in {"pending", "approved", "blocked"}
    assert isinstance(observation["evidence"], list)
    if observation["status"] == "open":
        assert observation["stableDecision"] == "pending"
    else:
        assert observation["stableDecision"] in {"approved", "blocked"}
        assert observation["evidence"], "completed RC observation requires recorded evidence"


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
        if entry["stableDecision"] != "pending":
            assert entry["evidence"], f"{entry['id']} resolved without decision evidence"
    return decisions


def synthetic_state_machine_checks(plan: dict) -> None:
    probe = copy.deepcopy(plan)
    probe["observation"] = {"status": "open", "stableDecision": "pending", "evidence": []}
    for entry in probe["localizationProfiles"]:
        entry["stableDecision"] = "pending"
        entry["evidence"] = []
    assert publication_allowed(probe) is False

    probe["observation"] = {"status": "complete", "stableDecision": "approved", "evidence": ["review-complete"]}
    decisions = ["accepted", "rejected", "accepted"]
    for entry, decision in zip(probe["localizationProfiles"], decisions):
        entry["stableDecision"] = decision
        entry["evidence"] = [f"decision:{entry['id']}:{decision}"]
    assert publication_allowed(probe) is True, "an explicitly rejected profile may remain reviewed without blocking v1"

    probe["localizationProfiles"][1]["stableDecision"] = "pending"
    probe["localizationProfiles"][1]["evidence"] = []
    assert publication_allowed(probe) is False

    probe["localizationProfiles"][1]["stableDecision"] = "accepted"
    probe["localizationProfiles"][1]["evidence"] = ["decision:accepted"]
    probe["observation"]["stableDecision"] = "blocked"
    assert publication_allowed(probe) is False


def main() -> None:
    plan = load("release/stable-plan.json")
    baseline = load(plan["identityBaseline"])
    current_release = load("release/publish.json")
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")

    assert plan["planVersion"] == 2
    assert plan["identityBaseline"] == "release/v1-identity.json"
    assert plan["sourceRc"] == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
        "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
    }
    assert plan["targetVersion"] == "1.0.0"
    assert plan["publication"]["targetTag"] == "v1.0.0"
    assert baseline["sourceTag"] == plan["sourceRc"]["tag"]
    assert baseline["sourceCommit"] == plan["sourceRc"]["commit"]

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

    notes_path = ROOT / plan["stableReleaseNotes"]
    archive_plan = ROOT / plan["archivePlan"]
    assert notes_path.is_file() and archive_plan.is_file()
    notes = notes_path.read_text(encoding="utf-8")

    if version == plan["sourceRc"]["version"]:
        assert current_release["prerelease"] is True
        assert current_release["notes"] == "release/notes/1.0.0-rc.1.md"
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" in notes
    else:
        assert expected_allowed is True, "stable metadata may not exist while the M4 gate is closed"
        assert current_release["prerelease"] is False
        assert current_release["notes"] == plan["stableReleaseNotes"]
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" not in notes

    synthetic_state_machine_checks(plan)
    print("Tredecadia stable-promotion plan validation: OK")


if __name__ == "__main__":
    main()
