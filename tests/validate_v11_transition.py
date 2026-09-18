#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Prove that v1.1 stable can differ from the published RC only as declared."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]
SOURCE_VERSION = "1.1.0-rc.1"
TARGET_VERSION = "1.1.0"
BASELINE_PROFILES = {"ru-Cyrl", "ja-Kana", "ko-Hang"}
NEW_PROFILES = {"ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva", "bn-Beng", "fa-Arab"}


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def without_release_metadata(data: dict) -> dict:
    result = copy.deepcopy(data)
    result.pop("specVersion", None)
    result.pop("status", None)
    return result


def main() -> None:
    manifest = load("release/v1.1-transition.json")
    identity = load(manifest["sourceIdentity"])
    plan = load(manifest["stablePlan"])
    observation = load(manifest["observation"])
    stable_decisions = load(manifest["profileDecisions"])
    ledger = load("release/published-releases.json")
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")
    publish = load("release/publish.json")
    version = citation_version()

    assert manifest["manifestVersion"] == 1
    assert manifest["sourceVersion"] == SOURCE_VERSION
    assert manifest["targetVersion"] == TARGET_VERSION
    assert manifest["compatibilityClass"] == "compatible-minor-localization-promotion"
    assert manifest["acceptedProfiles"] == [
        "ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva", "bn-Beng", "fa-Arab"
    ]
    assert manifest["rejectedProfiles"] == []
    assert set(manifest["acceptedProfiles"]) == NEW_PROFILES
    assert manifest["unchangedSchemaVersions"] == {
        "calendar": 2, "months": 3, "localizations": 1
    }

    release = identity["release"]
    assert release == {
        "version": SOURCE_VERSION,
        "tag": "v1.1.0-rc.1",
        "publicationStatus": "published",
        "commit": "8d1b5a0c05eab8875e95b9896fd1c386edfe1220",
        "publishedAt": "2026-09-18T08:01:59Z",
        "archive": "tredecadia-1.1.0-rc.1.tar.gz",
        "archiveSha256": "5b32dad3438572b67381ef5af05bf6fd915a2393fc69c8c132b7bef125ff876e",
    }
    ledger_entry = next(item for item in ledger["releases"] if item["version"] == SOURCE_VERSION)
    for key in ("version", "tag", "commit", "publishedAt", "archive", "archiveSha256"):
        assert ledger_entry[key] == release[key]

    assert identity["schemaVersions"] == manifest["unchangedSchemaVersions"]
    assert calendar["schemaVersion"] == identity["schemaVersions"]["calendar"]
    assert months["schemaVersion"] == identity["schemaVersions"]["months"]
    assert localizations["schemaVersion"] == identity["schemaVersions"]["localizations"]

    # Canonical calendar/month data are byte-structure-equivalent after
    # removing only release-version and maturity metadata.
    assert without_release_metadata(calendar) == identity["calendar"]
    assert without_release_metadata(months) == identity["months"]

    source_profiles = {item["id"]: item for item in identity["localizations"]["profiles"]}
    current_profiles = {item["id"]: item for item in localizations["profiles"]}
    decision_by_id = {item["id"]: item for item in plan["localizationProfiles"]}
    stable_record = {item["id"]: item for item in stable_decisions["decisions"]}

    assert set(source_profiles) == BASELINE_PROFILES | NEW_PROFILES
    assert set(current_profiles) == set(source_profiles)
    assert set(decision_by_id) == NEW_PROFILES
    assert set(stable_record) == NEW_PROFILES

    if version == SOURCE_VERSION:
        assert calendar["specVersion"] == months["specVersion"] == localizations["specVersion"] == SOURCE_VERSION
        assert calendar["status"] == months["status"] == localizations["status"] == "draft"
        assert current_profiles == source_profiles
        assert publish == {
            "version": SOURCE_VERSION,
            "tag": "v1.1.0-rc.1",
            "prerelease": True,
            "notes": "release/notes/1.1.0-rc.1.md",
        }
        # Profile acceptance may be completed before observation, but stable
        # publication must remain closed until the independent observation gate.
        assert all(item["stableDecision"] == "accepted" for item in decision_by_id.values())
        assert plan["publication"]["allowed"] is False
        assert observation["window"]["status"] == "open"
        assert observation["summary"]["stableDecision"] == "pending"
    elif version == TARGET_VERSION:
        assert plan["publication"]["allowed"] is True
        assert observation["window"]["status"] == "complete"
        assert observation["summary"] == {
            "compatibilityCriticalDefectsFound": 0,
            "compatibilityCriticalDefectsOpen": 0,
            "openReports": 0,
            "stableDecision": "approved",
        }
        assert calendar["specVersion"] == months["specVersion"] == localizations["specVersion"] == TARGET_VERSION
        assert calendar["status"] == months["status"] == localizations["status"] == "stable"
        assert publish == {
            "version": TARGET_VERSION,
            "tag": "v1.1.0",
            "prerelease": False,
            "notes": "release/notes/1.1.0.md",
        }

        for profile_id, current in current_profiles.items():
            source = copy.deepcopy(source_profiles[profile_id])
            actual = copy.deepcopy(current)
            if profile_id in NEW_PROFILES:
                assert decision_by_id[profile_id]["stableDecision"] == stable_record[profile_id]["stableDecision"]
                expected_status = "stable" if decision_by_id[profile_id]["stableDecision"] == "accepted" else "reviewed"
                assert actual["review"]["status"] == expected_status
                # Compare every other field to the immutable RC snapshot.
                actual["review"]["status"] = source["review"]["status"]
            else:
                assert actual["review"]["status"] == source["review"]["status"] == "stable"
            assert actual == source, profile_id
    else:
        # Once a later compatible release exists, this becomes historical
        # proof. Require that stable v1.1 has been immutably recorded rather
        # than forcing a future working tree to stay at v1.1 forever.
        stable = next(item for item in ledger["releases"] if item["version"] == TARGET_VERSION)
        assert stable["tag"] == "v1.1.0"
        assert stable["archiveSha256"]
        assert plan["publication"]["allowed"] is True

    for path in (
        manifest["sourceIdentity"],
        manifest["stablePlan"],
        manifest["observation"],
        manifest["profileDecisions"],
        manifest["targetPublication"]["notes"],
    ):
        assert (ROOT / path).is_file(), path

    assert manifest["targetPublication"] == {
        "tag": "v1.1.0",
        "prerelease": False,
        "notes": "release/notes/1.1.0.md",
    }

    print("Tredecadia v1.1 RC-to-stable transition validation: OK")


if __name__ == "__main__":
    main()
