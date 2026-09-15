# Changelog

All notable changes to Tredecadia will be documented here.

The project follows Semantic Versioning for stable public releases where practical.

## [Unreleased]

### Added

- Draft 0.3 pronunciation model separating segmental month identity from citation prosody.
- Weak initial citation prominence shared by Full, Short-6, and Short-4 forms.
- Explicit conversational role for Short-4 and pronunciation conformance examples.
- Short-4 conversational/UX review, machine-readable recognition-policy vectors, and executable close-pair checks.
- Conservative fuzzy/voice recognition guidance for `Nazu/Kazu`, `Yani/Yana`, and the syllable-close `Yani/Suni` pair.
- Machine-readable pronunciation policy in the month registry.
- Localization maturity model: `candidate`, `reviewed`, and `stable`.
- Separate machine-readable localization registry and JSON Schema.
- Candidate Russian Cyrillic (`ru-Cyrl`) and Japanese Katakana (`ja-Kana`) profiles.
- Executable localization derivation, uniqueness, reverse-mapping, and maturity checks.
- Pronunciation rationale and localization adaptation guidance.
- Dependency-free Python reference implementation for Tredecadia/Gregorian conversion.
- Strict canonical Tredecadia parser and small conversion CLI.
- Reference-implementation conformance tests against published vectors and the independent M1 arithmetic oracle.

### Changed

- Renamed the ambiguous month-registry `ipa` field to `citationIpa` in Draft 0.3.
- Clarified that stress placement/strength is not identity-critical and may adapt in localized speech.
- Clarified that Short-4 is deterministic only in an established month/date context and must not silently fuzzy-autocorrect between valid month forms.
- Advanced the canonical month-registry schema to version 3 and moved language-specific display aliases out of `months.json` into `localizations.json`.

## 0.2.0-draft — 2026-09-15

### Added

- Tredecadia Era (`TE`) with a real year `0` and one continuous integer year coordinate.
- Mathematical era origin `00000-EQ` at the conventional March-equinoctial civil boundary associated with 10000 BCE.
- Proleptic-Gregorian conversion using astronomical year numbering, including Gregorian year `0`.
- `EQ` as the opening intercalary day of a Tredecadia year.
- `ED` as the closing intercalary day of a leap Tredecadia year.
- Machine-readable calendar profile and JSON Schema.
- Conversion vectors covering negative Tredecadia years, epoch zero, the 1 BCE/1 CE boundary, modern dates, 2100, and 2400.
- Exhaustive bidirectional conversion tests across two full 400-year cycles spanning astronomical Gregorian year `0`.
- Documentation/table/license-scope and artifact-version consistency checks.
- Signed, minimum-five-digit canonical year notation.

### Changed

- Replaced the temporary Gregorian-number-preserving M1 epoch with the independent Tredecadia Era coordinate.
- Naming balance metrics are represented as exact rational values in verification data and rationale.
- Clarified the CC BY 4.0 scope for specifications, registries, and published test-vector data.
- Updated and SHA-pinned current official GitHub Actions.

## 0.1.0-draft — 2026-09-15

- First public draft of the Tredecadia standard and canonical month registry.
