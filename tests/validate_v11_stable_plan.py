#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the v1.1 RC -> stable promotion state machine."""

from __future__ import annotations

import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]
BASELINE = {"ru-Cyrl", "ja-Kana", "ko-Hang"}
CANDIDATES = {"ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva", "bn-Beng", "fa-Arab"}


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def publication_allowed(plan: dict, observation: dict) -> bool:
    summary = observation["summary"]
    return (
        observation["window"]["status"] == "complete"
        and summary["stableDecision"] == "approved"
        and summary["compatibilityCriticalDefectsFound"] == 0
        and summary["compatibilityCriticalDefectsOpen"] == 0
        and summary["openReports"] == 0
        and all(
            item["stableDecision"] in {"accepted", "rejected"}
            for item in plan["localizationProfiles"]
        )
    )


def main() -> None:
    plan = load("release/v1.1-stable-plan.json")
    observation = load(plan["observation"]["record"])
    publish = load("release/publish.json")
    localizations = load("registry/localizations.json")
    ledger = load("release/published-releases.json")
    version = citation_version()

    assert plan["planVersion"] == 1
    assert plan["sourceRc"] == observation["sourceRc"]
    assert plan["sourceRc"]["version"] == "1.1.0-rc.1"
    assert plan["sourceRc"]["publicationStatus"] == "published"
    assert plan["targetVersion"] == "1.1.0"
    assert plan["identityPolicy"] == "canonical-v1-unchanged"
    assert plan["stableBaseline"] == {
        "version": "1.0.0",
        "tag": "v1.0.0",
        "commit": "8c272bf6a48b1b84a4b2ca8c1db43c6ffb9f5ce3",
        "archiveSha256": "2f14cc4fb2bcac2cfcce280ddbe948d4c65cab098ce23c1d385d220709f5c392",
    }

    ledger_by_version = {item["version"]: item for item in ledger["releases"]}
    assert ledger_by_version["1.0.0"]["commit"] == plan["stableBaseline"]["commit"]
    assert ledger_by_version["1.0.0"]["archiveSha256"] == plan["stableBaseline"]["archiveSha256"]
    for key in ("version", "tag", "commit", "publishedAt", "archive", "archiveSha256"):
        assert ledger_by_version["1.1.0-rc.1"][key] == plan["sourceRc"][key]

    policy = plan["profileDecisionPolicy"]
    assert policy == {
        "publicationRequiresNoPending": True,
        "acceptedStatus": "stable",
        "rejectedStatus": "reviewed",
    }
    decisions = {item["id"]: item for item in plan["localizationProfiles"]}
    assert set(decisions) == CANDIDATES
    for item in decisions.values():
        assert item["currentStatus"] == "reviewed"
        assert item["stableDecision"] in {"pending", "accepted", "rejected"}
        assert isinstance(item["evidence"], list) and item["evidence"]

    assert plan["observation"]["status"] == observation["window"]["status"]
    assert plan["observation"]["stableDecision"] == observation["summary"]["stableDecision"]
    assert isinstance(plan["observation"]["evidence"], list)

    registries = {
        "registry/calendar.json": load("registry/calendar.json"),
        "registry/months.json": load("registry/months.json"),
        "registry/localizations.json": localizations,
    }
    assert {item["path"] for item in plan["registryPromotion"]} == set(registries)

    allowed = publication_allowed(plan, observation)
    assert plan["publication"]["targetTag"] == "v1.1.0"
    assert plan["publication"]["allowed"] is allowed

    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == BASELINE | CANDIDATES
    for profile_id in BASELINE:
        assert profiles[profile_id]["review"]["status"] == "stable"

    assert version in {plan["sourceRc"]["version"], plan["targetVersion"]}
    if version == plan["sourceRc"]["version"]:
        assert publish == {
            "version": "1.1.0-rc.1",
            "tag": "v1.1.0-rc.1",
            "prerelease": True,
            "notes": "release/notes/1.1.0-rc.1.md",
        }
        for item in plan["registryPromotion"]:
            assert registries[item["path"]]["status"] == item["currentStatus"] == "draft"
        for profile_id in CANDIDATES:
            assert profiles[profile_id]["review"]["status"] == "reviewed"
        assert allowed is False
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" in (
            ROOT / plan["stableReleaseNotes"]
        ).read_text(encoding="utf-8")
    else:
        assert allowed is True
        assert publish == {
            "version": "1.1.0",
            "tag": "v1.1.0",
            "prerelease": False,
            "notes": plan["stableReleaseNotes"],
        }
        for item in plan["registryPromotion"]:
            assert registries[item["path"]]["status"] == item["targetStatus"] == "stable"
        for profile_id, item in decisions.items():
            expected = policy["acceptedStatus"] if item["stableDecision"] == "accepted" else policy["rejectedStatus"]
            assert profiles[profile_id]["review"]["status"] == expected
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" not in (
            ROOT / plan["stableReleaseNotes"]
        ).read_text(encoding="utf-8")

    print("Tredecadia v1.1 stable-promotion plan validation: OK")


if __name__ == "__main__":
    main()
