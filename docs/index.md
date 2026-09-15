---
layout: default
title: Tredecadia
---

# Tredecadia

**A 13 × 28 perennial calendar standard.**

Tredecadia has thirteen equal 28-day months, four complete Monday–Sunday weeks per month, an independent mathematical year coordinate, and internationally neutral canonical month names.

> Pre-1.0 release-candidate work is in progress. Normative source files remain in the repository specifications and machine-readable registries.

## Calendar at a glance

- 13 regular months × 28 days = 364 regular days.
- Every month starts Monday and ends Sunday.
- `EQ` — **Equinox / New Year Day** — opens each year outside the month/week cycle.
- In a leap year, `ED` — **Earth Day** — follows month 13 day 28 and precedes the next year's `EQ`.
- Tredecadia Era (`TE`) is one integer year axis with a real year `0`.
- `TE 00000-EQ` is conventionally anchored to astronomical proleptic-Gregorian `-9999-03-20` (10000 BCE in historical notation).

Ordinary boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Leap boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

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

Short-4 is the preferred conversational compact form when the Tredecadia month context is already clear. Short-6 provides additional redundancy for written/display use.

## Example

Gregorian `2026-09-15` maps to:

**TE `12025-07-11` — day 11 of Muyasanumi.**

Canonical machine syntax is strict ASCII. Human-facing interfaces may display unpadded year values such as `1 TE` or a typographic negative value such as `−1 TE`; those are presentation forms, not alternate machine identifiers.

## Localization

The canonical Latin identifiers are language-neutral. Draft 0.3 has independently reviewed, non-stable display profiles for:

- Russian Cyrillic (`ru-Cyrl`);
- Japanese Katakana (`ja-Kana`);
- Korean Hangul (`ko-Hang`).

Localized spellings are aliases and never change canonical month numbers, Latin names, syllables, Short-6, or Short-4 identifiers.

## Standard and data

The GitHub repository is the canonical source during pre-1.0 development:

- [Calendar Standard](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/calendar-standard.md)
- [Conversion Standard](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/conversion-standard.md)
- [Month Naming Standard](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/month-naming-standard.md)
- [Date Notation](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/date-notation.md)
- [Localization](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/localization.md)
- [Compatibility Policy](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/compatibility.md)
- [Machine-readable registries](https://github.com/StanleyLl0yd/tredecadia/tree/main/registry)
- [Python reference implementation](https://github.com/StanleyLl0yd/tredecadia/tree/main/reference/python)

Tredecadia specifications, registries, and published test vectors are CC BY 4.0. Reference/source code is MIT licensed unless a file states otherwise.
