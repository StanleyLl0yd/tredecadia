---
layout: default
title: Tredecadia
---

# Tredecadia

**A 13 × 28 perennial calendar standard.**

Tredecadia has thirteen equal 28-day months, four complete seven-day weeks per month, an independent mathematical year coordinate, and internationally neutral canonical month and weekday names.

> **Stable release: `1.0.0`. Current candidate: `1.1.0-rc.1`.** The candidate is a compatible minor localization expansion; the published v1 canonical calendar identity remains unchanged.

This page is a navigational summary, not a second copy of the standard. Normative requirements remain in the repository specifications and machine-readable registries.

[Read the project introduction in all available languages](https://github.com/StanleyLl0yd/tredecadia/blob/main/README.languages.md) · [Stable v1.0.0](https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.0.0) · [Historical RC2](https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.0.0-rc.2) · [Historical RC1](https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.0.0-rc.1)

## Calendar at a glance

- 13 regular months × 28 days = 364 regular days.
- Every month starts `W1` / **Mene** and ends `W7` / **Toze**.
- `EQ` — **Equinox / New Year Day** — opens each year outside the month/week cycle.
- In a leap year, `ED` — **Earth Day** — follows month 13 day 28 and precedes the next year's `EQ`.
- Tredecadia Era (`TE`) is one integer year axis with a real year `0`.
- `TE 00000-EQ` is conventionally anchored to astronomical proleptic-Gregorian `-9999-03-20` (**10000 BCE — Before Common Era —** in historical notation).

Ordinary boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Leap boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Canonical weekdays

| Position | ID | Name |
|---:|---|---|
| 1 | `W1` | Mene |
| 2 | `W2` | Noko |
| 3 | `W3` | Kese |
| 4 | `W4` | Zoyo |
| 5 | `W5` | Sote |
| 6 | `W6` | Yemo |
| 7 | `W7` | Toze |

The weekday cycle is structural; it is not inherited from the Gregorian weekday label of a converted civil date. RC2 replaces the English weekday strings used by RC1 with these neutral canonical identities before stable v1.0.0.

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

**TE `12025-07-11` — day 11 of Muyasanumi, `W4` / Zoyo.**

Canonical machine syntax is strict ASCII. Human-facing interfaces may display unpadded year values such as `1 TE` or a typographic negative value such as `−1 TE`; those are presentation forms, not alternate machine identifiers.

## Localization

Stable `1.0.0` includes three **stable month** display profiles:

- Russian Cyrillic (`ru-Cyrl`);
- Japanese Katakana (`ja-Kana`);
- Korean Hangul (`ko-Hang`).

The `1.1.0-rc.1` candidate adds six **reviewed month-only** profiles: Georgian Mkhedruli (`ka-Geor`), Eastern Armenian (`hy-Armn`), fully vocalized Arabic (`ar-Arab`), Hindi-oriented Devanagari (`hi-Deva`), Bengali (`bn-Beng`), and Iranian Persian (`fa-Arab`).

Localized month spellings are aliases and never change canonical month numbers, Latin names, syllables, Short-6, or Short-4 identifiers. No weekday aliases are inferred from month profiles; the weekday `E/O` syllables require separate review.

## Published RC2 identity

- tag: `v1.0.0-rc.2`
- source commit: `b816d613618d51515d910e0d3bdb9d2f211b6d22`
- published: `2026-09-16T09:44:59Z`
- archive SHA-256: `23e40180098c656c88aa4ba27c6989ac053d9ce8b8029c9ce2e3b16946bf32ec`
- earliest observation completion: `2026-09-17T09:44:59Z`

The guarded publication workflow reran the full conformance suite, created the tag/release, verified the remote tag target, downloaded the published archive and checksum again, and byte-compared them with the locally generated deterministic assets.

## Standard and data

The GitHub repository is the canonical source:

- [Calendar Standard](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/calendar-standard.md)
- [Conversion Standard](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/conversion-standard.md)
- [Month Naming Standard](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/month-naming-standard.md)
- [Date Notation](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/date-notation.md)
- [Localization](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/localization.md)
- [Compatibility Policy](https://github.com/StanleyLl0yd/tredecadia/blob/main/specification/compatibility.md)
- [Machine-readable registries](https://github.com/StanleyLl0yd/tredecadia/tree/main/registry)
- [Python reference implementation](https://github.com/StanleyLl0yd/tredecadia/tree/main/reference/python)

Tredecadia specifications, registries, and published test vectors are CC BY 4.0. Reference/source code is MIT licensed unless a file states otherwise.
