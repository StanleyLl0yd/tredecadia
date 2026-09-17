#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate immutable RC1/RC2 history and the compatible v1 identity surface."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference" / "python"))

import tredecadia as ref  # noqa: E402


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def canonical_month_surface(months: dict) -> list[dict]:
    return [
        {
            "number": month["number"],
            "canonical": month["canonical"],
            "syllables": month["syllables"],
            "short6": month["short6"],
            "short4": month["short4"],
        }
        for month in months["months"]
    ]


def assert_rejected(value: str) -> None:
    try:
        ref.parse_tredecadia(value)
    except ref.TredecadiaError:
        return
    raise AssertionError(f"v1 parser accepted non-canonical value: {value!r}")


def main() -> None:
    rc1 = load("release/v1-identity.json")
    rc2 = load("release/rc2-identity.json")
    published = load("release/published-releases.json")
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")

    # Published RC1 remains an immutable historical baseline.
    assert rc1["baselineVersion"] == 1
    assert rc1["sourceTag"] == "v1.0.0-rc.1"
    assert rc1["sourceCommit"] == "937d8d681fcce6095d6a4d196783136b908c1be5"
    assert rc1["schemaVersions"] == {"calendar": 1, "months": 3, "localizations": 1}
    assert rc1["calendar"]["regularGrid"]["weekdays"] == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

    # RC2 changed only the explicitly reviewed weekday identity/schema surface
    # and remains bound to its exact published source/archive identity.
    assert rc2["baselineVersion"] == 2
    release = rc2["release"]
    assert release == {
        "version": "1.0.0-rc.2",
        "tag": "v1.0.0-rc.2",
        "publicationStatus": "published",
        "commit": "b816d613618d51515d910e0d3bdb9d2f211b6d22",
        "publishedAt": "2026-09-16T09:44:59Z",
        "archiveSha256": "23e40180098c656c88aa4ba27c6989ac053d9ce8b8029c9ce2e3b16946bf32ec",
    }
    rc2_ledger = next(entry for entry in published["releases"] if entry["version"] == release["version"])
    for key in ("version", "tag", "commit", "publishedAt", "archiveSha256"):
        assert rc2_ledger[key] == release[key]

    assert rc2["historicalPredecessor"] == "release/v1-identity.json"
    assert rc2["schemaVersions"] == {
        "calendar": calendar["schemaVersion"],
        "months": months["schemaVersion"],
        "localizations": localizations["schemaVersion"],
    } == {"calendar": 2, "months": 3, "localizations": 1}

    actual_calendar = {
        key: calendar[key]
        for key in ("profile", "era", "regularGrid", "epoch", "civilAnchor", "leapRule", "intercalary")
    }
    assert actual_calendar == rc2["calendar"]
    assert months["pronunciation"] == rc2["pronunciation"]
    assert canonical_month_surface(months) == rc2["months"]

    # The three v1.0 localization maps are part of the already-published v1
    # identity and must remain byte-equivalent at the mapping level. Compatible
    # later v1 minor releases may add reviewed display profiles, but may not
    # mutate or remove these baseline maps.
    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    baseline_profile_ids = set(rc2["localizationMaps"])
    assert baseline_profile_ids <= set(profiles)
    for profile_id, syllable_map in rc2["localizationMaps"].items():
        assert profiles[profile_id]["syllableMap"] == syllable_map

    extra_profile_ids = set(profiles) - baseline_profile_ids
    if extra_profile_ids:
        pack = load("rationale/additional-script-localization-candidates.json")
        decisions = load("rationale/additional-script-localization-decisions.json")
        candidate_by_id = {profile["id"]: profile for profile in pack["profiles"]}
        decision_by_id = {entry["id"]: entry for entry in decisions["decisions"]}
        assert extra_profile_ids == set(candidate_by_id) == {
            "ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva", "bn-Beng", "fa-Arab"
        }
        for profile_id in extra_profile_ids:
            assert decision_by_id[profile_id]["decision"] == "accept-reviewed"
            assert profiles[profile_id]["review"]["status"] == "reviewed"
            assert profiles[profile_id]["syllableMap"] == candidate_by_id[profile_id]["syllableMap"]
            assert profiles[profile_id]["aliases"] == candidate_by_id[profile_id]["aliases"]

    # Prove the RC2 correction did not drift any other v1 identity class.
    assert rc2["months"] == rc1["months"]
    assert rc2["pronunciation"] == rc1["pronunciation"]
    assert rc2["dateGrammar"] == rc1["dateGrammar"]
    assert rc2["localizationMaps"] == rc1["localizationMaps"]
    for key in ("profile", "era", "epoch", "civilAnchor", "leapRule", "intercalary"):
        assert rc2["calendar"][key] == rc1["calendar"][key]
    for key in ("monthsPerYear", "daysPerMonth", "regularDaysPerYear", "weeksPerMonth"):
        assert rc2["calendar"]["regularGrid"][key] == rc1["calendar"]["regularGrid"][key]

    weekdays = rc2["calendar"]["regularGrid"]["weekdays"]
    assert [day["id"] for day in weekdays] == [f"W{i}" for i in range(1, 8)]
    assert [day["canonical"] for day in weekdays] == ["Mene", "Noko", "Kese", "Zoyo", "Sote", "Yemo", "Toze"]

    grammar = rc2["dateGrammar"]
    assert grammar["minimumYearMagnitudeDigits"] == calendar["era"]["canonicalMinimumDigits"] == 5
    assert grammar["asciiDigitsOnly"] is True
    assert grammar["negativeSign"] == "-"
    assert grammar["leadingPlusAllowed"] is False
    assert grammar["negativeZeroAllowed"] is False
    assert grammar["redundantPaddingAllowed"] is False
    assert grammar["regularMonthRange"] == [1, 13]
    assert grammar["regularDayRange"] == [1, 28]
    assert grammar["intercalaryTokens"] == ["EQ", "ED"]
    assert grammar["intercalaryTokensCaseSensitive"] is True

    for value in ("00000-EQ", "00000-01-01", "12025-07-11", "-00001-01-01"):
        assert ref.parse_tredecadia(value).canonical == value
    for value in (
        "0000-EQ", "+00001-EQ", "-00000-EQ", "000001-EQ", "-000001-EQ",
        "−00001-EQ", "١٢٠٢٥-07-11", "１２０２５-07-11", "12025-eq",
        "12025-00-01", "12025-14-01", "12025-01-00", "12025-01-29",
    ):
        assert_rejected(value)

    print("Tredecadia immutable v1 identity + compatible localization extension validation: OK")


if __name__ == "__main__":
    main()
