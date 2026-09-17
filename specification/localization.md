# Tredecadia Localization

Status: **1.0.0**

Localized spellings are display aliases. They do not replace canonical machine identifiers or canonical Latin identity.

Canonical month data lives in `registry/months.json`. The currently reviewed localized aliases in `registry/localizations.json` are **month aliases**.

Canonical weekday identity lives in `registry/calendar.json` as `W1..W7` plus canonical Latin names. RC2 does not automatically extend the existing month profiles to weekdays: weekday aliases require separately reviewed mappings because the weekday syllable inventory introduces `E/O` values that are absent from the month inventory.

Profile methods, maturity states, evidence rules, reverse mapping, and promotion are defined in [`localization-profiles.md`](localization-profiles.md).

## Pronunciation adaptation

Canonical segmental syllables remain identity-critical. Citation pronunciation uses weak initial prominence, but localized speech MAY adapt stress, rhythm, pitch accent, vowel quality, consonant quality, and predictable allophony.

A profile SHOULD document material approximations when its language or script cannot reproduce a canonical sound exactly. Those approximations do not change canonical Tredecadia pronunciation identity.

For canonical weekdays, a localized display/speech mapping MUST preserve the underlying `W1..W7` position and unique reverse mapping. A month-profile syllable map MUST NOT be assumed to cover weekday `E/O` syllables unless the profile explicitly reviews and registers those values.

## Current release-candidate profiles

Tredecadia `1.0.0-rc.2` includes three independently reviewed, non-stable **month display profiles**:

- `ru-Cyrl` — Russian Cyrillic — **reviewed** against Russian practical-transcription and orthographic references; `MI/NI` palatalization is explicitly documented as a Russian adaptation;
- `ja-Kana` — Japanese Katakana — **reviewed** against the Japanese Agency for Cultural Affairs `外来語の表記` guidance;
- `ko-Hang` — Korean Hangul — **reviewed** against the National Institute of Korean Language `외래어 표기법` IPA-to-Hangul rules.

These reviews are evidence-based script/orthography reviews. They do not claim a separate usability study with a panel of native speakers. Evidence and approximation notes are recorded in `registry/localizations.json` and the corresponding rationale files.

No profile is `stable` in `1.0.0-rc.2`; final stable promotion is reserved for an explicitly accepted `v1.0.0` release.

Within each profile every registered Full, Short-6, and Short-4 month alias MUST map back to exactly one canonical month. Character-by-character reversibility to Latin is not required.
