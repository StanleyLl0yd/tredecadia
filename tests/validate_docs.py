#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Cross-check duplicated Tredecadia documentation against canonical data."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONTHS = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))["months"]


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def exactly_once(document: str, row: str, path: str) -> None:
    count = document.count(row)
    assert count == 1, f"{path}: expected one canonical row, found {count}: {row}"


def validate_month_tables() -> None:
    readme = text("README.md")
    naming = text("specification/month-naming-standard.md")
    localization = text("specification/localization.md")

    for month in MONTHS:
        n = month["number"]
        name = month["canonical"]
        short6 = month["short6"]
        short4 = month["short4"]
        syllables = "-".join(month["syllables"])
        ipa = f"/{month['ipa']}/"
        ru = month["localizations"]["ru"]

        exactly_once(readme, f"| {n:02d} | {name} | {short6} | {short4} |", "README.md")
        exactly_once(
            naming,
            f"| {n:02d} | {name} | {syllables} | {ipa} | {short6} | {short4} |",
            "month-naming-standard.md",
        )
        exactly_once(localization, f"| {n:02d} | {name} | {ru} |", "localization.md")


def validate_m1_docs() -> None:
    calendar = text("specification/calendar-standard.md")
    notation = text("specification/date-notation.md")
    conversion = text("specification/conversion-standard.md")
    readme = text("README.md")
    roadmap = text("ROADMAP.md")

    assert "external parameter" not in calendar
    assert "mandatory epoch" not in calendar
    assert "symbolic forms are provisional" not in notation
    assert "## Open item" not in notation

    for token in ("Y-01-01", "Y-EQ", "Y-ED", "Y+1", "03-21", "03-20"):
        assert token in conversion

    assert "specification/conversion-standard.md" in readme
    assert "fixed March-equinoctial" in readme
    assert "fixed March-equinoctial" in roadmap
    assert "Status: **complete**" in roadmap


def validate_license_docs() -> None:
    umbrella = text("LICENSE.md").lower()
    cc = text("LICENSES/CC-BY-4.0.md").lower()
    mit = text("LICENSES/MIT.txt")

    for phrase in ("documentation", "machine-readable registries", "test vectors"):
        assert phrase in umbrella
        assert phrase in cc
    assert "source code" in umbrella
    assert "ci/workflow code" in umbrella
    assert mit.startswith("MIT License\n")


def main() -> None:
    validate_month_tables()
    validate_m1_docs()
    validate_license_docs()
    print("Tredecadia documentation consistency: OK")


if __name__ == "__main__":
    main()
