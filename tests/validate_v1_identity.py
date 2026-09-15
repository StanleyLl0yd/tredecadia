#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate immutable v1 identity against the published RC baseline."""

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
    baseline = load("release/v1-identity.json")
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")

    assert baseline["baselineVersion"] == 1
    assert baseline["sourceTag"] == "v1.0.0-rc.1"
    assert baseline["sourceCommit"] == "937d8d681fcce6095d6a4d196783136b908c1be5"
    assert baseline["schemaVersions"] == {
        "calendar": calendar["schemaVersion"],
        "months": months["schemaVersion"],
        "localizations": localizations["schemaVersion"],
    }

    actual_calendar = {
        key: calendar[key]
        for key in ("profile", "era", "regularGrid", "epoch", "civilAnchor", "leapRule", "intercalary")
    }
    assert actual_calendar == baseline["calendar"]
    assert months["pronunciation"] == baseline["pronunciation"]
    assert canonical_month_surface(months) == baseline["months"]

    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == set(baseline["localizationMaps"])
    for profile_id, syllable_map in baseline["localizationMaps"].items():
        assert profiles[profile_id]["syllableMap"] == syllable_map

    grammar = baseline["dateGrammar"]
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

    print("Tredecadia immutable v1 identity baseline: OK")


if __name__ == "__main__":
    main()
