# Tredecadia Compatibility Policy

Status: **Draft 0.3 — v1 release-candidate policy**

This document defines which Tredecadia properties are intended to become compatibility-critical at the first stable `v1.0.0` release.

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in their ordinary standards-document sense.

## 1. Stable identity boundary

After `v1.0.0`, an implementation or specification revision that identifies itself as Tredecadia v1 MUST preserve the following calendar identity:

- 13 regular months;
- 28 regular days per month;
- 364 regular in-month days;
- four Monday–Sunday weeks per regular month;
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

## 3. Pronunciation compatibility

The ordered canonical CV syllables are segmental identity and are compatibility-critical.

The following v1 pronunciation policy is also retained:

- stress is not identity-critical;
- citation pronunciation uses weak initial prominence;
- Full, Short-6, and Short-4 inherit that same reference prominence location;
- localized speech may apply documented language-specific phonetic adaptation without redefining canonical syllables.

Compatible revisions MAY clarify phonetic detail, examples, or localization guidance, provided they do not redefine the canonical segmental sequence.

## 4. Canonical date syntax

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

## 5. Recognition policy

Short-4 remains a conversational compact form, not a globally reserved natural-language token.

Compatible v1 implementations MUST NOT silently fuzzy-autocorrect one valid canonical Short-4 month into another. Recognition systems MAY use context, confidence, confirmation, or longer forms to resolve ambiguity.

## 6. Machine registry contracts

Published stable v1 registry files and their schema versions form part of the implementation contract.

Within v1:

- required fields MUST retain their meaning;
- a required field MUST NOT be removed or reinterpreted incompatibly;
- enumerated identifiers MUST NOT be silently repurposed;
- new optional fields MAY be added in a compatible minor revision if older consumers can safely ignore them;
- an incompatible schema change requires a new schema version and, when it changes stable calendar identity, a new Tredecadia major version.

Schema-version changes and specification-version changes are related but distinct: a schema may evolve compatibly without changing calendar identity.

## 7. Localization compatibility

Localized profiles are aliases, never canonical month identity.

At the stable v1 release, profiles explicitly promoted to `stable` become stable v1 display profiles. Within the v1 line:

- profile IDs MUST remain stable;
- aliases SHOULD remain stable once published;
- a correction that changes a stable alias MUST be documented as a localization compatibility change and MUST preserve unique reverse mapping to the same canonical month;
- adding a new reviewed/stable language or script profile is compatible and does not change canonical month identity;
- localization MUST NOT change month numbers, canonical Latin names, canonical syllables, or canonical abbreviations.

The `1.0.0-rc.1` preparation phase keeps profiles at `reviewed`; final promotion to `stable` is a `v1.0.0` release action.

## 8. Versioning classes

After v1.0:

- **major**: incompatible calendar identity, canonical month identity, era/conversion, or canonical date-syntax change;
- **minor**: compatible additions such as new localization profiles, new optional registry metadata, additional test vectors, or reference implementations;
- **patch**: editorial corrections, clarifications, test hardening, and implementation fixes that do not alter normative behavior.

Before v1.0, release-candidate changes remain possible, but every change to the compatibility-critical surface MUST be called out explicitly in the release-candidate audit.
