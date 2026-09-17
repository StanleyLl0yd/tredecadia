# Tredecadia Compatibility Policy

Status: **1.1.0-rc.1 — release candidate**

This document defines the Tredecadia properties that are compatibility-critical in stable `v1.0.0` and later v1-compatible revisions.

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in their ordinary standards-document sense.

## 1. Stable identity boundary

After `v1.0.0`, an implementation or specification revision that identifies itself as Tredecadia v1 MUST preserve the following calendar identity:

- 13 regular months;
- 28 regular days per month;
- 364 regular in-month days;
- four `W1`–`W7` weeks per regular month;
- canonical weekday order and identity defined in section 3;
- intercalary `EQ` outside month/week and opening each year;
- conditional intercalary `ED` outside month/week and closing a leap year;
- the Tredecadia Era integer year coordinate, including real year `0`;
- the mathematical origin `00000-EQ` at astronomical proleptic-Gregorian `-9999-03-20`;
- the civil conversion formulas and derived leap rule.

Changing any of those properties creates a different incompatible calendar and requires a new major version or a separately named profile.

## 2. Canonical month identity

The following are compatibility-critical after v1.0:

- month numbers `01..13`;
- the canonical month order;
- canonical ASCII Latin names;
- ordered five-syllable segmental identity;
- canonical Short-6 forms;
- canonical Short-4 forms.

The v1 canonical names are, in month order:

`Masanumika, Tasuzunumu, Nazumasanu, Mikasumani, Yanimuzunu, Zumitanasu, Muyasanumi, Sunizusaka, Numanamuta, Kazunusuya, Yanazumasa, Sanumikazu, Nimutazuna`.

A newly discovered serious lexical or safety issue after v1.0 may justify a future major-version change, but does not permit silently mutating v1 identifiers.

## 3. Canonical weekday identity

The seven weekday positions and their canonical names are compatibility-critical after v1.0:

| Position | ID | Canonical name | Ordered syllables |
|---:|---|---|---|
| 1 | `W1` | Mene | `ME NE` |
| 2 | `W2` | Noko | `NO KO` |
| 3 | `W3` | Kese | `KE SE` |
| 4 | `W4` | Zoyo | `ZO YO` |
| 5 | `W5` | Sote | `SO TE` |
| 6 | `W6` | Yemo | `YE MO` |
| 7 | `W7` | Toze | `TO ZE` |

The following are part of v1 identity:

- machine identifiers `W1..W7`;
- their order;
- canonical ASCII Latin names;
- ordered two-syllable segmental identity;
- `W1` on regular month days `01`, `08`, `15`, and `22`;
- `W7` on regular month days `07`, `14`, `21`, and `28`.

Stress is not weekday identity-critical. Citation pronunciation uses weak initial prominence.

`v1.0.0-rc.1` used the English names Monday through Sunday directly in the calendar registry. Replacing that RC-only surface with the neutral `W1..W7` identity is an intentional pre-stable compatibility correction introduced by `v1.0.0-rc.2`; the published RC1 tag and artifacts remain immutable historical records.

## 4. Pronunciation compatibility

The ordered canonical CV syllables are segmental identity and are compatibility-critical.

The following v1 pronunciation policy is also retained:

- stress is not identity-critical;
- citation pronunciation uses weak initial prominence;
- month Full, Short-6, and Short-4 forms inherit that same reference prominence location;
- canonical weekdays likewise use weak initial reference prominence;
- localized speech may apply documented language-specific phonetic adaptation without redefining canonical syllables.

Compatible revisions MAY clarify phonetic detail, examples, or localization guidance, provided they do not redefine the canonical segmental sequence.

## 5. Canonical date syntax

The v1 machine grammar is compatibility-critical:

- minimum five ASCII digits of year magnitude;
- no sign for non-negative years;
- ASCII `-` before negative years;
- no leading `+`;
- no negative zero;
- no redundant padding beyond the five-digit minimum;
- regular dates `YEAR-MM-DD` with `MM=01..13`, `DD=01..28`;
- intercalary forms `YEAR-EQ` and conditional `YEAR-ED`;
- uppercase `EQ` and `ED` tokens.

Human display conventions such as unpadded `1 TE` or typographic `−1 TE` are not additional canonical serializations.

## 6. Recognition policy

Short-4 remains a conversational compact month form, not a globally reserved natural-language token.

Compatible v1 implementations MUST NOT silently fuzzy-autocorrect one valid canonical Short-4 month into another. Recognition systems MAY use context, confidence, confirmation, or longer forms to resolve ambiguity.

Canonical weekday names are also distinct identifiers rather than globally reserved natural-language words. Fuzzy recognition SHOULD preserve explicit `W1..W7` identity and SHOULD NOT silently substitute a different valid weekday when confidence is low.

## 7. Machine registry contracts

Published stable v1 registry files and their schema versions form part of the implementation contract.

Within v1:

- required fields MUST retain their meaning;
- a required field MUST NOT be removed or reinterpreted incompatibly;
- enumerated identifiers MUST NOT be silently repurposed;
- new optional fields MAY be added in a compatible minor revision if older consumers can safely ignore them;
- an incompatible schema change requires a new schema version and, when it changes stable calendar identity, a new Tredecadia major version.

Schema-version changes and specification-version changes are related but distinct: a schema may evolve compatibly without changing calendar identity.

The calendar registry schema advances from version `1` in RC1 to version `2` in RC2 because the weekday contract changes from seven English strings to seven structured canonical weekday identities. This is permitted only because both releases precede stable `v1.0.0` and the incompatibility is explicit.

## 8. Localization compatibility

Localized profiles are aliases, never canonical month or weekday identity.

At the stable v1 release, profiles explicitly promoted to `stable` become stable v1 display profiles. Within the v1 line:

- profile IDs MUST remain stable;
- aliases SHOULD remain stable once published;
- a correction that changes a stable alias MUST be documented as a localization compatibility change and MUST preserve unique reverse mapping to the same canonical identity;
- adding a new reviewed/stable language or script profile is compatible and does not change canonical month or weekday identity;
- localization MUST NOT change month numbers, canonical Latin month names, canonical month syllables or canonical abbreviations;
- localization MUST NOT change weekday IDs `W1..W7`, their order, canonical Latin weekday names, or canonical weekday syllables.

The reviewed `ru-Cyrl`, `ja-Kana`, and `ko-Hang` profiles in RC2 continue to cover month aliases only. Weekday aliases require separate evidence and review; RC2 does not silently infer `E/O` mappings from the reviewed month profiles.

## 9. Versioning classes

After v1.0:

- **major**: incompatible calendar identity, canonical month identity, canonical weekday identity, era/conversion, or canonical date-syntax change;
- **minor**: compatible additions such as new localization profiles, new optional registry metadata, additional test vectors, or reference implementations;
- **patch**: editorial corrections, clarifications, test hardening, and implementation fixes that do not alter normative behavior.

Before v1.0, release-candidate changes remain possible, but every change to the compatibility-critical surface MUST be called out explicitly in the release-candidate audit and represented by a new release candidate rather than rewriting a published RC.
