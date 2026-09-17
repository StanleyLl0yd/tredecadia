#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the explicit RC1 -> RC2 weekday compatibility transition."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def stable_publication_allowed(plan: dict, observation: dict) -> bool:
    return (
        observation["window"]["status"] == "complete"
        and observation["summary"]["stableDecision"] == "approved"
        and observation["summary"]["compatibilityCriticalDefectsFound"] == 0
        and observation["summary"]["compatibilityCriticalDefectsOpen"] == 0
        and observation["summary"]["openReports"] == 0
        and all(
            profile["stableDecision"] in {"accepted", "rejected"}
            for profile in plan["localizationProfiles"]
        )
    )


def main() -> None:
    manifest = load("release/rc2-transition.json")
    candidate = load(manifest["candidateRecord"])
    rc1 = load("release/v1-identity.json")
    rc2 = load("release/rc2-identity.json")
    calendar = load("registry/calendar.json")
    calendar_schema = load("registry/calendar.schema.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")
    stable_plan = load("release/stable-plan.json")
    observation = load("release/rc-observation.json")
    publish = load("release/publish.json")

    assert manifest["manifestVersion"] == 1
    assert manifest["sourceRc"] == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
        "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
    }
    assert manifest["targetRc"] == {
        "version": "1.0.0-rc.2",
        "tag": "v1.0.0-rc.2",
        "prerelease": True,
    }

    source_names = manifest["identityChange"]["sourceNames"]
    assert source_names == ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    assert rc1["calendar"]["regularGrid"]["weekdays"] == source_names

    target = manifest["identityChange"]["target"]
    assert target == [{"id": item["id"], "name": item["canonical"]} for item in candidate["weekdays"]]
    current_weekdays = calendar["regularGrid"]["weekdays"]
    assert [{"id": item["id"], "name": item["canonical"]} for item in current_weekdays] == target
    assert current_weekdays == rc2["calendar"]["regularGrid"]["weekdays"]

    assert manifest["schemaTransition"] == {
        "calendar": {"from": 1, "to": 2},
        "months": {"from": 3, "to": 3},
        "localizations": {"from": 1, "to": 1},
    }
    assert rc1["schemaVersions"] == {"calendar": 1, "months": 3, "localizations": 1}
    assert calendar["schemaVersion"] == 2
    assert calendar_schema["properties"]["schemaVersion"]["const"] == 2
    assert months["schemaVersion"] == 3
    assert localizations["schemaVersion"] == 1

    assert stable_plan["sourceRc"]["version"] == "1.0.0-rc.2"
    assert stable_plan["predecessorRc"]["version"] == "1.0.0-rc.1"
    assert stable_plan["publication"]["allowed"] is stable_publication_allowed(stable_plan, observation)
    assert observation["sourceRc"]["version"] == "1.0.0-rc.2"
    assert publish == {
        "version": "1.0.0-rc.2",
        "tag": "v1.0.0-rc.2",
        "prerelease": True,
        "notes": "release/notes/1.0.0-rc.2.md",
    }

    required = (
        manifest["requiredNormativeFiles"]
        + manifest["requiredFreezeAndReleaseFiles"]
        + manifest["requiredPublicSurfaces"]
        + [manifest["candidateRecord"], "release/rc2-identity.json", "release/rc1-observation.json"]
    )
    for path in set(required):
        assert (ROOT / path).is_file(), path

    preserved = set(manifest["preservedIdentity"])
    for required_identity in (
        "13x28 regular grid",
        "all month numbers, names, syllables, Short-6 and Short-4 forms",
        "EQ and ED placement and semantics",
        "epoch and civil conversion formulas",
        "canonical date grammar",
    ):
        assert required_identity in preserved

    assert rc2["months"] == rc1["months"]
    assert rc2["dateGrammar"] == rc1["dateGrammar"]
    assert rc2["pronunciation"] == rc1["pronunciation"]
    assert rc2["localizationMaps"] == rc1["localizationMaps"]

    assert len(manifest["publicationSequence"]) == 6
    assert "one-full-day" in manifest["publicationSequence"][4]

    print("Tredecadia applied RC1 -> RC2 weekday transition: OK")


if __name__ == "__main__":
    main()
