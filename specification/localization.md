# Tredecadia Localization

Status: **1.1.0-rc.1 — release candidate**

Localized spellings are display aliases. They do not replace canonical machine identifiers or canonical Latin identity.

Canonical month data lives in `registry/months.json`. The currently reviewed localized aliases in `registry/localizations.json` are **month aliases**.

Canonical weekday identity lives in `registry/calendar.json` as `W1..W7` plus canonical Latin names. RC2 does not automatically extend the existing month profiles to weekdays: weekday aliases require separately reviewed mappings because the weekday syllable inventory introduces `E/O` values that are absent from the month inventory.

Profile methods, maturity states, evidence rules, reverse mapping, and promotion are defined in [`localization-profiles.md`](localization-profiles.md).

## Pronunciation adaptation

Canonical segmental syllables remain identity-critical. Citation pronunciation uses weak initial prominence, but localized speech MAY adapt stress, rhythm, pitch accent, vowel quality, consonant quality, and predictable allophony.

A profile SHOULD document material approximations when its language or script cannot reproduce a canonical sound exactly. Those approximations do not change canonical Tredecadia pronunciation identity.

For canonical weekdays, a localized display/speech mapping MUST preserve the underlying `W1..W7` position and unique reverse mapping. A month-profile syllable map MUST NOT be assumed to cover weekday `E/O` syllables unless the profile explicitly reviews and registers those values.

## Current release-candidate profiles

Stable `v1.0.0` established three month display profiles at `stable` maturity:

- `ru-Cyrl` — Russian Cyrillic; `MI/NI` palatalization is a documented Russian adaptation;
- `ja-Kana` — Japanese Katakana; reviewed against the Japanese Agency for Cultural Affairs foreign-word orthography guidance;
- `ko-Hang` — Korean Hangul; reviewed against the National Institute of Korean Language IPA-to-Hangul foreign-word rules.

The compatible `1.1.0-rc.1` candidate carries those profiles forward unchanged and adds six independently reviewed month-only profiles at `reviewed` maturity:

- `ka-Geor` — Georgian Mkhedruli;
- `hy-Armn` — Eastern Armenian;
- `ar-Arab` — fully vocalized Arabic;
- `hi-Deva` — Hindi-oriented Devanagari;
- `bn-Beng` — Bengali;
- `fa-Arab` — Iranian Persian.

The six new profiles are evidence-reviewed but are not yet `stable`; stable maturity requires an explicit stable-release acceptance decision. No native-speaker usability study is claimed for them. Evidence, deterministic syllable maps, derived aliases, and documented approximations are recorded in `registry/localizations.json` and the M5 rationale/review records.

Within each profile every registered Full, Short-6, and Short-4 month alias MUST map back to exactly one canonical month. Character-by-character reversibility to Latin is not required.

No registered month profile automatically defines weekday aliases. Weekday aliases require a separate review surface covering `W1..W7` and the canonical weekday `E/O` syllables.
