# Changelog

All notable changes to Tredecadia will be documented here.

The project follows Semantic Versioning for stable public releases where practical.

## [Unreleased]

### Added

- Executable M4 stable-promotion state machine, immutable v1 identity baseline, and atomic RC-to-stable transition manifest.
- Machine-readable 14-day RC observation record and structured GitHub RC feedback form.
- Nineteen natural-language README editions in addition to English, with CI checks for canonical facts and release-version synchronization.
- Reviewed local-script month presentation in Russian, Japanese, and Korean README editions, while avoiding unreviewed script transliterations elsewhere.
- GitHub Pages build/deployment workflow and CI-checked public navigation page; deployment remains manually gated until the repository's one-time Pages setting is enabled.
- Immutable `release/published-releases.json` record for published tag/commit/archive identities.
- Published-release source-lock checks in ordinary CI and the guarded release workflow.

### Changed

- Expanded and localized BCE/CE explanations and removed avoidable English prose fragments from non-English README editions.
- Release-bundle reproducibility CI now uses an explicitly unpublished snapshot version when testing the evolving default branch.
- Stable publication now reruns Pages, RC-observation, and published-release source-lock gates in addition to the existing conformance suite.

### Fixed

- Prevented a post-release source tree from creating a different archive under an already-published version name; historical published artifacts must be reproduced from their exact recorded source commit/tag.

## 1.0.0-rc.1 — 2026-09-15

First v1 release candidate. The compatibility-critical calendar/month/date surface is frozen for RC testing; localization profiles remain reviewed but non-stable until final `v1.0.0` acceptance.

### Added

- Pronunciation model separating segmental month identity from citation prosody.
- Weak initial citation prominence shared by Full, Short-6, and Short-4 forms.
- Explicit conversational role for Short-4 and pronunciation conformance examples.
- Short-4 conversational/UX review, machine-readable recognition-policy vectors, and executable close-pair checks.
- Conservative fuzzy/voice recognition guidance for `Nazu/Kazu`, `Yani/Yana`, and the syllable-close `Yani/Suni` pair.
- Machine-readable pronunciation policy in the month registry.
- Localization maturity model: `candidate`, `reviewed`, and `stable`.
- Separate machine-readable localization registry and JSON Schema.
- Standards-based Japanese Katakana review using Japan's official `外来語の表記` guidance, with approximation notes retained.
- Standards-based Korean Hangul (`ko-Hang`) profile derived from Korea's official IPA-to-Hangul foreign-word rules.
- References-based Russian Cyrillic (`ru-Cyrl`) review using practical-transcription and orthographic sources, with `ми/ни` palatalization explicitly documented as a localization approximation.
- Executable localization derivation, uniqueness, reverse-mapping, maturity, and review-evidence checks.
- Signed-year accessibility/presentation policy separating strict machine syntax from human display.
- Machine-readable accessibility vectors for padded, signed, intercalary, and semantic date cases.
- Reference display-year helper and strict rejection checks for Unicode minus signs, localized digits, alternate separators, and presentation whitespace.
- Dependency-free Python reference implementation for Tredecadia/Gregorian conversion.
- Strict canonical Tredecadia parser and small conversion CLI.
- Reference-implementation conformance tests against published vectors and the independent M1 arithmetic oracle.
- Normative v1 compatibility policy and executable RC freeze checks.
- Draft 2020-12 JSON Schema validation using a pinned standards implementation.
- Repository-local Markdown and `$schema` link validation.
- Release-candidate evidence audit record for reviewed localization references.
- Deterministic release-bundle builder with embedded manifest and SHA-256 checksum output.
- Byte-for-byte release reproducibility test in CI.
- GitHub Pages documentation source under `docs/`, with canonical data still sourced from registries/specifications.

### Changed

- Renamed the ambiguous month-registry `ipa` field to `citationIpa` before the v1 freeze.
- Clarified that stress placement/strength is not identity-critical and may adapt in localized speech.
- Clarified that Short-4 is deterministic only in an established month/date context and must not silently fuzzy-autocorrect between valid month forms.
- Advanced the canonical month-registry schema to version 3 and moved language-specific display aliases out of `months.json` into `localizations.json`.
- Promoted `ja-Kana`, `ko-Hang`, and `ru-Cyrl` to `reviewed`; all remain non-stable during the RC.
- Tightened reference parsers to ASCII digits explicitly at machine/reference CLI boundaries.
- Transitioned public specification/artifact version identifiers from `0.3.0-draft` to `1.0.0-rc.1` while retaining schema versions `calendar=1`, `months=3`, and `localizations=1`.

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
