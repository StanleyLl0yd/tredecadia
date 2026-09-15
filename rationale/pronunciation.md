# Pronunciation Rationale

This document is non-normative. Normative pronunciation rules live in `specification/month-naming-standard.md`.

## Why stress is not identity-critical

No single primary-stress location is internationally neutral.

The World Atlas of Language Structures (WALS), Chapter 14 / Feature 14A, classifies a 502-language sample as follows:

| Stress type | Languages |
|---|---:|
| No fixed stress | 220 |
| Initial | 92 |
| Second syllable | 16 |
| Third syllable | 1 |
| Antepenultimate | 12 |
| Penultimate | 110 |
| Ultimate | 51 |

Sources:

- https://wals.info/chapter/14
- https://wals.info/feature/14A

Initial stress is therefore a real and relatively common pattern, but it is not dominant enough to justify treating it as an international identity constraint. Penultimate stress is even more frequent among the fixed-stress categories, while many languages in the sample have no fixed stress pattern at all.

For Tredecadia, the more portable identity is the deliberately simple five-syllable segmental sequence. Stress is consequently separated from lexical identity.

## Why retain an initial-stress citation form

A standard still benefits from one reproducible pronunciation for:

- dictionaries and documentation;
- teaching material;
- recorded examples;
- text-to-speech test fixtures;
- cross-language discussion where no localization profile has been selected.

Initial stress was retained for this **citation** role because it is simple to teach, immediately locatable from the left edge, and already present in the project’s earlier draft pronunciations. Retaining it as a reference realization avoids unnecessary churn while removing the stronger and unjustified requirement that every natural pronunciation must use it.

## Segmental versus citation notation

Tredecadia now distinguishes two representations:

- `/ma.sa.nu.mi.ka/` — the broad segmental/phonemic sequence relevant to canonical identity;
- `[ˈma.sa.nu.mi.ka]` — the Tredecadia citation realization, including reference initial stress.

The International Phonetic Association distinguishes broad/phonemic transcription, conventionally written between slashes, from phonetic transcription, conventionally written in square brackets when phonetic detail is represented. See the IPA’s transcription guidance and Handbook resources:

- https://www.internationalphoneticassociation.org/sites/default/files/ipaexam/Writing_a_phonemic_transcription_2015.pdf
- https://www.internationalphoneticassociation.org/content/handbook-ipa

The Tredecadia bracketed citation form is intentionally broad: it specifies the reference stress location without attempting to prescribe language-specific allophonic detail.

## Localization consequence

Localized speech may follow the target language’s natural stress, rhythm, pitch-accent system, and predictable allophony. This is especially important because some languages use stress very differently from the citation model and some speech systems do not map neatly onto a fixed lexical-stress requirement.

The adaptation boundary is segmental identity: localization should preserve the five syllables and their consonant/vowel sequence as closely as the language permits. When a target language lacks an exact canonical contrast, the localization profile should document the approximation rather than silently alter the canonical inventory.

## Registry design

Draft 0.3 makes the distinction machine-readable:

- `pronunciation.identity = "ordered-segmental-syllables"`;
- `pronunciation.stressIdentityCritical = false`;
- `pronunciation.citationStress = "initial"`;
- `pronunciation.syllableIpa` records the canonical segmental inventory;
- each month stores `citationIpa` rather than the ambiguous old field name `ipa`.

The month-registry schema is therefore advanced from schema version 1 to schema version 2 during the pre-1.0 period.
