# Tredecadia Calendar Standard

Status: **1.0.0-rc.2**

This document defines the structural calendar model and the Tredecadia Era. Month naming is specified separately in [`month-naming-standard.md`](month-naming-standard.md); civil conversion is specified in [`conversion-standard.md`](conversion-standard.md).

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in their ordinary standards-document sense.

## 1. Year structure

A Tredecadia year contains:

1. one Equinox / New Year Day (`EQ`) at the start of the year;
2. 13 regular months of exactly 28 days each;
3. in leap years only, one Earth Day (`ED`) after month 13 day 28.

The regular month grid therefore contains exactly 364 days:

`13 × 28 = 364`

An ordinary Tredecadia year contains 365 civil days in total. A leap Tredecadia year contains 366 civil days in total.

Both `EQ` and `ED` are outside all regular months and outside the seven-day week cycle.

Ordinary-year sequence:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Leap-year sequence:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## 2. Week structure

The regular week contains seven canonical weekday positions. Their machine identifiers and canonical human-readable names are:

| Position | ID | Canonical name | Syllables | Citation IPA |
|---:|---|---|---|---|
| 1 | `W1` | **Mene** | `ME NE` | `/ˈme.ne/` |
| 2 | `W2` | **Noko** | `NO KO` | `/ˈno.ko/` |
| 3 | `W3` | **Kese** | `KE SE` | `/ˈke.se/` |
| 4 | `W4` | **Zoyo** | `ZO YO` | `/ˈzo.jo/` |
| 5 | `W5` | **Sote** | `SO TE` | `/ˈso.te/` |
| 6 | `W6` | **Yemo** | `YE MO` | `/ˈje.mo/` |
| 7 | `W7` | **Toze** | `TO ZE` | `/ˈto.ze/` |

`W1` through `W7` are stable machine identifiers. The canonical names are ASCII Latin identifiers, not translations of Gregorian weekday names. The ordered two-syllable segmental identity of each canonical weekday name is compatibility-critical; stress is not identity-critical, and the reference pronunciation uses weak initial prominence.

Every regular month contains exactly four complete weeks.

Within every month:

- day 01 is `W1` / Mene;
- day 07 is `W7` / Toze;
- day 08 is `W1` / Mene;
- day 14 is `W7` / Toze;
- day 15 is `W1` / Mene;
- day 21 is `W7` / Toze;
- day 22 is `W1` / Mene;
- day 28 is `W7` / Toze.

Because intercalary days are outside the week, month 01 day 01 is `W1` / Mene every year.

Localization MAY provide reviewed display aliases for canonical weekdays, but MUST preserve the underlying `W1..W7` identities, order, and reverse mapping to the canonical names.

## 3. Intercalary days

### 3.1 Equinox / New Year Day (`EQ`)

`Y-EQ` is the first civil day associated with Tredecadia year `Y`.

It immediately precedes `Y-01-01`.

It has no weekday and no month/day number.

Under the Tredecadia civil conversion profile, `Y-EQ` maps to March 20 of astronomical Gregorian year `Y - 9999`.

`Equinox` is a conventional civil designation associated with the **March equinox**. The standard does not assert that the astronomical equinox instant occurs on that civil date in every year, timezone, location, or astronomical time scale.

### 3.2 Earth Day (`ED`)

A leap Tredecadia year adds `Y-ED` immediately after `Y-13-28` and immediately before `(Y+1)-EQ`.

It is therefore the final civil day associated with leap year `Y`.

It has no weekday and no month/day number.

Under the Tredecadia civil conversion profile, `Y-ED` maps to March 19 of astronomical Gregorian year `Y - 9998`.

## 4. Month numbering

Regular months are numbered `01` through `13` in canonical order.

Month numbers are stable identifiers and MUST NOT depend on localization.

## 5. Day numbering

Days inside a regular month are numbered `01` through `28`.

No regular month may contain a day `00`, `29`, `30`, or `31`.

Intercalary days MUST NOT be represented as fabricated dates inside month 13 or month 01.

## 6. Tredecadia Era

The canonical era is the **Tredecadia Era**, abbreviated `TE`.

Tredecadia years form one continuous integer coordinate:

`…, -2, -1, 0, 1, 2, …`

Year `0` exists. Tredecadia does not require a BCE/CE-style change of era or reversal of counting direction.

The mathematical era origin is:

`TE 00000-EQ`

For civil conversion this is identified with proleptic Gregorian astronomical date:

`year -9999, March 20`

Astronomical Gregorian year `-9999` corresponds to the conventional historical label **10000 BCE**.

The era origin MUST NOT be interpreted as a claim about the beginning of humanity, civilization, agriculture, the Holocene, or any other historical or geological process. It is solely the mathematical origin chosen for the Tredecadia year coordinate.

Years before the origin use negative Tredecadia year numbers and remain on the same coordinate.

## 7. Leap-year determination

The civil profile uses the proleptic Gregorian leap pattern with astronomical Gregorian year numbering.

For Tredecadia year `Y`, define:

`G = Y - 9999`

where `G` is the astronomical Gregorian year containing `Y-EQ` and `Y-01-01`.

Tredecadia year `Y` is leap exactly when astronomical Gregorian year `G + 1`, equivalently `Y - 9998`, is leap:

`tredecadia_leap(Y) = gregorian_leap(Y - 9998)`

The Gregorian leap predicate is true when the year number is divisible by `4`, except that a year divisible by `100` is not leap unless it is also divisible by `400`. The same arithmetic predicate applies to zero and negative astronomical Gregorian year numbers.

Every 400 consecutive Tredecadia years therefore contain exactly 97 leap years.

Examples:

- `TE 09998` is leap because astronomical Gregorian year `0` is leap;
- `TE 09999` is ordinary because astronomical Gregorian year `1` is ordinary;
- `TE 12022` is leap because Gregorian `2024` is leap;
- `TE 12098` is ordinary because Gregorian `2100` is ordinary;
- `TE 12398` is leap because Gregorian `2400` is leap.

## 8. Invariants

A conforming implementation of the structural model MUST preserve all of the following:

- one `EQ` opening every Tredecadia year;
- 13 regular months per year;
- 28 days per regular month;
- 364 regular in-month days;
- four complete seven-day weeks per month;
- `W1` / Mene on every month day 01;
- `W7` / Toze on every month day 28;
- canonical weekday order `W1..W7` = Mene, Noko, Kese, Zoyo, Sote, Yemo, Toze;
- all intercalary days outside both months and weekdays;
- one additional `ED` exactly in Tredecadia leap years;
- a continuous integer year coordinate with year `0`.
