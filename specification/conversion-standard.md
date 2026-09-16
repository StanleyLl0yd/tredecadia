# Tredecadia–Gregorian Conversion Standard

Status: **1.0.0-rc.2**

This document defines the Tredecadia civil conversion profile against the proleptic Gregorian calendar.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in their ordinary standards-document sense.

## 1. External Gregorian coordinate

Conversion uses the **proleptic Gregorian calendar with astronomical year numbering**.

Astronomical Gregorian year numbering is an integer coordinate:

- year `1` = conventional `1 CE`;
- year `0` = conventional `1 BCE`;
- year `-1` = conventional `2 BCE`;
- year `-9999` = conventional `10000 BCE`.

The Gregorian leap rule is extended arithmetically to every integer astronomical year.

Historical BCE/CE labels are explanatory only. Tredecadia itself does not use them.

## 2. Tredecadia Era origin

The Tredecadia Era (`TE`) has a real year `0`.

Its mathematical origin is:

`TE 00000-EQ`

The civil conversion profile maps that origin to:

`proleptic Gregorian astronomical year -9999, March 20`

or, in conventional historical terminology, the March-20 civil date in **10000 BCE**.

This is a conventional mathematical origin. It MUST NOT be interpreted as a claim that an astronomical equinox instant occurred on that civil date under some uniquely correct ancient time scale, nor as the beginning of any human, cultural, agricultural, historical, or geological era.

## 3. Year-coordinate relation

For any Tredecadia integer year `Y`, define:

`G = Y - 9999`

Then astronomical Gregorian year `G` contains both:

- `Y-EQ` on March 20;
- `Y-01-01` on March 21.

Equivalently:

`Y = G + 9999`

Examples:

| Astronomical Gregorian G | Conventional label | Tredecadia Y |
|---:|---|---:|
| -9999 | 10000 BCE | 0 |
| 0 | 1 BCE | 9999 |
| 1 | 1 CE | 10000 |
| 2026 | 2026 CE | 12025 |

## 4. Fixed March-equinoctial civil anchor

For every Tredecadia year `Y`:

- `Y-EQ` ↔ Gregorian astronomical `(Y - 9999)-03-20`;
- `Y-01-01` ↔ Gregorian astronomical `(Y - 9999)-03-21`;
- if `Y` is leap, `Y-ED` ↔ Gregorian astronomical `(Y - 9998)-03-19`;
- `(Y+1)-EQ` ↔ Gregorian astronomical `(Y - 9998)-03-20`.

`EQ` is therefore the first civil day associated with year `Y`.

`ED`, when present, is the final civil day associated with year `Y`.

The anchor is deliberately fixed and civil. Conversion requires no ephemeris, timezone, reference meridian, delta-T model, or observation of the actual March equinox instant.

## 5. Gregorian leap predicate

For any integer astronomical Gregorian year `G`:

`gregorian_leap(G) = divisible_by_4(G) and (not divisible_by_100(G) or divisible_by_400(G))`

Divisibility is mathematical divisibility and applies identically to positive, zero, and negative integer year numbers.

Therefore astronomical Gregorian year `0` is leap because it is divisible by `400`.

## 6. Tredecadia leap predicate

Tredecadia year `Y` is leap exactly when astronomical Gregorian year `Y - 9998` is leap:

`tredecadia_leap(Y) = gregorian_leap(Y - 9998)`

This follows from the March boundary: the possible extra civil day occurs in March of the following Gregorian astronomical year.

Every consecutive 400-year interval of Tredecadia contains 97 leap years.

## 7. Tredecadia-to-Gregorian conversion

### 7.1 Equinox / New Year Day

For `Y-EQ`:

1. compute `G = Y - 9999`;
2. return Gregorian astronomical `G-03-20`.

### 7.2 Regular dates

For a regular Tredecadia date `Y-MM-DD`, with `MM` in `01..13` and `DD` in `01..28`:

1. compute `G = Y - 9999`;
2. compute zero-based regular offset:

   `offset = (MM - 1) × 28 + (DD - 1)`

3. add `offset` civil days to Gregorian astronomical `G-03-21`.

The regular offset is always in `0..363`.

### 7.3 Earth Day

`Y-ED` is valid only when `tredecadia_leap(Y)` is true.

For valid `Y-ED`:

1. compute `G = Y - 9999`;
2. return Gregorian astronomical `(G + 1)-03-19`.

## 8. Gregorian-to-Tredecadia conversion

Let the input be a proleptic Gregorian date with astronomical year `G`.

### 8.1 Determine the Tredecadia year

If the Gregorian month/day is on or after March 20:

`Y = G + 9999`

Otherwise:

`Y = G + 9998`

Let `S` be Gregorian astronomical `(Y - 9999)-03-20`, the `EQ` that opens year `Y`.

Let `delta` be the number of civil days from `S` to the input date.

### 8.2 Interpret the offset

- if `delta = 0`, return `Y-EQ`;
- if `1 ≤ delta ≤ 364`, set `regular_offset = delta - 1`, then:
  - `MM = floor(regular_offset / 28) + 1`;
  - `DD = (regular_offset mod 28) + 1`;
- if `delta = 365`, `Y` MUST be leap and the result is `Y-ED`.

No other `delta` can occur before the next Tredecadia year opens.

## 9. Round-trip requirement

For every valid date in the integer conversion domain:

- Tredecadia → Gregorian → Tredecadia MUST return the original Tredecadia date;
- Gregorian → Tredecadia → Gregorian MUST return the original Gregorian date.

A conforming implementation SHOULD test this across:

- negative Tredecadia years;
- Tredecadia year `0`;
- astronomical Gregorian year `0` (1 BCE);
- the 1 BCE / 1 CE boundary;
- Gregorian century exceptions;
- Gregorian 400-year leap restorations;
- expanded year numbers.

## 10. Weekday semantics

Tredecadia weekdays are structural labels inside regular months and are not inherited from Gregorian weekdays.

For every regular Tredecadia date:

`weekday_index = (DD - 1) mod 7`

with index `0 = W1 / Mene` through `6 = W7 / Toze`.

Therefore every regular day `01` is `W1` / Mene and every regular day `28` is `W7` / Toze. The intermediate indexes are `W2` Noko, `W3` Kese, `W4` Zoyo, `W5` Sote, and `W6` Yemo.

`EQ` and `ED` have no Tredecadia weekday.

## 11. Conformance

A conforming Tredecadia civil converter MUST:

- use the Tredecadia Era year coordinate with year `0`;
- use the fixed March-20 `EQ` / March-21 regular-start anchor;
- use astronomical Gregorian year numbering for external arithmetic;
- use `Y = G + 9999` for the year-coordinate relation;
- use `tredecadia_leap(Y) = gregorian_leap(Y - 9998)`;
- preserve `EQ` and `ED` as intercalary values rather than fabricate regular month/day numbers;
- preserve the structural weekday index mapping `0..6 = W1..W7` for regular dates;
- satisfy the round-trip requirement.

A calendar whose year boundary moves according to a calculated or observed astronomical equinox is a different calendar profile and MUST NOT identify those dates as conforming Tredecadia civil dates.
