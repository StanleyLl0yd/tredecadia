# Tredecadia Localization

Status: **Draft 0.3**

Localized spellings are display aliases. They do not replace canonical month numbers, Latin names, syllable sequences, Short-6, or Short-4 forms.

Canonical month data lives in `registry/months.json`. Localized aliases live in `registry/localizations.json`.

Profile methods, maturity states, evidence rules, reverse mapping, and promotion are defined in [`localization-profiles.md`](localization-profiles.md).

## Pronunciation adaptation

Canonical segmental syllables remain identity-critical. Citation pronunciation uses weak initial prominence, but localized speech MAY adapt stress, rhythm, pitch accent, vowel quality, and predictable allophony.

A profile SHOULD document material approximations when its language or script cannot reproduce a canonical sound exactly. Those approximations do not change canonical Tredecadia pronunciation identity.

## Current draft profiles

Draft 0.3 currently includes two machine-readable candidate profiles:

- `ru-Cyrl` - Russian Cyrillic;
- `ja-Kana` - Japanese Katakana.

Both are `candidate`, not reviewed or stable.

Within each profile every registered Full, Short-6, and Short-4 alias MUST map back to exactly one canonical month. Character-by-character reversibility to Latin is not required.
