#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reference implementation of the Tredecadia civil calendar.

The normative definition lives in ``specification/`` and ``registry/``.
This module is deliberately dependency-free and supports all integer
Tredecadia years and all integer proleptic-Gregorian astronomical years.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass

TE_GREGORIAN_YEAR_OFFSET = 9999
_GREGORIAN_MONTH_LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
_TE_RE = re.compile(r"^(-?[0-9]{5,})-(?:([0-9]{2})-([0-9]{2})|(EQ|ED))$")
_GREGORIAN_RE = re.compile(r"^(-?[0-9]+)-([0-9]{2})-([0-9]{2})$")


class TredecadiaError(ValueError):
    """Raised when a Tredecadia or conversion value is invalid."""


def format_year(year: int) -> str:
    """Return the canonical Tredecadia year field."""
    magnitude = f"{abs(year):05d}"
    return f"-{magnitude}" if year < 0 else magnitude


def format_display_year(year: int, *, typographic_minus: bool = True) -> str:
    """Return an unpadded human-facing Tredecadia year coordinate.

    This is presentation only and is intentionally not accepted by the strict
    canonical parser as an alternate machine serialization.
    """
    magnitude = str(abs(year))
    if year >= 0:
        return magnitude
    sign = "−" if typographic_minus else "-"
    return f"{sign}{magnitude}"


def format_gregorian_year(year: int) -> str:
    """Format an astronomical Gregorian year for reference-output use."""
    magnitude = f"{abs(year):04d}"
    return f"-{magnitude}" if year < 0 else magnitude


def gregorian_is_leap(year: int) -> bool:
    """Return whether an astronomical proleptic-Gregorian year is leap."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def tredecadia_is_leap(year: int) -> bool:
    """Return whether Tredecadia Era year ``year`` contains Earth Day."""
    return gregorian_is_leap(year - 9998)


def _gregorian_month_length(year: int, month: int) -> int:
    if not 1 <= month <= 12:
        raise TredecadiaError("Gregorian month must be in 1..12")
    if month == 2 and gregorian_is_leap(year):
        return 29
    return _GREGORIAN_MONTH_LENGTHS[month - 1]


def _validate_gregorian(year: int, month: int, day: int) -> None:
    length = _gregorian_month_length(year, month)
    if not 1 <= day <= length:
        raise TredecadiaError("invalid Gregorian day")


def _days_before_gregorian_year(year: int) -> int:
    """Days from astronomical Gregorian 0001-01-01 to ``year-01-01``.

    The result may be negative. Python's floor-division semantics make the
    standard Gregorian cycle formula valid for zero and negative years too.
    """
    y = year - 1
    return 365 * y + y // 4 - y // 100 + y // 400


def _gregorian_ordinal(year: int, month: int, day: int) -> int:
    _validate_gregorian(year, month, day)
    ordinal = _days_before_gregorian_year(year)
    ordinal += sum(_gregorian_month_length(year, m) for m in range(1, month))
    return ordinal + day - 1


def _gregorian_from_ordinal(ordinal: int) -> GregorianDate:
    cycle = ordinal // 146097
    lo = cycle * 400 + 1
    hi = lo + 399
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if _days_before_gregorian_year(mid) <= ordinal:
            lo = mid
        else:
            hi = mid - 1

    year = lo
    day_of_year = ordinal - _days_before_gregorian_year(year)
    month = 1
    while True:
        length = _gregorian_month_length(year, month)
        if day_of_year < length:
            return GregorianDate(year, month, day_of_year + 1)
        day_of_year -= length
        month += 1


@dataclass(frozen=True, slots=True)
class GregorianDate:
    """A date in the proleptic Gregorian calendar, astronomical year numbering."""

    year: int
    month: int
    day: int

    def __post_init__(self) -> None:
        _validate_gregorian(self.year, self.month, self.day)

    @property
    def canonical(self) -> str:
        return f"{format_gregorian_year(self.year)}-{self.month:02d}-{self.day:02d}"

    def __str__(self) -> str:
        return self.canonical


@dataclass(frozen=True, slots=True)
class TredecadiaDate:
    """A regular or intercalary Tredecadia Era date."""

    year: int
    month: int | None = None
    day: int | None = None
    special: str | None = None

    def __post_init__(self) -> None:
        if self.special is not None:
            if self.special not in {"EQ", "ED"}:
                raise TredecadiaError("special date must be EQ or ED")
            if self.month is not None or self.day is not None:
                raise TredecadiaError("intercalary dates have no month/day")
            if self.special == "ED" and not tredecadia_is_leap(self.year):
                raise TredecadiaError("Earth Day exists only in a leap Tredecadia year")
            return

        if self.month is None or self.day is None:
            raise TredecadiaError("regular dates require both month and day")
        if not 1 <= self.month <= 13:
            raise TredecadiaError("Tredecadia month must be in 1..13")
        if not 1 <= self.day <= 28:
            raise TredecadiaError("Tredecadia day must be in 1..28")

    @property
    def canonical(self) -> str:
        year = format_year(self.year)
        if self.special is not None:
            return f"{year}-{self.special}"
        assert self.month is not None and self.day is not None
        return f"{year}-{self.month:02d}-{self.day:02d}"

    def __str__(self) -> str:
        return self.canonical


def parse_tredecadia(text: str) -> TredecadiaDate:
    """Parse only canonical ASCII Tredecadia date notation.

    This intentionally rejects a leading plus sign, negative zero, fewer than
    five year digits, redundant leading zeroes, non-ASCII digits, Unicode
    minus signs, presentation whitespace, and alternate separators.
    """
    match = _TE_RE.fullmatch(text)
    if match is None:
        raise TredecadiaError("invalid canonical Tredecadia date")

    year_field, month_field, day_field, special = match.groups()
    year = int(year_field)
    if format_year(year) != year_field:
        raise TredecadiaError("non-canonical Tredecadia year field")

    if special is not None:
        return TredecadiaDate(year, special=special)
    assert month_field is not None and day_field is not None
    return TredecadiaDate(year, int(month_field), int(day_field))


def parse_gregorian(text: str) -> GregorianDate:
    """Parse an astronomical proleptic-Gregorian ASCII reference date.

    The external Gregorian notation is intentionally permissive about year
    width; the year is an integer coordinate. A leading plus sign is rejected.
    """
    match = _GREGORIAN_RE.fullmatch(text)
    if match is None:
        raise TredecadiaError("invalid Gregorian reference date")
    year, month, day = match.groups()
    return GregorianDate(int(year), int(month), int(day))


def to_gregorian(value: TredecadiaDate) -> GregorianDate:
    """Convert a Tredecadia date to astronomical proleptic Gregorian."""
    start_year = value.year - TE_GREGORIAN_YEAR_OFFSET

    if value.special == "EQ":
        return GregorianDate(start_year, 3, 20)
    if value.special == "ED":
        return GregorianDate(start_year + 1, 3, 19)

    assert value.month is not None and value.day is not None
    regular_offset = (value.month - 1) * 28 + value.day - 1
    ordinal = _gregorian_ordinal(start_year, 3, 21) + regular_offset
    return _gregorian_from_ordinal(ordinal)


def from_gregorian(value: GregorianDate) -> TredecadiaDate:
    """Convert astronomical proleptic Gregorian to Tredecadia Era."""
    if (value.month, value.day) >= (3, 20):
        year = value.year + 9999
    else:
        year = value.year + 9998

    start_gregorian_year = year - 9999
    start = _gregorian_ordinal(start_gregorian_year, 3, 20)
    delta = _gregorian_ordinal(value.year, value.month, value.day) - start

    if delta == 0:
        return TredecadiaDate(year, special="EQ")
    if 1 <= delta <= 364:
        month0, day0 = divmod(delta - 1, 28)
        return TredecadiaDate(year, month0 + 1, day0 + 1)
    if delta == 365 and tredecadia_is_leap(year):
        return TredecadiaDate(year, special="ED")
    raise AssertionError("derived Gregorian date is outside its Tredecadia year")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tredecadia",
        description="Reference Tredecadia Era / Gregorian civil converter",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    fg = sub.add_parser("from-gregorian", help="convert astronomical Gregorian to Tredecadia")
    fg.add_argument("date", help="Gregorian date, e.g. 2026-09-15 or 0-03-20")

    tg = sub.add_parser("to-gregorian", help="convert canonical Tredecadia to Gregorian")
    tg.add_argument("date", help="Tredecadia date, e.g. 12025-07-11 or 00000-EQ")

    return parser


def _normalize_cli_argv(argv: list[str]) -> list[str]:
    """Let a negative-year date be used as a positional without explicit ``--``."""
    if (
        len(argv) == 2
        and argv[0] in {"from-gregorian", "to-gregorian"}
        and argv[1].startswith("-")
    ):
        return [argv[0], "--", argv[1]]
    return argv


def main(argv: list[str] | None = None) -> int:
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = _build_parser().parse_args(_normalize_cli_argv(raw_argv))
    try:
        if args.command == "from-gregorian":
            print(from_gregorian(parse_gregorian(args.date)).canonical)
        else:
            print(to_gregorian(parse_tredecadia(args.date)).canonical)
    except TredecadiaError as exc:
        raise SystemExit(f"error: {exc}") from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
