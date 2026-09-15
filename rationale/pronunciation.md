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

Initial stress is common enough to serve as a simple citation convention, but it is not dominant enough to justify treating it as international lexical identity. The more portable identity is the deliberately simple ordered five-syllable segmental sequence.

## Why weak initial prominence

Tredecadia uses **weak initial prominence** for its citation pronunciation rather than a strongly accented first syllable.

This choice serves three design goals:

1. the location is trivial to derive from the left edge;
2. the full name, Short-6, and Short-4 all share that same first syllable, so shortening never changes the reference prominence;
3. keeping the prominence deliberately light reduces pressure to imitate a strong language-specific lexical stress pattern.

Short-4 is expected to be the most natural compact conversational form in contexts where the calendar is already understood. A rule that moved stress after shortening would therefore be particularly undesirable. Initial prominence avoids that completely.

The policy is Tredecadia's own convention. It is not normatively derived from the stress system of Georgian or any other natural language, even if weak-stress languages provide a useful intuitive analogy.

## Segmental versus citation notation

Tredecadia distinguishes two representations:

- `/ma.sa.nu.mi.ka/` — the broad segmental sequence relevant to canonical identity;
- `[ˈma.sa.nu.mi.ka]` — the Tredecadia citation realization with the reference prominence location marked on the first syllable.

The IPA stress mark records the **location** of reference prominence. It should not be read as a requirement for exaggerated stress strength. The citation transcription remains deliberately broad and does not attempt to prescribe language-specific phonetic detail.

## Abbreviation inheritance

The reference pattern is prefix-stable:

- full: `Masanumika` → `[ˈma.sa.nu.mi.ka]`;
- Short-6: `Masanu` → `[ˈma.sa.nu]`;
- Short-4: `Masa` → `[ˈma.sa]`.

The same derivation applies to every month because every abbreviation is a complete-syllable prefix of the full form.

## Localization consequence

Localized speech may follow the target language's natural stress, rhythm, pitch-accent system, and predictable allophony. A difference in stress placement or strength alone does not change month identity.

The adaptation boundary is segmental identity: localization should preserve the canonical syllables and their consonant/vowel sequence as closely as the language permits. When a target language lacks an exact canonical contrast, the localization profile should document the approximation rather than silently alter the canonical inventory.

## Registry design

Draft 0.3 makes the distinction machine-readable:

- `pronunciation.identity = "ordered-segmental-syllables"`;
- `pronunciation.stressIdentityCritical = false`;
- `pronunciation.citationProminence = "weak-initial"`;
- `pronunciation.abbreviationsInheritCitationProminence = true`;
- `pronunciation.syllableIpa` records the canonical segmental inventory;
- each month stores `citationIpa` rather than the ambiguous old field name `ipa`.

The month-registry schema is advanced from schema version 1 to schema version 2 during the pre-1.0 period.
