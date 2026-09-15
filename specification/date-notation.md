# Tredecadia Date Notation

Status: **Draft 0.1**

## Regular dates

A regular in-month date uses the numeric form:

`YYYY-MM-DD`

where:

- `YYYY` is the Tredecadia year number;
- `MM` is `01` through `13`;
- `DD` is `01` through `28`.

Example: `2084-07-14`.

The numeric grammar is deliberately ISO-like, but this draft does not claim ISO 8601 compatibility.

## Human-readable dates

A canonical month name may replace the numeric month:

`14 Muyasanumi 2084`

The Short-6 form may be used where context is clear:

`14 Muyasa 2084`

Short-4 is intended for compact interfaces and should not be used when ambiguity with ordinary prose is likely.

## Intercalary dates

Intercalary days are not regular month/day values. Draft 0.1 reserves these symbolic forms:

- `YYYY-ED` — Earth Day, present only in a leap year;
- `YYYY-EQ` — Equinox / New Year Day, present every year.

These symbolic forms are provisional until the machine date model is finalized.

Implementations must not encode an intercalary day as month `13` day `29` or as month `01` day `00`.

## Open item

A stable release still needs to define the epoch, year-number conversion semantics, and leap-year rule before Gregorian/Tredecadia conversion can be normative.
