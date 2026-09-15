# SPDX-License-Identifier: MIT
"""Executable calendar arithmetic for validating the Tredecadia civil profile.

This module is a test oracle, not yet a stable public API.
"""

from __future__ import annotations

from dataclasses import dataclass

COMMON_MONTH_LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
TREDECADIA_GREGORIAN_YEAR_OFFSET = 9999

def format_year(year: int) -> str:
    return f"-{abs(year):05d}" if year < 0 else f"{year:05d}"

def format_astronomical_year(year: int) -> str:
    return f"-{abs(year):05d}" if year < 0 else f"{year:05d}"

@dataclass(frozen=True)
class GregorianDate:
    year: int
    month: int
    day: int
    def __post_init__(self) -> None:
        validate_gregorian(self.year, self.month, self.day)
    def __str__(self) -> str:
        return f"{format_astronomical_year(self.year)}-{self.month:02d}-{self.day:02d}"

@dataclass(frozen=True)
class TredecadiaDate:
    year: int
    month: int | None = None
    day: int | None = None
    special: str | None = None
    def __post_init__(self) -> None:
        if self.special is not None:
            if self.special not in {"ED", "EQ"}: raise ValueError("unknown intercalary code")
            if self.month is not None or self.day is not None: raise ValueError("intercalary dates have no month/day")
            if self.special == "ED" and not tredecadia_is_leap(self.year): raise ValueError("Earth Day exists only in leap years")
        else:
            if self.month is None or self.day is None: raise ValueError("regular dates require month and day")
            if not 1 <= self.month <= 13: raise ValueError("month must be in 1..13")
            if not 1 <= self.day <= 28: raise ValueError("day must be in 1..28")
    @property
    def canonical(self) -> str:
        y = format_year(self.year)
        if self.special is not None: return f"{y}-{self.special}"
        assert self.month is not None and self.day is not None
        return f"{y}-{self.month:02d}-{self.day:02d}"

def gregorian_is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def tredecadia_start_gregorian_year(year: int) -> int:
    return year - TREDECADIA_GREGORIAN_YEAR_OFFSET

def tredecadia_is_leap(year: int) -> bool:
    return gregorian_is_leap(year - 9998)

def gregorian_month_length(year: int, month: int) -> int:
    if not 1 <= month <= 12: raise ValueError("Gregorian month must be in 1..12")
    if month == 2 and gregorian_is_leap(year): return 29
    return COMMON_MONTH_LENGTHS[month - 1]

def validate_gregorian(year: int, month: int, day: int) -> None:
    if not 1 <= day <= gregorian_month_length(year, month): raise ValueError("invalid Gregorian day")

def days_before_gregorian_year(year: int) -> int:
    y = year - 1
    return 365 * y + y // 4 - y // 100 + y // 400

def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    validate_gregorian(year, month, day)
    result = days_before_gregorian_year(year)
    for m in range(1, month): result += gregorian_month_length(year, m)
    return result + day - 1

def ordinal_to_gregorian(ordinal: int) -> GregorianDate:
    cycle = ordinal // 146097
    low, high = cycle * 400 + 1, cycle * 400 + 400
    while low < high:
        mid = (low + high + 1) // 2
        if days_before_gregorian_year(mid) <= ordinal: low = mid
        else: high = mid - 1
    year = low
    remaining = ordinal - days_before_gregorian_year(year)
    month = 1
    while True:
        length = gregorian_month_length(year, month)
        if remaining < length: break
        remaining -= length
        month += 1
    return GregorianDate(year, month, remaining + 1)

def tredecadia_to_gregorian(value: TredecadiaDate) -> GregorianDate:
    g = tredecadia_start_gregorian_year(value.year)
    if value.special == "EQ": return GregorianDate(g, 3, 20)
    if value.special == "ED": return GregorianDate(g + 1, 3, 19)
    assert value.month is not None and value.day is not None
    offset = (value.month - 1) * 28 + (value.day - 1)
    return ordinal_to_gregorian(gregorian_to_ordinal(g, 3, 21) + offset)

def gregorian_to_tredecadia(value: GregorianDate) -> TredecadiaDate:
    year = value.year + 9999 if (value.month, value.day) >= (3, 20) else value.year + 9998
    g = tredecadia_start_gregorian_year(year)
    delta = gregorian_to_ordinal(value.year, value.month, value.day) - gregorian_to_ordinal(g, 3, 20)
    if delta == 0: return TredecadiaDate(year, special="EQ")
    if 1 <= delta <= 364:
        month, day0 = divmod(delta - 1, 28)
        return TredecadiaDate(year, month + 1, day0 + 1)
    if delta == 365 and tredecadia_is_leap(year): return TredecadiaDate(year, special="ED")
    raise AssertionError("Gregorian date fell outside its derived Tredecadia year")
