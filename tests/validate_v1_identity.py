#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate immutable RC1 history and the current RC2 v1 identity candidate."""

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

    # RC2 changes only the explicitly reviewed weekday identity/schema surface.
    assert rc2["baselineVersion"] == 2
    assert rc2["release"] == {
        "version": "1.0.0-rc.2",
        "tag": "v1.0.0-rc.2",
        "publicationStatus": "awaiting-publication",
    }
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

    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == set(rc2["localizationMaps"])
    for profile_id, syllable_map in rc2["localizationMaps"].items():
        assert profiles[profile_id]["syllableMap"] == syllable_map

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

    print("Tredecadia RC1 history + RC2 v1 identity validation: OK")


if __name__ == "__main__":
    main()
