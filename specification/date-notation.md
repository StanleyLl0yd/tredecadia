# Tredecadia Date Notation

Status: **Draft 0.2**

## 1. Era

The canonical era is the **Tredecadia Era**, abbreviated `TE`.

Tredecadia year numbering is one integer axis and includes year `0`. BCE/CE notation is not used inside Tredecadia.

## 2. Canonical year field

The canonical year field contains at least five decimal digits of magnitude.

For non-negative years, no sign is written:

- year `0` → `00000`;
- year `1` → `00001`;
- year `9999` → `09999`;
- year `12025` → `12025`;
- year `100000` → `100000`.

For negative years, a leading ASCII minus sign is followed by at least five digits of magnitude:

- year `-1` → `-00001`;
- year `-10000` → `-10000`;
- year `-100000` → `-100000`.

A leading plus sign is not canonical.

## 3. Regular dates

A regular in-month date uses:

`YEAR-MM-DD`

where:

- `YEAR` follows the canonical year-field rule above;
- `MM` is `01` through `13`;
- `DD` is `01` through `28`.

Examples:

- `00000-01-01`;
- `09999-13-28`;
- `10000-01-01`;
- `12025-07-11`;
- `-00001-01-01`.

The grammar is deliberately ISO-like, but Tredecadia date notation does not claim ISO 8601 compatibility.

## 4. Intercalary dates

Intercalary days use symbolic forms:

- `YEAR-EQ` — Equinox / New Year Day, which **opens** `YEAR`;
- `YEAR-ED` — Earth Day, present only in a leap year and **closing** `YEAR`.

Examples:

- `00000-EQ`;
- `09998-ED`;
- `12025-EQ`;
- `-00001-EQ`.

`Y-EQ` is immediately followed by `Y-01-01`.

In a leap year, `Y-13-28` is followed by `Y-ED`, then `(Y+1)-EQ`.

In an ordinary year, `Y-13-28` is followed directly by `(Y+1)-EQ`.

Implementations MUST NOT encode an intercalary day as month `13` day `29`, month `01` day `00`, or any other fabricated regular date.

## 5. Human-readable dates

A canonical month name may replace the numeric month:

`11 Muyasanumi 12025 TE`

The Short-6 form may be used where context is clear:

`11 Muyasa 12025 TE`

The `TE` era suffix MAY be omitted when the Tredecadia context is unambiguous.

Short-4 is intended for compact interfaces and should not be used when ambiguity with ordinary prose is likely.

## 6. Gregorian conversion

The normative civil mapping is defined by [`conversion-standard.md`](conversion-standard.md).

For Tredecadia year `Y`:

- `Y-EQ` ↔ astronomical Gregorian `(Y - 9999)-03-20`;
- `Y-01-01` ↔ astronomical Gregorian `(Y - 9999)-03-21`;
- when `Y` is leap, `Y-ED` ↔ astronomical Gregorian `(Y - 9998)-03-19`.

The corresponding Gregorian weekday does not determine the Tredecadia weekday. Regular Tredecadia weekdays follow the fixed 28-day month structure; `EQ` and `ED` have no Tredecadia weekday.
