# Tredecadia

Tredecadia is an open 13 × 28 perennial calendar standard with equal months, stable weekdays, and internationally neutral month names.

> **Status:** pre-1.0 draft. M0 repository bootstrap is complete. M1 currently contains a review proposal for the fixed March-equinoctial civil conversion profile; it is not yet frozen as v1.0.

## Core model

- 13 months × 28 days = 364 in-month days.
- Every month has exactly four complete weeks.
- Day `01` of every month is Monday; day `28` is Sunday.
- One year-end intercalary day sits outside the month/week cycle in an ordinary year.
- A leap year has one additional intercalary day, also outside the week cycle.
- The canonical month names are designed for international neutrality and high mutual distinguishability.

## M1 civil conversion proposal

The current review proposal uses a deterministic fixed March anchor:

- Tredecadia `Y-01-01` ↔ Gregorian `Y-03-21`;
- Tredecadia `Y-EQ` ↔ Gregorian `(Y+1)-03-20`;
- when Tredecadia `Y` is leap, `Y-ED` ↔ Gregorian `(Y+1)-03-19`;
- Tredecadia `Y` is leap exactly when Gregorian `Y+1` is leap.

This keeps Equinox / New Year Day associated with the March equinox without making civil conversion depend on an astronomical ephemeris or timezone. See issue #2 and the conversion standard for the full proposal.

## Specification

- [`specification/calendar-standard.md`](specification/calendar-standard.md) — calendar structure.
- [`specification/conversion-standard.md`](specification/conversion-standard.md) — M1 Gregorian conversion proposal.
- [`specification/month-naming-standard.md`](specification/month-naming-standard.md) — canonical month names, pronunciation, and abbreviations.
- [`specification/date-notation.md`](specification/date-notation.md) — date representation.
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

## Licensing

Documentation, specifications, machine-readable registries, and test vectors are licensed under **CC BY 4.0**. Source code, scripts, and CI/workflow code are licensed under the **MIT License** unless a file states otherwise. See [`LICENSE.md`](LICENSE.md).

The licenses do not grant trademark rights in the Tredecadia name or branding.

## Versioning

The repository currently tracks a pre-1.0 draft. Once the normative text, registry, conversion semantics, test vectors, and compatibility rules have been independently verified, the first stable release will be tagged `v1.0.0`.
