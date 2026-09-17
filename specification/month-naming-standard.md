# Tredecadia Month Naming Standard

Status: **1.1.0-rc.1 — release candidate**

This document defines the canonical names, pronunciation model, and standard abbreviations of Tredecadia's 13 regular months.

## 1. Canonical syllables

`MA MI MU NA NI NU SA SU TA YA KA ZU`

Each canonical month name contains exactly five open CV syllables.

The canonical segmental values are:

- `MA /ma/`, `MI /mi/`, `MU /mu/`;
- `NA /na/`, `NI /ni/`, `NU /nu/`;
- `SA /sa/`, `SU /su/`;
- `TA /ta/`;
- `YA /ja/`;
- `KA /ka/`;
- `ZU /zu/`.

## 2. Pronunciation identity

The **ordered segmental syllable sequence** is the normative pronunciation identity of a canonical month name.

Stress placement is **not identity-critical**. A spoken form MUST NOT be treated as a different month solely because a speaker or language realizes prominence differently.

Tredecadia nevertheless defines one reproducible **citation pronunciation** for teaching, dictionaries, synthesized speech, and cross-language reference. Its reference prosody uses **weak initial prominence on the first syllable**.

The intended effect is light/non-emphatic prominence, not a strongly stressed lexical accent. The IPA primary-stress mark in citation forms records the reference **location** of prominence; it MUST NOT be interpreted as requiring unusually strong stress.

Thus the canonical segmental form of `Masanumika` is:

`/ma.sa.nu.mi.ka/`

and its reference citation realization is shown as:

`[ˈma.sa.nu.mi.ka]`

The slash form represents the broad segmental sequence. The bracketed citation form adds the reference prominence location. It is not a claim that every localized natural pronunciation must use identical stress strength, rhythm, pitch, or allophones.

### 2.1 Local spoken adaptation

A localized spoken realization MAY adapt stress, rhythm, pitch accent, and predictable allophony to the target language, provided that:

- the five syllables remain in canonical order;
- no canonical syllable is deliberately added, deleted, or reordered;
- the intended consonant/vowel sequence remains recognizable as closely as the target language permits;
- localized adaptation does not create a new canonical spelling or identifier.

Where a target language cannot reproduce a canonical contrast exactly, its localization profile SHOULD document the approximation.

## 3. Canonical months

| # | Name | Syllables | Segmental IPA | Citation IPA | Short-6 | Short-4 |
|---:|---|---|---|---|---|---|
| 01 | Masanumika | MA-SA-NU-MI-KA | /ma.sa.nu.mi.ka/ | [ˈma.sa.nu.mi.ka] | Masanu | Masa |
| 02 | Tasuzunumu | TA-SU-ZU-NU-MU | /ta.su.zu.nu.mu/ | [ˈta.su.zu.nu.mu] | Tasuzu | Tasu |
| 03 | Nazumasanu | NA-ZU-MA-SA-NU | /na.zu.ma.sa.nu/ | [ˈna.zu.ma.sa.nu] | Nazuma | Nazu |
| 04 | Mikasumani | MI-KA-SU-MA-NI | /mi.ka.su.ma.ni/ | [ˈmi.ka.su.ma.ni] | Mikasu | Mika |
| 05 | Yanimuzunu | YA-NI-MU-ZU-NU | /ja.ni.mu.zu.nu/ | [ˈja.ni.mu.zu.nu] | Yanimu | Yani |
| 06 | Zumitanasu | ZU-MI-TA-NA-SU | /zu.mi.ta.na.su/ | [ˈzu.mi.ta.na.su] | Zumita | Zumi |
| 07 | Muyasanumi | MU-YA-SA-NU-MI | /mu.ja.sa.nu.mi/ | [ˈmu.ja.sa.nu.mi] | Muyasa | Muya |
| 08 | Sunizusaka | SU-NI-ZU-SA-KA | /su.ni.zu.sa.ka/ | [ˈsu.ni.zu.sa.ka] | Sunizu | Suni |
| 09 | Numanamuta | NU-MA-NA-MU-TA | /nu.ma.na.mu.ta/ | [ˈnu.ma.na.mu.ta] | Numana | Numa |
| 10 | Kazunusuya | KA-ZU-NU-SU-YA | /ka.zu.nu.su.ja/ | [ˈka.zu.nu.su.ja] | Kazunu | Kazu |
| 11 | Yanazumasa | YA-NA-ZU-MA-SA | /ja.na.zu.ma.sa/ | [ˈja.na.zu.ma.sa] | Yanazu | Yana |
| 12 | Sanumikazu | SA-NU-MI-KA-ZU | /sa.nu.mi.ka.zu/ | [ˈsa.nu.mi.ka.zu] | Sanumi | Sanu |
| 13 | Nimutazuna | NI-MU-TA-ZU-NA | /ni.mu.ta.zu.na/ | [ˈni.mu.ta.zu.na] | Nimuta | Nimu |

The machine-readable registry is `registry/months.json`. Its `citationIpa` field stores the bracket contents without literal brackets; the `syllables` plus `pronunciation.syllableIpa` fields determine the normative segmental form.

## 4. Canonical spelling

Canonical names use ASCII Latin letters. Display spelling uses initial capital plus lower-case letters. Systems may compare canonical identifiers case-insensitively, but the letter sequence is fixed.

`Y` always corresponds to canonical /j/ in `YA`; `Z` corresponds to canonical /z/ in `ZU`. Local script profiles may use the closest conventional representation available to the target language.

## 5. Abbreviations and conversational forms

**Short-6** is the first three complete syllables. **Short-4** is the first two complete syllables. Both sets are unique across all 13 months.

Five-letter truncation is non-standard because it cuts a CV syllable boundary.

Short-4 is the preferred **conversational compact form** when context already makes clear that a Tredecadia month is being named. Short-6 remains the safer written/display abbreviation where more redundancy is useful.

Full, Short-6, and Short-4 forms all inherit the same weak initial citation prominence because they share the same first syllable. Shortening therefore never moves the reference prominence.

Example:

- full: `Masanumika` → `[ˈma.sa.nu.mi.ka]`;
- Short-6: `Masanu` → `[ˈma.sa.nu]`;
- Short-4: `Masa` → `[ˈma.sa]`.

A localized realization with different natural prosody remains the same month as long as the canonical segmental sequence is preserved recognizably.

### 5.1 Recognition and ambiguity

An exact case-insensitive Short-4 value in a structured Tredecadia month/date context maps to exactly one canonical month and MAY be resolved directly.

Short-4 is not intended to be a globally reserved natural-language vocabulary. A Short-4 token appearing in unrestricted prose MUST NOT be assumed to denote a Tredecadia month solely because its spelling matches a month abbreviation.

Implementations that provide fuzzy text matching, autocorrection, or speech recognition MUST NOT silently transform one valid canonical Short-4 form into a different valid canonical Short-4 form.

The character-distance-1 pairs are:

- `Nazu` / `Kazu`;
- `Yani` / `Yana`.

At the canonical two-syllable level, the distance-1 pairs are:

- `Nazu` / `Kazu`;
- `Yani` / `Suni`;
- `Yani` / `Yana`.

When recognition leaves more than one of these valid forms plausible, an interactive implementation SHOULD request disambiguation or present the candidate months rather than guess.

Voice interfaces SHOULD use surrounding month/date context and SHOULD treat the syllable-distance-1 pairs as known recognition neighbours. Machine storage SHOULD use the canonical month number or full canonical name after recognition rather than preserve a probabilistic recognition hypothesis as the month identifier.

Assistive labels SHOULD make month semantics explicit when a visually compact Short-4 form appears without sufficient surrounding structure; for example, an implementation may expose the localized equivalent of “Masa, month 1” while displaying only `Masa`.

## 6. Stability

After the first stable release, month number, canonical Latin name, ordered segmental syllable sequence, Short-6, and Short-4 are intended to be compatibility-critical.

Reference prominence policy and localized phonetic realization may be clarified in compatible revisions provided that they do not redefine the canonical segmental sequence.

## 7. Design record (non-normative)

The full-name syllable-frequency vector is `MA=5, MI=5, MU=5, NA=5, NI=4, NU=8, SA=6, SU=5, TA=4, YA=4, KA=5, ZU=9`.

Full-name balance SSD is exactly `323/12` (approximately `26.9166666666667`), with sum of squared syllable counts `379`. Short-6 balance SSD is exactly `41/4` (`10.25`); Short-4 balance SSD is exactly `11/3` (approximately `3.66666666666667`).

The only Short-6 pair at Levenshtein distance 2 is `Yanimu` / `Yanazu`. The Short-4 pairs at character Levenshtein distance 1 are `Nazu` / `Kazu` and `Yani` / `Yana`. The Short-4 pairs at positional syllable Hamming distance 1 are `Nazu` / `Kazu`, `Yani` / `Suni`, and `Yani` / `Yana`.
