#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Cross-check the public Python reference implementation against M1 data."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference" / "python"))
sys.path.insert(0, str(ROOT / "tests"))

import calendar_math as oracle  # noqa: E402
import tredecadia as ref  # noqa: E402

VECTORS = json.loads((ROOT / "tests" / "conversion-vectors.json").read_text(encoding="utf-8"))
SCRIPT = ROOT / "reference" / "python" / "tredecadia.py"


def ref_tuple(value: ref.GregorianDate | ref.TredecadiaDate) -> tuple[object, ...]:
    if isinstance(value, ref.GregorianDate):
        return value.year, value.month, value.day
    return value.year, value.month, value.day, value.special


def oracle_tuple(value: oracle.GregorianDate | oracle.TredecadiaDate) -> tuple[object, ...]:
    if isinstance(value, oracle.GregorianDate):
        return value.year, value.month, value.day
    return value.year, value.month, value.day, value.special


def validate_published_vectors() -> None:
    for item in VECTORS["pairs"]:
        g_data = item["gregorianAstronomical"]
        g = ref.GregorianDate(g_data["year"], g_data["month"], g_data["day"])
        t = ref.parse_tredecadia(item["tredecadia"])
        assert ref.from_gregorian(g) == t, item
        assert ref.to_gregorian(t) == g, item

    for item in VECTORS["leapPredicates"]:
        assert ref.tredecadia_is_leap(item["tredecadiaYear"]) is item["isLeap"]


def validate_against_oracle() -> None:
    windows = [(-200, 200), (200, 600), (9600, 10400), (11800, 12200)]

    for start, stop in windows:
        for year in range(start, stop):
            assert ref.tredecadia_is_leap(year) == oracle.tredecadia_is_leap(year)

            specials = ["EQ"] + (["ED"] if ref.tredecadia_is_leap(year) else [])
            for special in specials:
                rt = ref.TredecadiaDate(year, special=special)
                ot = oracle.TredecadiaDate(year, special=special)
                assert ref_tuple(ref.to_gregorian(rt)) == oracle_tuple(oracle.tredecadia_to_gregorian(ot))

            for month in range(1, 14):
                for day in range(1, 29):
                    rt = ref.TredecadiaDate(year, month, day)
                    ot = oracle.TredecadiaDate(year, month, day)
                    rg = ref.to_gregorian(rt)
                    og = oracle.tredecadia_to_gregorian(ot)
                    assert ref_tuple(rg) == oracle_tuple(og)
                    assert ref.from_gregorian(rg) == rt

    civil_windows = [(-50, 50), (1950, 2050)]
    for start_year, stop_year in civil_windows:
        start = oracle.gregorian_to_ordinal(start_year, 1, 1)
        stop = oracle.gregorian_to_ordinal(stop_year, 1, 1)
        for ordinal in range(start, stop):
            og = oracle.ordinal_to_gregorian(ordinal)
            rg = ref.GregorianDate(og.year, og.month, og.day)
            rt = ref.from_gregorian(rg)
            ot = oracle.gregorian_to_tredecadia(og)
            assert ref_tuple(rt) == oracle_tuple(ot)
            assert ref.to_gregorian(rt) == rg


def validate_parsing() -> None:
    canonical = (
        "00000-EQ",
        "00000-01-01",
        "09998-ED",
        "12025-07-11",
        "-00001-EQ",
        "-10000-13-28",
    )
    for value in canonical:
        assert ref.parse_tredecadia(value).canonical == value

    invalid = (
        "0000-EQ",
        "+00001-EQ",
        "-00000-EQ",
        "000001-EQ",
        "-000001-EQ",
        "−00001-EQ",
        " 12025-07-11",
        "12025-07-11 ",
        "12025/07/11",
        "١٢٠٢٥-07-11",
        "１２０２５-07-11",
        "12025-00-01",
        "12025-14-01",
        "12025-01-00",
        "12025-01-29",
        "12023-ED",
        "12025-eq",
    )
    for value in invalid:
        try:
            ref.parse_tredecadia(value)
        except ref.TredecadiaError:
            pass
        else:
            raise AssertionError(f"reference parser accepted invalid value: {value}")

    assert ref.parse_gregorian("0-03-20") == ref.GregorianDate(0, 3, 20)
    assert ref.parse_gregorian("-9999-03-20") == ref.GregorianDate(-9999, 3, 20)

    # Reference Gregorian input is also ASCII, avoiding digit-script
    # confusables at the CLI boundary.
    for value in ("٢٠٢٦-09-15", "２０２６-09-15", "−9999-03-20"):
        try:
            ref.parse_gregorian(value)
        except ref.TredecadiaError:
            pass
        else:
            raise AssertionError(f"Gregorian reference parser accepted non-ASCII input: {value}")


def validate_display_years() -> None:
    assert ref.format_display_year(0) == "0"
    assert ref.format_display_year(1) == "1"
    assert ref.format_display_year(12025) == "12025"
    assert ref.format_display_year(-1) == "−1"
    assert ref.format_display_year(-10000) == "−10000"
    assert ref.format_display_year(-1, typographic_minus=False) == "-1"

    # Display forms intentionally differ from canonical storage for padded or
    # negative small-magnitude years.
    assert ref.format_year(1) == "00001"
    assert ref.format_year(-1) == "-00001"


def validate_cli() -> None:
    cases = [
        (["from-gregorian", "2026-09-15"], "12025-07-11"),
        (["from-gregorian", "-9999-03-20"], "00000-EQ"),
        (["to-gregorian", "12025-07-11"], "2026-09-15"),
        (["to-gregorian", "00000-EQ"], "-9999-03-20"),
    ]
    for arguments, expected in cases:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        assert completed.stdout.strip() == expected


def main() -> None:
    validate_published_vectors()
    validate_against_oracle()
    validate_parsing()
    validate_display_years()
    validate_cli()
    print("Tredecadia Python reference implementation: OK")


if __name__ == "__main__":
    main()
