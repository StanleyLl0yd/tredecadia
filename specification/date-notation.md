# Tredecadia Date Notation

Status: **1.0.0-rc.2**

## 1. Era

The canonical era is the **Tredecadia Era**, abbreviated `TE`.

Tredecadia year numbering is one integer axis and includes year `0`. BCE/CE notation is not used inside Tredecadia.

## 2. Canonical year field

The canonical year field contains at least five **ASCII decimal digits** of magnitude.

For non-negative years, no sign is written:

- year `0` → `00000`;
- year `1` → `00001`;
- year `9999` → `09999`;
- year `12025` → `12025`;
- year `100000` → `100000`.

For negative years, a leading ASCII hyphen-minus `-` is followed by at least five ASCII digits of magnitude:

- year `-1` → `-00001`;
- year `-10000` → `-10000`;
- year `-100000` → `-100000`.

A leading plus sign is not canonical. Negative zero (`-00000`) is not canonical. Leading zeroes are used only to reach the five-digit minimum; additional redundant leading zeroes are not canonical. Thus year `1` is `00001`, not `000001`.

Canonical machine syntax MUST use ASCII digits `0` through `9` and ASCII `-`. A typographic Unicode minus sign, localized numeral set, grouping separator, or surrounding whitespace is not canonical machine input.

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

`EQ` and `ED` are canonical machine tokens and are case-sensitive.

`Y-EQ` is immediately followed by `Y-01-01`.

In a leap year, `Y-13-28` is followed by `Y-ED`, then `(Y+1)-EQ`.

In an ordinary year, `Y-13-28` is followed directly by `(Y+1)-EQ`.

Implementations MUST NOT encode an intercalary day as month `13` day `29`, month `01` day `00`, or any other fabricated regular date.

## 5. Human-readable dates

A canonical month name may replace the numeric month:

`11 Muyasanumi 12025 TE`

The Short-6 form is the safer written/display abbreviation where more redundancy is useful:

`11 Muyasa 12025 TE`

Short-4 is the preferred conversational compact form when context already makes clear that a Tredecadia month is being named:

`11 Muya 12025 TE`

The `TE` era suffix MAY be omitted when the Tredecadia context is unambiguous.

In prose where a four-letter month form could be confused with an unrelated ordinary word or name, Short-6 or the full canonical month name SHOULD be preferred.

### 5.1 Human year display

Human-facing presentation MAY suppress canonical leading zeroes. Thus canonical year `00001` may be shown as `1 TE`, while canonical `00000` may be shown as `0 TE`.

For a negative year, human-facing typography MAY use Unicode MINUS SIGN `−` (U+2212), for example `−1 TE`, even though canonical machine syntax remains `-00001`.

Human-friendly display forms are presentation only. They MUST NOT be accepted as alternate canonical identifiers unless an application explicitly performs normalization into the canonical form.

Tredecadia negative years remain Tredecadia Era coordinates. They MUST NOT be relabeled BCE or CE.

### 5.2 Accessible semantic labels

Accessible interfaces SHOULD expose a date as semantic components instead of relying only on punctuation or abbreviations.

For a regular date, the accessible representation SHOULD make available:

- Tredecadia Era identity;
- the signed integer year value;
- canonical month identity or localized month alias;
- day number;
- structural weekday identity (`W1..W7`) when the interface exposes a weekday.

For an intercalary date, `EQ` and `ED` SHOULD be exposed by their names rather than only by the letter tokens:

- `EQ` → **Equinox / New Year Day**;
- `ED` → **Earth Day**.

Examples of semantic readings in English are:

- `12025-07-11` → “Tredecadia Era, year 12025, month Muyasanumi, day 11, weekday Zoyo”;
- `00000-EQ` → “Tredecadia Era, year 0, Equinox / New Year Day”;
- `-00001-01-01` → “Tredecadia Era, year minus 1, month Masanumika, day 1, weekday Mene”.

The exact spoken wording MAY be localized. The sign, year value, month/intercalary identity, day value, and any exposed weekday identity MUST remain recoverable from the accessible representation.

### 5.3 Forgiving input layers

Applications MAY provide a forgiving human-input layer that accepts typographic minus signs, localized digits, omitted padding, or surrounding whitespace. Such input is outside canonical syntax.

Before storage, comparison, interchange, or signing, a forgiving input layer SHOULD normalize to one canonical Tredecadia representation and SHOULD surface ambiguity rather than silently guessing.

## 6. Gregorian conversion

The normative civil mapping is defined by [`conversion-standard.md`](conversion-standard.md).

For Tredecadia year `Y`:

- `Y-EQ` ↔ astronomical Gregorian `(Y - 9999)-03-20`;
- `Y-01-01` ↔ astronomical Gregorian `(Y - 9999)-03-21`;
- when `Y` is leap, `Y-ED` ↔ astronomical Gregorian `(Y - 9998)-03-19`.

The corresponding Gregorian weekday does not determine the Tredecadia weekday. Regular Tredecadia weekdays follow the fixed `W1..W7` 28-day month structure; `EQ` and `ED` have no Tredecadia weekday.
