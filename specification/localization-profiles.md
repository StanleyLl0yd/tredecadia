# Tredecadia Localization Profiles

Status: **1.0.0-rc.2**

Canonical month identity is language-neutral and lives in `registry/months.json`. Canonical weekday identity lives in `registry/calendar.json`. Localized display aliases live separately from canonical identity and never replace month numbers, weekday IDs, canonical Latin names, or canonical syllable sequences.

The profiles currently registered in `registry/localizations.json` cover **months only**. A future profile may add weekday aliases, but it must explicitly review/register the weekday `E/O` syllable space rather than infer it from a month-only mapping.

## Profile methods

A profile records its language, script, direction, derivation method, syllable mapping, aliases, reverse-mapping rule, and review evidence.

- `transliteration`: primarily maps writing-system symbols.
- `phonemic-transcription`: primarily maps the intended sound sequence.
- `orthographic-adaptation`: follows target-language spelling conventions.

Every registered alias MUST resolve to exactly one canonical identity within its profile. For current month profiles, every Full, Short-6, and Short-4 alias MUST resolve to exactly one month. A future weekday alias MUST resolve uniquely to one `W1..W7` identity. Character-by-character reversibility to Latin is not required.

## Maturity

`candidate` means proposed but not independently validated. Generated tables may be candidates, but MUST NOT be presented as reviewed or stable.

`reviewed` requires recorded independent evidence such as competent language/script review or a directly applicable orthographic or transcription reference. Material sound approximations MUST be documented.

`stable` means the reviewed profile was explicitly accepted into a stable Tredecadia release. A profile MUST NOT be `stable` while the localization registry itself is `draft`.

## Promotion

Before promotion of a month profile, verify all 13 Full, Short-6, and Short-4 aliases, confirm uniqueness and reverse mapping, review material pronunciation/orthography approximations, and record the evidence in the registry. Automatic bulk transliteration cannot bypass this process.

Before adding/promoting weekday aliases, verify all seven `W1..W7` mappings independently, including the canonical `E/O` vowels, unique reverse mapping, and any material language-specific approximations. Existing month-profile evidence does not automatically satisfy this requirement.

Evidence may establish a profile at `reviewed` without claiming that it has undergone a separate native-speaker usability study. Where that distinction matters, the profile notes and rationale MUST say so explicitly.

`1.0.0-rc.2` month-profile status:

- `ru-Cyrl`: `reviewed` using independent Russian practical-transcription and orthographic references; the predictable palatalization in `ми/ни` is explicitly documented;
- `ja-Kana`: `reviewed` using an independent Japanese government orthographic standards reference;
- `ko-Hang`: `reviewed` using the Korean National Institute's official IPA-to-Hangul foreign-word rules.

All three remain non-stable throughout the release-candidate phase. Promotion to `stable` is a deliberate final `v1.0.0` release action. RC2 does not add localized weekday aliases.
