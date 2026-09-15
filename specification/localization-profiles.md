# Tredecadia Localization Profiles

Status: **Draft 0.3**

Canonical month identity is language-neutral and lives in `registry/months.json`. Localized display aliases live separately in `registry/localizations.json` and never replace canonical month numbers, Latin names, syllable sequences, Short-6, or Short-4 forms.

## Profile methods

A profile records its language, script, direction, derivation method, syllable mapping, aliases, reverse-mapping rule, and review evidence.

- `transliteration`: primarily maps writing-system symbols.
- `phonemic-transcription`: primarily maps the intended sound sequence.
- `orthographic-adaptation`: follows target-language spelling conventions.

Every Full, Short-6, and Short-4 alias MUST resolve to exactly one month within its profile. Character-by-character reversibility to Latin is not required.

## Maturity

`candidate` means proposed but not independently validated. Generated tables may be candidates, but MUST NOT be presented as reviewed or stable.

`reviewed` requires recorded independent evidence such as competent language/script review or a directly applicable orthographic or transcription reference. Material sound approximations MUST be documented.

`stable` means the reviewed profile was explicitly accepted into a stable Tredecadia release. A profile MUST NOT be `stable` while the localization registry itself is `draft`.

## Promotion

Before promotion, verify all 13 Full, Short-6, and Short-4 aliases, confirm uniqueness and reverse mapping, review material pronunciation/orthography approximations, and record the evidence in the registry. Automatic bulk transliteration cannot bypass this process.

Evidence may establish a profile at `reviewed` without claiming that it has undergone a separate native-speaker usability study. Where that distinction matters, the profile notes and rationale MUST say so explicitly.

Draft 0.3 profile status:

- `ru-Cyrl`: `reviewed` using independent Russian practical-transcription and orthographic references; the predictable palatalization in `ми/ни` is explicitly documented;
- `ja-Kana`: `reviewed` using an independent Japanese government orthographic standards reference;
- `ko-Hang`: `reviewed` using the Korean National Institute's official IPA-to-Hangul foreign-word rules.

All three remain non-stable until an explicit stable Tredecadia release adopts them.
