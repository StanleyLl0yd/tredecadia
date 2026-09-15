# Design Rationale

This document is non-normative. It explains the design goals behind Tredecadia; normative requirements live under `specification/`.

## Goals

Tredecadia is designed around a small set of structural invariants:

- every regular month has the same length;
- every regular month has exactly four complete weeks;
- the same day number always has the same weekday;
- year-end adjustment does not disturb the weekly cycle;
- month names remain distinguishable in full and commonly shortened forms;
- the canonical naming system does not assign culture-specific semantic meanings to the months.

## Why 13 × 28

Thirteen 28-day months produce exactly 364 regular days, or 52 complete seven-day weeks. This makes every regular month structurally identical and leaves one intercalary day in an ordinary 365-day year, plus one additional intercalary day in a 366-day leap year.

Keeping the intercalary day or days outside the week preserves the invariant that every month starts on Monday and ends on Sunday.

## Separation of concerns

The project deliberately separates:

- calendar structure;
- month naming;
- date notation;
- localization;
- conversion/epoch rules.

This allows the stable structural model and month registry to be reviewed independently from the still-open epoch and leap-year determination questions.

## Non-goals of Draft 0.1

Draft 0.1 does not yet attempt to define:

- a mandatory Gregorian conversion epoch;
- a final leap-year algorithm;
- religious or civil adoption policy;
- semantic themes for individual month names.
