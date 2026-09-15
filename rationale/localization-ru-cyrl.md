# Russian Cyrillic Localization Review

This document records the evidence used to promote `ru-Cyrl` from `candidate` to `reviewed`. It is non-normative; machine-readable profile status and aliases live in `registry/localizations.json`.

## Method

The profile is Russian practical phonemic transcription, not reversible Latin transliteration. Tredecadia supplies a canonical sound sequence; Russian Cyrillic provides a conventional display alias that follows the source pronunciation as closely as ordinary Russian writing permits.

This matches the general description of practical transcription in the *Большая российская энциклопедия*: practical transcription is used for foreign names and terms, is based on the target-language alphabet, and may map source phonemes directly where appropriate.

Reference:

- https://old.bigenc.ru/linguistics/text/4199684

## `YA /ja/`

Russian orthographic rules state that `я` can represent `[j] + [a]` at the beginning of a word and after a vowel. That is exactly the environment in Tredecadia forms: `YA` either opens a form or follows the vowel of a preceding open syllable.

Examples therefore remain natural:

- `Yanimuzunu` → `Янимузуну`;
- `Muyasanumi` → `Муясануми`;
- `Kazunusuya` → `Казунусуя`.

Reference:

- https://gramota.ru/biblioteka/spravochniki/pravila-russkoy-orfografii-i-punktuatsii/bukvy-a-ya-u-yu

## `MI` and `NI`: documented approximation

Russian `и` represents /i/ while also signalling softness of a preceding paired consonant. Therefore `ми` and `ни` normally realize approximately /mʲi/ and /nʲi/, not a contrastively hard /mi/ and /ni/.

Tredecadia keeps broad canonical values `/mi/` and `/ni/`. The Russian palatalization is accepted as a predictable language-specific phonetic adaptation under the localization policy; it does not change canonical month identity.

Using `мы` or `ны` would preserve harder consonants only by replacing canonical /i/ with Russian /ɨ/, which is a larger vowel-category change. The existing `ми` / `ни` choice therefore remains the more natural Russian transcription.

Reference:

- https://gramota.ru/biblioteka/spravochniki/pravila-russkoy-orfografii-i-punktuatsii/bukvy-i-y

## Remaining syllables

The remaining mappings use ordinary Russian Cyrillic CV values without a material identity problem for this profile:

`MA ма · MU му · NA на · NU ну · SA са · SU су · TA та · KA ка · ZU зу`

Russian speech may apply its normal weak-vowel and prosodic realizations. Those allophonic effects are already permitted by the Tredecadia localization standard and do not redefine the canonical syllable inventory.

## Review result

The existing Full, Short-6, and Short-4 aliases remain unchanged. They are mechanically derived from the reviewed syllable map and are unique within `ru-Cyrl`.

Result: **reviewed**, not stable. Stable status is reserved for an explicitly accepted stable Tredecadia release.
