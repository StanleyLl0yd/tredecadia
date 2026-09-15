# Short-4 Conversational and UX Review

This document is non-normative. Normative naming and pronunciation rules live in `specification/month-naming-standard.md`.

## Purpose

Tredecadia's four-letter month forms are deliberately short enough for ordinary speech, compact UI labels, reminders, and date entry. Short-4 is therefore reviewed as a user-facing vocabulary rather than only as a mathematical prefix set.

The review separates three questions:

1. **canonical identity** — does an exact Short-4 token map to exactly one month?;
2. **near-neighbour recognition** — can a typo or uncertain speech recognizer confuse two Tredecadia Short-4 forms?;
3. **ordinary-language collision** — does the same four-letter string already occur as a word, name, place, or romanization somewhere in the world?

Only the first question is a hard interoperability requirement. Near-neighbour recognition is mitigated by UI/voice behavior. Ordinary neutral lexical/name collisions are expected for two-syllable four-letter strings and are not by themselves reasons to rename a month.

## Exact identity

All 13 Short-4 forms are case-insensitively unique:

`Masa Tasu Nazu Mika Yani Zumi Muya Suni Numa Kazu Yana Sanu Nimu`

An exact Short-4 token in an established Tredecadia-month context therefore maps deterministically to one month.

## Structural near neighbours

Two pairs have character Levenshtein distance 1:

- `Nazu` / `Kazu`;
- `Yani` / `Yana`.

At the two-syllable level, three pairs have positional syllable Hamming distance 1:

- `Nazu` / `Kazu` (`NA-ZU` / `KA-ZU`);
- `Yani` / `Yana` (`YA-NI` / `YA-NA`);
- `Yani` / `Suni` (`YA-NI` / `SU-NI`).

The third pair is worth recording separately: it is not a one-character neighbour, but in speech only the first syllable distinguishes the two forms.

These pairs are not failures of the naming system. They define the cases where fuzzy text matching or low-confidence speech recognition must not silently guess.

## Recognition policy

Recommended implementation behavior:

- exact, case-insensitive Short-4 matching in a month field MAY resolve immediately;
- Short-4 SHOULD NOT be used as an unrestricted natural-language keyword outside a month/date context;
- fuzzy matching MUST NOT silently auto-correct one valid Short-4 into another valid Short-4;
- when an input is compatible with more than one close Tredecadia form, the interface SHOULD ask for confirmation or show the candidate months;
- voice interfaces SHOULD retain surrounding date/month context and SHOULD disambiguate low-confidence close pairs rather than relying only on acoustic nearest-neighbour selection;
- machine storage SHOULD use the month number or canonical full name rather than storing a locale-dependent recognition guess.

Examples of safe compact contexts include a month picker, a calendar header, `14 Masa`, or a voice command whose grammar already expects a Tredecadia month. A naked `Masa` in unrestricted prose is intentionally not required to mean the Tredecadia month.

## Abbreviation-stable prosody

The weak initial citation prominence selected in Draft 0.3 is stable under shortening because Full, Short-6, and Short-4 share the same first syllable.

For example:

- `Masanumika` → `[ˈma.sa.nu.mi.ka]`;
- `Masanu` → `[ˈma.sa.nu]`;
- `Masa` → `[ˈma.sa]`.

No canonical abbreviation requires prominence to move to a different syllable.

## Lexical collision spot-check

A non-exhaustive international spot-check confirms that several Short-4 strings already exist as ordinary words, names, language names, or romanizations. Examples include:

- `Masa`: the established culinary term *masa* in English and Spanish;
- `Tasu`: Korean romanization `tasu` for terms including an official at-bat/stroke count, and a Kadazandusun noun for “dog”;
- `Nazu`: a Judeo-Tat noun recorded for “cat”;
- `Mika`: an established Finnish given name;
- `Yani`: an established personal name/romanization in several languages;
- `Zumi`: an Esperanto verb “to hum/buzz” and a Romani noun “soup/broth”;
- `Muya`: the name of a Sino-Tibetan language;
- `Suni`: ordinary lexical/name uses in multiple languages, including an English zoological term and Georgian `სუნი` “smell/odour”;
- `Numa`: an established historical personal name and other proper-name uses;
- `Kazu`: a Japanese name/romanization and lexical uses in other languages;
- `Yana`: an established personal/language name;
- `Sanu`: established personal-name and lexical uses;
- `Nimu`: lexical uses including Dungan and Lisu attestations.

This is expected. A globally collision-free four-letter CV vocabulary is not a realistic requirement. The relevant screening question is whether a collision is substantially harmful or internationally disqualifying; the examples above are ordinary neutral or context-dependent uses and do not meet that threshold.

Sources used for this spot-check include Cambridge Dictionary (`masa`), Store norske leksikon / Behind the Name (`Mika`), Wiktionary entries for `tasu`, `nazu`, `zumi`, `suni`, and `kazu`, and general language/name reference pages for Muya, Yani, Numa, Sanu, and Nimu. This evidence is descriptive and non-normative; it is not a promise that no additional lexical coincidence exists.

## UI guidance

### Calendar and date UI

Short-4 is appropriate where the visual structure already establishes month semantics:

- compact month headers;
- month selectors;
- date chips;
- reminder summaries;
- narrow mobile layouts.

Short-6 or the full name is preferable in onboarding, documentation, first-use screens, and contexts where a four-letter token could be mistaken for ordinary prose.

### Search and fuzzy entry

Exact Short-4 entry is safe because the set is unique. Fuzzy entry should be conservative:

- do not autocorrect `Nazu` to `Kazu` or vice versa;
- do not autocorrect `Yani` to `Yana` or vice versa;
- speech recognizers should also treat `Yani` / `Suni` as a known acoustic-risk pair;
- if multiple valid months remain plausible, request disambiguation.

### Accessibility

Assistive labels SHOULD add month semantics when a Short-4 token appears without sufficient surrounding structure. For example, an implementation may expose an accessible label equivalent to “Masa, month 1” while displaying only `Masa` visually.

Screen readers and synthesized speech should use the pronunciation profile rather than spelling the four letters individually unless the user explicitly requests spelling.

## Conclusion

Short-4 remains suitable as Tredecadia's preferred conversational compact form. The review found no substantial reason to reopen any canonical month name. The main implementation requirement is conservative handling of known close pairs in fuzzy text and speech recognition.
