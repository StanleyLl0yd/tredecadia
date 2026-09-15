# Tredecadia–Gregorian Conversion Standard

Status: **M1 proposal / Draft 0.1**

This document defines the proposed normative mapping between Tredecadia civil dates and the proleptic Gregorian calendar. It implements the fixed March-equinoctial anchor discussed in issue #2.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in their ordinary standards-document sense.

## 1. Scope and calendar model

Conversion is defined against the **proleptic Gregorian calendar** using the usual Gregorian leap rule for all positive Gregorian year numbers.

Tredecadia v1 conversion uses positive year numbers beginning with year `1`. Year `0` and negative/BCE year notation are outside the v1 core profile.

The conversion epoch is:

`Gregorian 0001-03-21 ↔ Tredecadia 0001-01-01`

A Tredecadia year number therefore matches the Gregorian year in which its regular month grid begins.

## 2. Fixed March-equinoctial anchor

For every Tredecadia year `Y >= 1`:

- Tredecadia `Y-01-01` corresponds to Gregorian `Y-03-21`;
- Tredecadia `Y-EQ` corresponds to Gregorian `(Y+1)-03-20`;
- if `Y` is a Tredecadia leap year, `Y-ED` corresponds to Gregorian `(Y+1)-03-19`.

`EQ` is a fixed civil **Equinox / New Year Day** associated with the March equinox. The standard does not claim that the astronomical equinox instant occurs on March 20 in every year, timezone, or location.

This fixed anchor is deliberate: conversion remains deterministic and requires no ephemeris, reference meridian, timezone, or astronomical model.

## 3. Gregorian leap predicate

A positive Gregorian year `G` is leap exactly when:

- `G` is divisible by `4`; and
- either `G` is not divisible by `100`, or `G` is divisible by `400`.

Equivalently:

`gregorian_leap(G) = G mod 4 = 0 and (G mod 100 != 0 or G mod 400 = 0)`

## 4. Tredecadia leap predicate

Tredecadia year `Y` is leap exactly when Gregorian year `Y + 1` is leap:

`tredecadia_leap(Y) = gregorian_leap(Y + 1)`

Thus each 400-year Tredecadia cycle contains 97 leap years, matching the Gregorian 400-year cycle but shifted by one year number.

Examples:

- Tredecadia `2023` is leap because Gregorian `2024` is leap;
- Tredecadia `2024` is ordinary because Gregorian `2025` is ordinary;
- Tredecadia `2099` is ordinary because Gregorian `2100` is not leap;
- Tredecadia `2399` is leap because Gregorian `2400` is leap.

## 5. Regular-date conversion

Let `Y-MM-DD` be a regular Tredecadia date, with `MM` in `01..13` and `DD` in `01..28`.

Its zero-based regular-day offset is:

`offset = (MM - 1) × 28 + (DD - 1)`

where `offset` is always in `0..363`.

The corresponding Gregorian date is obtained by adding `offset` civil days to Gregorian `Y-03-21`.

This mapping is one-to-one.

## 6. Intercalary-date conversion

For an ordinary Tredecadia year:

- offsets `0..363` are regular dates;
- offset `364` is `Y-EQ`.

For a leap Tredecadia year:

- offsets `0..363` are regular dates;
- offset `364` is `Y-ED`;
- offset `365` is `Y-EQ`.

`ED` and `EQ` are outside all regular months and have no Tredecadia weekday.

The Gregorian weekday of their mapped civil date MUST NOT be imported into the Tredecadia weekday cycle.

## 7. Gregorian-to-Tredecadia conversion

For a Gregorian date on or after `0001-03-21`:

1. Let its Gregorian year be `G`.
2. If the Gregorian date is on or after `G-03-21`, set Tredecadia year `Y = G`; otherwise set `Y = G - 1`.
3. Compute the zero-based civil-day offset from Gregorian `Y-03-21`.
4. If the offset is less than `364`, convert it to:
   - `MM = floor(offset / 28) + 1`;
   - `DD = (offset mod 28) + 1`.
5. If the offset is `364`:
   - return `Y-ED` when `Y` is leap;
   - otherwise return `Y-EQ`.
6. If the offset is `365`, `Y` MUST be leap and the result is `Y-EQ`.

No other offset can occur before the next Tredecadia year begins.

## 8. Round-trip requirement

For every valid date in the conversion domain:

- converting Tredecadia → Gregorian → Tredecadia MUST return the original Tredecadia date;
- converting Gregorian → Tredecadia → Gregorian MUST return the original Gregorian date.

Implementations SHOULD verify this property across Gregorian leap, non-leap, century, and 400-year boundaries.

## 9. Weekday semantics

Tredecadia weekdays are structural labels inside regular months; they are not inherited from Gregorian weekdays.

For every regular Tredecadia date, weekday is determined solely by its day number:

`weekday_index = (DD - 1) mod 7`

with index `0 = Monday` through `6 = Sunday`.

Therefore every `01` is Monday and every `28` is Sunday regardless of the Gregorian weekday of the mapped civil date.

`ED` and `EQ` have no Tredecadia weekday.

## 10. Conformance

A conforming converter MUST:

- use the fixed March 21 / March 20 civil anchor;
- use the Gregorian leap predicate above;
- derive Tredecadia leap status from Gregorian year `Y + 1`;
- preserve ED/EQ as intercalary values rather than fabricate month/day numbers;
- satisfy the round-trip requirement.

Astronomical-equinoctial calendars that move the year boundary according to an observed or calculated equinox are different calendar profiles and MUST NOT identify their dates as conforming Tredecadia v1 dates.
