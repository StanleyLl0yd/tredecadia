#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the planned RC1 -> RC2 weekday compatibility transition before it is applied."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    manifest = load("release/rc2-transition.json")
    candidate = load(manifest["candidateRecord"])
    baseline = load("release/v1-identity.json")
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
    assert baseline["calendar"]["regularGrid"]["weekdays"] == source_names
    assert calendar["regularGrid"]["weekdays"] == source_names

    target = manifest["identityChange"]["target"]
    assert target == [{"id": item["id"], "name": item["name"]} for item in candidate["weekdays"]]
    assert [item["id"] for item in target] == [f"W{i}" for i in range(1, 8)]
    assert len({item["name"] for item in target}) == 7

    assert manifest["schemaTransition"] == {
        "calendar": {"from": 1, "to": 2},
        "months": {"from": 3, "to": 3},
        "localizations": {"from": 1, "to": 1},
    }
    assert calendar["schemaVersion"] == 1
    assert calendar_schema["properties"]["schemaVersion"]["const"] == 1
    assert months["schemaVersion"] == 3
    assert localizations["schemaVersion"] == 1

    assert stable_plan["sourceRc"]["version"] == "1.0.0-rc.1"
    assert stable_plan["publication"]["allowed"] is False
    assert observation["sourceRc"]["version"] == "1.0.0-rc.1"
    assert publish == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "prerelease": True,
        "notes": "release/notes/1.0.0-rc.1.md",
    }

    required = (
        manifest["requiredNormativeFiles"]
        + manifest["requiredFreezeAndReleaseFiles"]
        + manifest["requiredPublicSurfaces"]
        + [manifest["candidateRecord"]]
    )
    assert len(required) == len(set(required)), "RC2 transition manifest contains duplicate file entries"
    for path in required:
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

    assert len(manifest["publicationSequence"]) == 6
    assert "one-full-day" in manifest["publicationSequence"][4]

    print("Tredecadia planned RC2 weekday transition: OK")


if __name__ == "__main__":
    main()
