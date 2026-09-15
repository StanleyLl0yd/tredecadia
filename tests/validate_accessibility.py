#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate signed-year display/accessibility policy against the reference parser."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference" / "python"))

import tredecadia as ref  # noqa: E402

VECTORS = json.loads((ROOT / "tests/accessibility-vectors.json").read_text(encoding="utf-8"))
MONTHS = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))["months"]
MONTH_BY_NUMBER = {month["number"]: month for month in MONTHS}


def assert_rejected(value: str) -> None:
    try:
        ref.parse_tredecadia(value)
    except ref.TredecadiaError:
        return
    raise AssertionError(f"strict parser accepted presentation/non-canonical input: {value!r}")


def validate_display_years() -> None:
    for item in VECTORS["displayYears"]:
        year = item["year"]
        assert ref.format_year(year) == item["canonical"]
        assert ref.format_display_year(year) == item["human"]
        if year < 0:
            assert ref.format_display_year(year, typographic_minus=False) == f"-{abs(year)}"
        else:
            assert ref.format_display_year(year, typographic_minus=False) == str(year)

        if item["human"] != item["canonical"]:
            assert_rejected(f"{item['human']}-EQ")


def validate_semantic_labels() -> None:
    for item in VECTORS["semanticLabels"]:
        value = ref.parse_tredecadia(item["canonical"])
        assert value.year == item["year"]
        if item["kind"] == "intercalary":
            assert value.special in {"EQ", "ED"}
            expanded = {"EQ": "Equinox / New Year Day", "ED": "Earth Day"}[value.special]
            assert expanded == item["name"]
            assert value.month is None and value.day is None
        else:
            assert value.special is None
            assert value.month == item["month"]
            assert value.day == item["day"]
            assert MONTH_BY_NUMBER[value.month]["canonical"] == item["monthName"]


def validate_rejections() -> None:
    for value in VECTORS["mustRejectCanonicalParser"]:
        assert_rejected(value)
    assert_rejected("−00001-01-01")
    assert_rejected("١٢٠٢٥-07-11")
    assert_rejected("１２０２５-07-11")


def validate_documentation() -> None:
    notation = (ROOT / "specification/date-notation.md").read_text(encoding="utf-8")
    rationale = (ROOT / "rationale/accessibility-years.md").read_text(encoding="utf-8")
    for phrase in (
        "ASCII decimal digits",
        "Unicode MINUS SIGN",
        "Accessible semantic labels",
        "Equinox / New Year Day",
        "Earth Day",
        "forgiving human-input layer",
    ):
        assert phrase in notation, phrase
    for phrase in ("Machine syntax and human presentation", "Negative Tredecadia years", "Strict parsing boundary"):
        assert phrase in rationale, phrase


def main() -> None:
    assert VECTORS["specVersion"] == citation_version()
    assert VECTORS["policy"] == "signed-year-accessibility-v1"
    validate_display_years()
    validate_semantic_labels()
    validate_rejections()
    validate_documentation()
    print("Tredecadia signed-year accessibility validation: OK")


if __name__ == "__main__":
    main()
