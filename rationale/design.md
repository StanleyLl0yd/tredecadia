# Design Rationale

This document is non-normative. It explains the design goals behind Tredecadia; normative requirements live under `specification/`.

## Goals

Tredecadia is designed around a small set of structural invariants:

- every regular month has the same length;
- every regular month has exactly four complete weeks;
- the same day number always has the same weekday;
- intercalary adjustment does not disturb the weekly cycle;
- month names remain distinguishable in full and commonly shortened forms;
- the canonical naming system does not assign culture-specific semantic meanings to the months;
- year numbering is one continuous mathematical coordinate;
- civil conversion is deterministic and does not depend on location, timezone, or an astronomical ephemeris.

## Why 13 × 28

Thirteen 28-day months produce exactly 364 regular days, or 52 complete seven-day weeks. This makes every regular month structurally identical.

`EQ` supplies the 365th civil day and opens every year. A leap year adds `ED` as the 366th civil day at the end of the year.

Keeping both intercalary days outside the week preserves the invariant that every regular month starts on Monday and ends on Sunday.

## Why EQ opens the year

Calling the intercalary day both **Equinox Day** and **New Year Day** is semantically clearest when it belongs to the year being opened, not the year being closed.

The boundary is therefore:

`… → Y-13-28 → [Y-ED] → (Y+1)-EQ → (Y+1)-01-01`

This also makes the mathematical era origin expressible directly as `00000-EQ`.

## Why a mathematical epoch near 10000 BCE

Tredecadia deliberately does not inherit a religious, dynastic, national, or political era origin.

The chosen mathematical origin is the conventional March-equinoctial civil boundary associated with **10000 BCE**:

`TE 00000-EQ ↔ proleptic Gregorian astronomical -9999-03-20`

This choice has two practical properties:

1. almost all conventionally documented human history lies on the positive side of the Tredecadia year axis;
2. the calendar has a real year `0` and therefore needs no discontinuity such as `1 BCE → 1 CE`.

The number is a coordinate choice, not a historical assertion. Tredecadia does **not** claim that year 0 marks the beginning of humanity, civilization, agriculture, settlement, the Holocene, or any other process.

For the same reason the project does not label the era “Human Era” or attach semantic meaning to the elapsed year count.

## Why astronomical Gregorian year numbering is used for conversion

Historical BCE/CE notation has no year `0`, which makes arithmetic across the era boundary awkward.

The conversion layer instead uses standard astronomical integer year numbering:

- astronomical `1` = 1 CE;
- astronomical `0` = 1 BCE;
- astronomical `-1` = 2 BCE.

The relation then becomes a simple affine coordinate transform:

`Tredecadia year = astronomical Gregorian year + 9999`

This convention is used only for conversion arithmetic. Tredecadia's own year coordinate remains independent.

## Why the March anchor is fixed rather than observational

The civil profile anchors `EQ` to March 20 and regular `01-01` to March 21 in the corresponding proleptic Gregorian astronomical year.

This keeps the named Equinox Day associated with the March equinox while remaining purely arithmetic.

An observational or calculated equinox rule would require additional normative choices about time scale, reference meridian or timezone, astronomical model, precision, validity range, and future ephemeris updates. At the remote era origin those issues are especially pronounced.

Tredecadia therefore makes no claim that its conventional March-20 civil boundary is the historically or astronomically exact equinox date in 10000 BCE or in every other year.

## Leap alignment

For Tredecadia year `Y`, the corresponding Gregorian astronomical start year is:

`G = Y - 9999`

The interval reaches the next March boundary through February of `G + 1`. Therefore the possible extra day is determined by whether `G + 1`, equivalently `Y - 9998`, is Gregorian-leap.

The offset in the leap formula is a consequence of the March boundary, not an independent design choice.

## Separation of concerns

The project deliberately separates:

- calendar structure and era;
- month naming;
- date notation;
- localization;
- Gregorian conversion semantics.

This keeps the canonical month registry independent from era/conversion arithmetic while allowing both layers to be verified together before v1.0.

## Non-goals

The civil core does not attempt to define:

- an observational or astronomical equinox calendar;
- a claim about the beginning of human history;
- religious or civil adoption policy;
- semantic themes for individual month names.
