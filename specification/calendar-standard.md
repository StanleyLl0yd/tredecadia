# Tredecadia Calendar Standard

Status: **M1 proposal / Draft 0.1**

This document defines the structural calendar model. Month naming is specified separately in [`month-naming-standard.md`](month-naming-standard.md); civil conversion is specified in [`conversion-standard.md`](conversion-standard.md).

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in their ordinary standards-document sense.

## 1. Year structure

A Tredecadia year contains 13 regular months. Each regular month contains exactly 28 days.

Therefore the regular month grid contains exactly 364 days:

`13 × 28 = 364`

An ordinary year contains one additional intercalary day after month 13 day 28. A leap year contains two intercalary days after month 13 day 28.

Intercalary days are outside all regular months and outside the seven-day week cycle.

## 2. Week structure

The regular week contains seven days in the order:

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

Every regular month contains exactly four complete weeks.

Within every month:

- day 01 is Monday;
- day 07 is Sunday;
- day 08 is Monday;
- day 14 is Sunday;
- day 15 is Monday;
- day 21 is Sunday;
- day 22 is Monday;
- day 28 is Sunday.

Because intercalary days are outside the week, month 01 day 01 is Monday every year.

## 3. Intercalary days

### 3.1 Equinox / New Year Day

The final intercalary day of every year is the Equinox / New Year Day (`EQ`). It follows month 13 day 28 and immediately precedes month 01 day 01 of the following year.

It has no weekday and no month/day number.

Under the civil conversion profile, Tredecadia `Y-EQ` maps to Gregorian `(Y+1)-03-20`. `Equinox` is a fixed civil designation associated with the March equinox; it does not assert that the astronomical equinox instant occurs on that civil date in every location or year.

### 3.2 Earth Day

A leap year adds Earth Day (`ED`) immediately before the Equinox / New Year Day.

It has no weekday and no month/day number.

The leap-year sequence is therefore:

`13-28 → Earth Day → Equinox / New Year Day → next year 01-01`

The ordinary-year sequence is:

`13-28 → Equinox / New Year Day → next year 01-01`

## 4. Month numbering

Regular months are numbered `01` through `13` in canonical order.

Month numbers are stable identifiers and MUST NOT depend on localization.

## 5. Day numbering

Days inside a regular month are numbered `01` through `28`.

No regular month may contain a day `00`, `29`, `30`, or `31`.

Intercalary days MUST NOT be represented as fabricated dates inside month 13 or month 01.

## 6. Leap-year determination

Tredecadia year `Y` is leap exactly when Gregorian year `Y + 1` is leap under the proleptic Gregorian rule.

A Gregorian year is leap when it is divisible by `4`, except a year divisible by `100` is not leap unless it is also divisible by `400`.

Thus:

`tredecadia_leap(Y) = gregorian_leap(Y + 1)`

A 400-year Tredecadia cycle contains 97 leap years.

The exact conversion algorithm and boundary behavior are defined in [`conversion-standard.md`](conversion-standard.md).

## 7. Year numbering and epoch

Tredecadia v1 uses positive year numbers beginning with year `1`. Year `0` and negative/BCE year notation are outside the v1 core profile.

The civil conversion epoch is:

`Gregorian 0001-03-21 ↔ Tredecadia 0001-01-01`

For every `Y >= 1`, Tredecadia `Y-01-01` maps to Gregorian `Y-03-21`, and Tredecadia `Y-EQ` maps to Gregorian `(Y+1)-03-20`.

The Tredecadia year number therefore matches the Gregorian year in which its 364-day regular month grid begins.

## 8. Invariants

A conforming implementation of the structural model MUST preserve all of the following:

- 13 regular months per year;
- 28 days per regular month;
- 364 regular in-month days;
- four complete seven-day weeks per month;
- Monday on every month day 01;
- Sunday on every month day 28;
- all intercalary days outside both months and weekdays;
- one `EQ` day every year;
- one additional `ED` day exactly in Tredecadia leap years.
