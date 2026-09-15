#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate Tredecadia M1 conversion semantics and published vectors."""

from __future__ import annotations

import json
from pathlib import Path

from calendar_math import (
    GregorianDate,
    TredecadiaDate,
    gregorian_is_leap,
    gregorian_to_ordinal,
    gregorian_to_tredecadia,
    ordinal_to_gregorian,
    tredecadia_is_leap,
    tredecadia_to_gregorian,
)

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "tests" / "conversion-vectors.json"


def parse_gregorian(text: str) -> GregorianDate:
    year, month, day = (int(part) for part in text.split("-"))
    return GregorianDate(year, month, day)


def parse_tredecadia(text: str) -> TredecadiaDate:
    parts = text.split("-")
    if len(parts) == 2:
        return TredecadiaDate(int(parts[0]), special=parts[1])
    if len(parts) == 3:
        return TredecadiaDate(int(parts[0]), int(parts[1]), int(parts[2]))
    raise ValueError(f"invalid Tredecadia vector: {text}")


def assert_raises_value_error(fn, *args) -> None:
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(f"expected ValueError from {fn.__name__}{args}")


def validate_vectors() -> None:
    vectors = json.loads(VECTORS.read_text(encoding="utf-8"))
    assert vectors["profile"] == "fixed-march-equinoctial-m1-proposal"

    epoch_g = parse_gregorian(vectors["epoch"]["gregorian"])
    epoch_t = parse_tredecadia(vectors["epoch"]["tredecadia"])
    assert epoch_g == GregorianDate(1, 3, 21)
    assert epoch_t == TredecadiaDate(1, 1, 1)
    assert tredecadia_to_gregorian(epoch_t) == epoch_g
    assert gregorian_to_tredecadia(epoch_g) == epoch_t

    for item in vectors["leapPredicates"]:
        year = item["tredecadiaYear"]
        reason_year = item["reasonGregorianYear"]
        assert reason_year == year + 1
        assert tredecadia_is_leap(year) is item["isLeap"]
        assert tredecadia_is_leap(year) == gregorian_is_leap(reason_year)

    for pair in vectors["pairs"]:
        g = parse_gregorian(pair["gregorian"])
        t = parse_tredecadia(pair["tredecadia"])
        assert tredecadia_to_gregorian(t) == g, pair
        assert gregorian_to_tredecadia(g) == t, pair
        assert str(g) == pair["gregorian"]
        assert t.canonical == pair["tredecadia"]


def validate_cycles() -> None:
    # The leap pattern is the Gregorian 400-year pattern shifted by one year.
    assert sum(tredecadia_is_leap(y) for y in range(1, 401)) == 97
    assert sum(tredecadia_is_leap(y) for y in range(401, 801)) == 97

    # Century exceptions and 400-year restoration.
    assert tredecadia_is_leap(1999)  # Gregorian 2000
    assert not tredecadia_is_leap(2099)  # Gregorian 2100
    assert not tredecadia_is_leap(2199)  # Gregorian 2200
    assert not tredecadia_is_leap(2299)  # Gregorian 2300
    assert tredecadia_is_leap(2399)  # Gregorian 2400


def validate_round_trips() -> None:
    # Exhaust two complete 400-year leap cycles, including every regular and
    # intercalary Tredecadia date.
    for year in range(1, 801):
        for month in range(1, 14):
            for day in range(1, 29):
                t = TredecadiaDate(year, month, day)
                assert gregorian_to_tredecadia(tredecadia_to_gregorian(t)) == t

        eq = TredecadiaDate(year, special="EQ")
        assert gregorian_to_tredecadia(tredecadia_to_gregorian(eq)) == eq

        if tredecadia_is_leap(year):
            ed = TredecadiaDate(year, special="ED")
            assert gregorian_to_tredecadia(tredecadia_to_gregorian(ed)) == ed

    # Also exhaust Gregorian civil dates over the same conversion interval.
    start = gregorian_to_ordinal(1, 3, 21)
    end = gregorian_to_ordinal(801, 3, 21)
    for ordinal in range(start, end):
        g = ordinal_to_gregorian(ordinal)
        assert tredecadia_to_gregorian(gregorian_to_tredecadia(g)) == g


def validate_boundaries() -> None:
    # Earth Day cannot be fabricated in an ordinary Tredecadia year.
    assert_raises_value_error(TredecadiaDate, 2024, None, None, "ED")

    # Gregorian dates before the conversion epoch are outside the v1 profile.
    assert_raises_value_error(gregorian_to_tredecadia, GregorianDate(1, 3, 20))

    # Expanded positive years remain arithmetic, not a four-digit implementation limit.
    t = TredecadiaDate(10000, 1, 1)
    assert tredecadia_to_gregorian(t) == GregorianDate(10000, 3, 21)
    assert gregorian_to_tredecadia(GregorianDate(10000, 3, 21)) == t

    # EQ is always fixed to March 20 of the following Gregorian year.
    for year in (1, 2023, 2024, 2099, 2399, 9999, 10000):
        assert tredecadia_to_gregorian(TredecadiaDate(year, special="EQ")) == GregorianDate(year + 1, 3, 20)
        if tredecadia_is_leap(year):
            assert tredecadia_to_gregorian(TredecadiaDate(year, special="ED")) == GregorianDate(year + 1, 3, 19)


def main() -> None:
    validate_vectors()
    validate_cycles()
    validate_round_trips()
    validate_boundaries()
    print("Tredecadia conversion validation: OK")


if __name__ == "__main__":
    main()
