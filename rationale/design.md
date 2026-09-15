# Design Rationale

This document is non-normative. It explains the design goals behind Tredecadia; normative requirements live under `specification/`.

## Goals

Tredecadia is designed around a small set of structural invariants:

- every regular month has the same length;
- every regular month has exactly four complete weeks;
- the same day number always has the same weekday;
- year-end adjustment does not disturb the weekly cycle;
- month names remain distinguishable in full and commonly shortened forms;
- the canonical naming system does not assign culture-specific semantic meanings to the months;
- civil conversion is deterministic and does not depend on location, timezone, or an astronomical ephemeris.

## Why 13 × 28

Thirteen 28-day months produce exactly 364 regular days, or 52 complete seven-day weeks. This makes every regular month structurally identical and leaves one intercalary day in an ordinary 365-day year, plus one additional intercalary day in a 366-day leap year.

Keeping the intercalary day or days outside the week preserves the invariant that every month starts on Monday and ends on Sunday.

## Civil year anchor

The M1 civil-calendar proposal anchors Tredecadia `Y-01-01` to Gregorian `Y-03-21`. The final Equinox / New Year Day then falls on Gregorian `(Y+1)-03-20`; in a leap Tredecadia year, Earth Day falls on `(Y+1)-03-19`.

This choice keeps the named Equinox Day near the March equinox while remaining purely arithmetic. It deliberately does **not** make the calendar depend on the observed or calculated astronomical equinox instant.

An astronomical rule was rejected for the civil core because it would require additional normative choices about time scale, reference meridian/timezone, astronomical model, precision, validity range, and future ephemeris updates. Those choices would make the same calendar date harder to reproduce independently.

A January-1 alignment would be simpler computationally, but would place Equinox Day at the end of December and weaken the intended meaning of the intercalary day name.

The fixed March anchor is therefore a compromise between semantic meaning and deterministic civil arithmetic.

## Leap alignment

The span from Gregorian March 21 in year `Y` to March 21 in year `Y+1` contains 366 days exactly when Gregorian `Y+1` is leap. Consequently Tredecadia year `Y` is leap when Gregorian `Y+1` is leap.

The apparent one-year shift is not an extra calendar rule; it follows directly from choosing March 21 as the start of the Tredecadia year.

## Separation of concerns

The project deliberately separates:

- calendar structure;
- month naming;
- date notation;
- localization;
- Gregorian conversion semantics.

This keeps the canonical month registry independent from conversion arithmetic while still allowing both layers to be verified together before v1.0.

## Non-goals

The civil core does not attempt to define:

- an observational or astronomical equinox calendar;
- year `0` or BCE notation in v1;
- religious or civil adoption policy;
- semantic themes for individual month names.
