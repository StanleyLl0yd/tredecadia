# Tredecadia

Tredecadia is an open 13 × 28 perennial calendar standard with equal months, stable weekdays, and internationally neutral month names.

> **Status:** draft. The repository is being prepared for a first public specification release. Nothing in the current draft should be treated as a frozen v1.0 requirement unless explicitly marked normative.

## Core model

- 13 months × 28 days = 364 in-month days.
- Every month has exactly four complete weeks.
- Day `01` of every month is Monday; day `28` is Sunday.
- One year-end intercalary day sits outside the month/week cycle in an ordinary year.
- A leap year has one additional intercalary day, also outside the week cycle.
- The canonical month names are designed for international neutrality and high mutual distinguishability.

## Specification

- [`specification/calendar-standard.md`](specification/calendar-standard.md) — calendar structure.
- [`specification/month-naming-standard.md`](specification/month-naming-standard.md) — canonical month names, pronunciation, and abbreviations.
- [`specification/date-notation.md`](specification/date-notation.md) — date representation.
- [`specification/localization.md`](specification/localization.md) — localization rules.

Machine-readable data lives in [`registry/`](registry/); verification vectors live in [`tests/`](tests/). Design rationale is intentionally separated from normative text in [`rationale/`](rationale/).

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

## Licensing

Documentation and specifications are licensed under **CC BY 4.0**. Source code and scripts, when added, are licensed under the **MIT License** unless a file states otherwise. See [`LICENSE.md`](LICENSE.md).

The licenses do not grant trademark rights in the Tredecadia name or branding.

## Versioning

The repository currently tracks a pre-1.0 draft. Once the normative text, registry, test vectors, and compatibility rules have been independently verified, the first stable release will be tagged `v1.0.0`.
