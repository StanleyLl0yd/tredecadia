# Tredecadia Localization

Status: **Draft 0.3**

Localized spellings are display aliases. They do not replace canonical month numbers, Latin names, syllable sequences, Short-6, or Short-4 forms.

Canonical month data lives in `registry/months.json`. Localized aliases live in `registry/localizations.json`.

Profile methods, maturity states, evidence rules, reverse mapping, and promotion are defined in [`localization-profiles.md`](localization-profiles.md).

## Pronunciation adaptation

Canonical segmental syllables remain identity-critical. Citation pronunciation uses weak initial prominence, but localized speech MAY adapt stress, rhythm, pitch accent, vowel quality, consonant quality, and predictable allophony.

A profile SHOULD document material approximations when its language or script cannot reproduce a canonical sound exactly. Those approximations do not change canonical Tredecadia pronunciation identity.

## Current draft profiles

Draft 0.3 currently includes three independently reviewed, non-stable display profiles:

- `ru-Cyrl` — Russian Cyrillic — **reviewed** against Russian practical-transcription and orthographic references; `MI/NI` palatalization is explicitly documented as a Russian adaptation;
- `ja-Kana` — Japanese Katakana — **reviewed** against the Japanese Agency for Cultural Affairs `外来語の表記` guidance;
- `ko-Hang` — Korean Hangul — **reviewed** against the National Institute of Korean Language `외래어 표기법` IPA-to-Hangul rules.

These reviews are evidence-based script/orthography reviews. They do not claim a separate usability study with a panel of native speakers. Evidence and approximation notes are recorded in `registry/localizations.json` and the corresponding rationale files.

No profile is `stable` while Tredecadia and the localization registry remain pre-1.0/draft.

Within each profile every registered Full, Short-6, and Short-4 alias MUST map back to exactly one canonical month. Character-by-character reversibility to Latin is not required.
