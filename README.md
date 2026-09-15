# Tredecadia

Tredecadia is an open 13 × 28 perennial calendar standard with equal months, stable weekdays, a continuous mathematical year coordinate, and internationally neutral month names.

> **Status:** pre-1.0, Draft 0.2. The Tredecadia Era and civil conversion model are defined, but the project is not yet a frozen v1.0 standard.

## Core model

- 13 months × 28 days = 364 regular in-month days.
- Every month has exactly four complete weeks.
- Day `01` of every month is Monday; day `28` is Sunday.
- **Equinox / New Year Day (`EQ`) opens each Tredecadia year** and is outside the month/week cycle.
- A leap year has one additional intercalary **Earth Day (`ED`)** after month 13 day 28 and immediately before the next year's `EQ`.
- The canonical month names are designed for international neutrality and high mutual distinguishability.

Ordinary-year boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Leap-year boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia uses the **Tredecadia Era (TE)**, a single integer year coordinate with a real year `0`.

The mathematical origin is:

`TE 00000-EQ ↔ proleptic Gregorian astronomical year -9999, March 20`

Astronomical Gregorian year `-9999` is conventionally described as **10000 BCE**. The epoch is not claimed to be the beginning of humanity, civilization, agriculture, the Holocene, or any historical process. It is only the mathematical origin of the Tredecadia year coordinate.

Tredecadia does not use BCE/CE internally:

```text
…  -2  -1   0   1   2  …  9999  10000  …  12025 …
```

For the civil conversion profile, if `G` is the astronomical Gregorian year containing a Tredecadia year's `EQ` and `01-01`:

`TE year = G + 9999`

Examples:

| External year | Astronomical G | Tredecadia year |
|---|---:|---:|
| 10000 BCE | -9999 | 0 |
| 1 BCE | 0 | 9999 |
| 1 CE | 1 | 10000 |
| 2026 CE | 2026 | 12025 |

The March-20 anchor is a deterministic **civil convention associated with the March equinox**. It is not a claim that the astronomical equinox instant occurs on March 20 in every year, location, or time scale.

## Specification

- [`specification/calendar-standard.md`](specification/calendar-standard.md) — calendar structure and Tredecadia Era.
- [`specification/conversion-standard.md`](specification/conversion-standard.md) — proleptic-Gregorian civil conversion.
- [`specification/month-naming-standard.md`](specification/month-naming-standard.md) — canonical month names, pronunciation, and abbreviations.
- [`specification/date-notation.md`](specification/date-notation.md) — canonical date representation.
- [`specification/localization.md`](specification/localization.md) — localization rules.

Machine-readable data lives in [`registry/`](registry/); verification vectors and executable checks live in [`tests/`](tests/). Design rationale is intentionally separated from normative text in [`rationale/`](rationale/).

## Canonical months

| # | Full name | Short-6 | Short-4 |
|---:|---|---|---|
| 01 | Masanumika | Masanu | Masa |
| 02 | Tasuzunumu | Tasuzu | Tasu |
| 03 | Nazumasanu | Nazuma | Nazu |
| 04 | Mikasumani | Mikasu | Mika |
| 05 | Yanimuzunu | Yanimu | Yani |
| 06 | Zumitanasu | Zumita | Zumi |
| 07 | Muyasanumi | Muyasa | Muya |
| 08 | Sunizusaka | Sunizu | Suni |
| 09 | Numanamuta | Numana | Numa |
| 10 | Kazunusuya | Kazunu | Kazu |
| 11 | Yanazumasa | Yanazu | Yana |
| 12 | Sanumikazu | Sanumi | Sanu |
| 13 | Nimutazuna | Nimuta | Nimu |

## Example

Proleptic Gregorian `2026-09-15` maps to:

`TE 12025-07-11`

The Tredecadia weekday is determined by the regular-month day number, not by the weekday label of the corresponding Gregorian civil date.

## Python reference implementation

A dependency-free reference converter is available at [`reference/python/tredecadia.py`](reference/python/tredecadia.py). It is executable documentation and a conformance aid; the specification and registries remain normative.

```console
$ python reference/python/tredecadia.py from-gregorian 2026-09-15
12025-07-11

$ python reference/python/tredecadia.py to-gregorian 00000-EQ
-9999-03-20
```

The reference code supports negative and zero astronomical Gregorian years, negative and zero Tredecadia years, `EQ`, conditional `ED`, strict canonical Tredecadia parsing, and both conversion directions. CI cross-checks it against the published vectors and the independent calendar-arithmetic oracle. See [`reference/python/README.md`](reference/python/README.md).

## Licensing

Documentation, specifications, machine-readable registries, and test vectors are licensed under **CC BY 4.0**. Source code, scripts, and CI/workflow code are licensed under the **MIT License** unless a file states otherwise. See [`LICENSE.md`](LICENSE.md).

The licenses do not grant trademark rights in the Tredecadia name or branding.

## Versioning

The repository currently tracks a pre-1.0 draft. Once the normative text, localization profiles, registry, conversion semantics, test vectors, and compatibility rules have been independently verified, the first stable release will be tagged `v1.0.0`.
