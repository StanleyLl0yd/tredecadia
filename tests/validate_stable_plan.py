#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate M4 stable-promotion gate state without authorizing it prematurely."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(r'^version:\s*"([^"]+)"\s*$', text, re.MULTILINE)
    assert match is not None
    return match.group(1)


def main() -> None:
    plan = load("release/stable-plan.json")
    baseline = load(plan["identityBaseline"])
    current_release = load("release/publish.json")
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")

    assert plan["planVersion"] == 1
    assert plan["identityBaseline"] == "release/v1-identity.json"
    assert plan["sourceRc"] == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
        "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
    }
    assert baseline["sourceTag"] == plan["sourceRc"]["tag"]
    assert baseline["sourceCommit"] == plan["sourceRc"]["commit"]
    assert current_release["version"] == plan["sourceRc"]["version"]
    assert current_release["tag"] == plan["sourceRc"]["tag"]
    assert citation_version() in {plan["sourceRc"]["version"], plan["targetVersion"]}
    assert plan["targetVersion"] == "1.0.0"
    assert plan["publication"]["targetTag"] == "v1.0.0"

    registry_by_path = {
        "registry/calendar.json": calendar,
        "registry/months.json": months,
        "registry/localizations.json": localizations,
    }
    assert {entry["path"] for entry in plan["registryPromotion"]} == set(registry_by_path)
    for entry in plan["registryPromotion"]:
        assert entry["currentStatus"] == "draft"
        assert entry["targetStatus"] == "stable"
        if citation_version() == plan["sourceRc"]["version"]:
            assert registry_by_path[entry["path"]]["status"] == entry["currentStatus"]
        else:
            assert registry_by_path[entry["path"]]["status"] == entry["targetStatus"]

    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    decisions = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    assert set(decisions) == set(profiles) == {"ru-Cyrl", "ja-Kana", "ko-Hang"}
    for profile_id, entry in decisions.items():
        assert entry["currentStatus"] == "reviewed"
        assert entry["targetStatus"] == "stable"
        assert entry["stableDecision"] in {"pending", "accepted", "rejected"}
        if citation_version() == plan["sourceRc"]["version"]:
            assert profiles[profile_id]["review"]["status"] == entry["currentStatus"]
        elif entry["stableDecision"] == "accepted":
            assert profiles[profile_id]["review"]["status"] == entry["targetStatus"]

    observation = plan["observation"]
    assert observation["status"] in {"open", "complete"}
    assert observation["stableDecision"] in {"pending", "approved", "blocked"}
    assert isinstance(observation["evidence"], list)

    expected_allowed = (
        observation["status"] == "complete"
        and observation["stableDecision"] == "approved"
        and all(entry["stableDecision"] == "accepted" for entry in decisions.values())
    )
    assert plan["publication"]["allowed"] is expected_allowed

    notes_path = ROOT / plan["stableReleaseNotes"]
    archive_plan = ROOT / plan["archivePlan"]
    assert notes_path.is_file() and archive_plan.is_file()
    notes = notes_path.read_text(encoding="utf-8")
    if not expected_allowed:
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" in notes

    # The current repository is still the public RC; a stable release cannot be
    # authorized merely by introducing this plan.
    if citation_version() == plan["sourceRc"]["version"]:
        assert expected_allowed is False

    print("Tredecadia stable-promotion plan validation: OK")


if __name__ == "__main__":
    main()
