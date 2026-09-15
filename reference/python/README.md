# Tredecadia Python reference implementation

This directory contains a small dependency-free reference implementation of the Tredecadia civil calendar.

It is **not** the normative definition of the calendar. Normative semantics live in [`../../specification/`](../../specification/) and machine-readable canonical data lives in [`../../registry/`](../../registry/). The purpose of this implementation is to make those rules executable and easy to compare with independent implementations.

## Requirements

Python 3.11 or newer. No third-party runtime packages are required.

## Gregorian → Tredecadia

```console
$ python reference/python/tredecadia.py from-gregorian 2026-09-15
12025-07-11
```

Astronomical Gregorian year numbering is accepted, including year `0` and negative years:

```console
$ python reference/python/tredecadia.py from-gregorian -9999-03-20
00000-EQ

$ python reference/python/tredecadia.py from-gregorian 0-03-20
09999-EQ
```

## Tredecadia → Gregorian

```console
$ python reference/python/tredecadia.py to-gregorian 12025-07-11
2026-09-15

$ python reference/python/tredecadia.py to-gregorian 00000-EQ
-9999-03-20
```

## Python API

```python
from tredecadia import (
    GregorianDate,
    TredecadiaDate,
    from_gregorian,
    parse_tredecadia,
    to_gregorian,
)

te = from_gregorian(GregorianDate(2026, 9, 15))
assert te.canonical == "12025-07-11"

civil = to_gregorian(parse_tredecadia("00000-EQ"))
assert (civil.year, civil.month, civil.day) == (-9999, 3, 20)
```

The main public functions are:

- `gregorian_is_leap(year)`;
- `tredecadia_is_leap(year)`;
- `format_year(year)`;
- `parse_tredecadia(text)`;
- `parse_gregorian(text)`;
- `to_gregorian(date)`;
- `from_gregorian(date)`.

`TredecadiaDate` represents regular month dates and the two intercalary forms `EQ` and `ED`. Invalid Earth Days are rejected at construction time.

## Canonical parsing

`parse_tredecadia()` is intentionally strict. It rejects, among other things:

- fewer than five year digits (`0001-EQ`);
- a leading plus sign (`+00001-EQ`);
- negative zero (`-00000-EQ`);
- redundant leading zeroes (`000001-EQ`);
- month `00` or `14`;
- regular day `00` or `29`;
- `ED` in an ordinary Tredecadia year.

## Verification

`tests/validate_reference.py` compares this implementation against:

1. the published conversion vectors;
2. the independent calendar-arithmetic test oracle in `tests/calendar_math.py`;
3. round-trip properties over large ranges crossing year `0` and the Gregorian astronomical `0` boundary.

The implementation is licensed under the MIT License.
