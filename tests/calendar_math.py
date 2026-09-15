# SPDX-License-Identifier: MIT
"""Executable calendar arithmetic for validating the Tredecadia M1 proposal.

This module is a test oracle, not yet a stable public API.
"""

from __future__ import annotations

from dataclasses import dataclass


COMMON_MONTH_LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


@dataclass(frozen=True)
class GregorianDate:
    year: int
    month: int
    day: int

    def __post_init__(self) -> None:
        validate_gregorian(self.year, self.month, self.day)

    def __str__(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


@dataclass(frozen=True)
class TredecadiaDate:
    year: int
    month: int | None = None
    day: int | None = None
    special: str | None = None

    def __post_init__(self) -> None:
        if self.year < 1:
            raise ValueError("Tredecadia v1 years must be positive")
        if self.special is not None:
            if self.special not in {"ED", "EQ"}:
                raise ValueError("unknown intercalary code")
            if self.month is not None or self.day is not None:
                raise ValueError("intercalary dates have no month/day")
            if self.special == "ED" and not tredecadia_is_leap(self.year):
                raise ValueError("Earth Day exists only in leap years")
        else:
            if self.month is None or self.day is None:
                raise ValueError("regular dates require month and day")
            if not 1 <= self.month <= 13:
                raise ValueError("month must be in 1..13")
            if not 1 <= self.day <= 28:
                raise ValueError("day must be in 1..28")

    @property
    def canonical(self) -> str:
        if self.special is not None:
            return f"{self.year:04d}-{self.special}"
        assert self.month is not None and self.day is not None
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


def gregorian_is_leap(year: int) -> bool:
    if year < 1:
        raise ValueError("Gregorian conversion years must be positive")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def tredecadia_is_leap(year: int) -> bool:
    if year < 1:
        raise ValueError("Tredecadia v1 years must be positive")
    return gregorian_is_leap(year + 1)


def gregorian_month_length(year: int, month: int) -> int:
    if not 1 <= month <= 12:
        raise ValueError("Gregorian month must be in 1..12")
    if month == 2 and gregorian_is_leap(year):
        return 29
    return COMMON_MONTH_LENGTHS[month - 1]


def validate_gregorian(year: int, month: int, day: int) -> None:
    if year < 1:
        raise ValueError("Gregorian conversion years must be positive")
    length = gregorian_month_length(year, month)
    if not 1 <= day <= length:
        raise ValueError("invalid Gregorian day")


def days_before_gregorian_year(year: int) -> int:
    if year < 1:
        raise ValueError("Gregorian conversion years must be positive")
    y = year - 1
    return 365 * y + y // 4 - y // 100 + y // 400


def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    """Return a zero-based ordinal where Gregorian 0001-01-01 is 0."""
    validate_gregorian(year, month, day)
    result = days_before_gregorian_year(year)
    for m in range(1, month):
        result += gregorian_month_length(year, m)
    return result + day - 1


def ordinal_to_gregorian(ordinal: int) -> GregorianDate:
    if ordinal < 0:
        raise ValueError("dates before Gregorian 0001-01-01 are outside the v1 domain")

    cycle = ordinal // 146097  # 400 Gregorian years
    low = cycle * 400 + 1
    high = low + 399

    # Find the unique Gregorian year whose first ordinal is <= ordinal and
    # whose successor starts after ordinal. Binary search keeps conversion
    # fast even for expanded year numbers.
    while low < high:
        mid = (low + high + 1) // 2
        if days_before_gregorian_year(mid) <= ordinal:
            low = mid
        else:
            high = mid - 1

    year = low
    remaining = ordinal - days_before_gregorian_year(year)
    month = 1
    while True:
        length = gregorian_month_length(year, month)
        if remaining < length:
            break
        remaining -= length
        month += 1

    return GregorianDate(year, month, remaining + 1)


def tredecadia_to_gregorian(value: TredecadiaDate) -> GregorianDate:
    start = gregorian_to_ordinal(value.year, 3, 21)

    if value.special == "ED":
        offset = 364
    elif value.special == "EQ":
        offset = 365 if tredecadia_is_leap(value.year) else 364
    else:
        assert value.month is not None and value.day is not None
        offset = (value.month - 1) * 28 + (value.day - 1)

    return ordinal_to_gregorian(start + offset)


def gregorian_to_tredecadia(value: GregorianDate) -> TredecadiaDate:
    ordinal = gregorian_to_ordinal(value.year, value.month, value.day)
    same_year_start = gregorian_to_ordinal(value.year, 3, 21)
    year = value.year if ordinal >= same_year_start else value.year - 1
    if year < 1:
        raise ValueError("Gregorian date precedes Tredecadia v1 conversion epoch")

    start = gregorian_to_ordinal(year, 3, 21)
    offset = ordinal - start
    leap = tredecadia_is_leap(year)

    if offset < 364:
        month, day0 = divmod(offset, 28)
        return TredecadiaDate(year, month + 1, day0 + 1)
    if offset == 364:
        return TredecadiaDate(year, special="ED" if leap else "EQ")
    if offset == 365 and leap:
        return TredecadiaDate(year, special="EQ")

    raise AssertionError("Gregorian date fell outside its derived Tredecadia year")
