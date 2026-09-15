# Tredecadia Date Notation

Status: **M1 proposal / Draft 0.1**

## Regular dates

A regular in-month date uses the numeric form:

`YYYY-MM-DD`

where:

- `YYYY` is the positive Tredecadia year number, written with at least four decimal digits;
- `MM` is `01` through `13`;
- `DD` is `01` through `28`.

Years below `1000` are zero-padded to four digits. Years above `9999` use the required additional decimal digits without a leading `+` in the Tredecadia core notation.

Examples:

- `0001-01-01`;
- `2084-07-14`;
- `10000-01-01`.

The numeric grammar is deliberately ISO-like, but Tredecadia date notation does not claim ISO 8601 compatibility.

## Human-readable dates

A canonical month name may replace the numeric month:

`14 Muyasanumi 2084`

The Short-6 form may be used where context is clear:

`14 Muyasa 2084`

Short-4 is intended for compact interfaces and should not be used when ambiguity with ordinary prose is likely.

## Intercalary dates

Intercalary days are not regular month/day values. Their canonical machine forms are:

- `YYYY-ED` — Earth Day, present only in a Tredecadia leap year;
- `YYYY-EQ` — Equinox / New Year Day, present every Tredecadia year.

`YYYY` follows the same positive, at-least-four-digit rule as regular dates.

Examples:

- `2023-ED`;
- `2023-EQ`;
- `2024-EQ`.

`2024-ED` is invalid because Tredecadia `2024` is not a leap year under the v1 civil conversion rule.

Implementations MUST NOT encode an intercalary day as month `13` day `29`, month `01` day `00`, or any other fabricated regular date.

## Gregorian conversion

The normative civil mapping is defined by [`conversion-standard.md`](conversion-standard.md).

In particular:

- Tredecadia `Y-01-01` ↔ Gregorian `Y-03-21`;
- Tredecadia `Y-EQ` ↔ Gregorian `(Y+1)-03-20`;
- when Tredecadia `Y` is leap, `Y-ED` ↔ Gregorian `(Y+1)-03-19`.

The corresponding Gregorian date has no effect on the Tredecadia weekday label. Regular Tredecadia weekdays follow the fixed 28-day month structure; `ED` and `EQ` have no Tredecadia weekday.
