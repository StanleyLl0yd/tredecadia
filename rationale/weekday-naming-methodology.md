# Weekday Naming Methodology — RC2 Candidate

Status: **non-normative candidate research**

This document records the search that selected a proposed internationally neutral weekday vocabulary for a second v1 release candidate. It does **not** change the published `v1.0.0-rc.1` vocabulary by itself. Until an explicit RC2 transition is merged and published, the normative RC1 weekday names remain Monday through Sunday.

The machine-readable research snapshot is [`release/weekday-rc2-candidate.json`](../release/weekday-rc2-candidate.json).

## Goal

Tredecadia already uses internationally neutral canonical month names. The RC2 weekday search applies the same principle to the seven regular weekdays while keeping them visually and phonetically distinct from the month Short-4 forms.

The proposed machine identities are `W1` through `W7`. Human-readable weekday names are four ASCII letters and two open CV syllables.

## Structural model

A weekday candidate has shape `CVCV`.

Consonants reuse the seven onsets already proven usable by the month system:

`M N S T Y K Z`

The weekday-only vowel inventory is:

`E O`

This intentionally separates weekday syllables from the canonical month vowel inventory `A I U`.

The resulting weekday syllable inventory is:

`ME MO NE NO SE SO TE TO YE YO KE KO ZE ZO`

For the selected seven-name set:

- every initial consonant is used exactly once;
- every second consonant is used exactly once;
- a name does not repeat its consonant onset;
- every one of the 14 `E/O` CV syllables is used exactly once;
- every weekday is at character Hamming distance at least `3/4` from every canonical month Short-4;
- every weekday is also at Levenshtein distance at least `3` from every canonical month Short-4.

The month Short-4 reference set is loaded from `registry/months.json`, not duplicated as an independent normative list.

## Exact separation bound

With only `E/O`, a four-letter `CVCV` name has one of four vowel-position patterns:

`EE EO OE OO`

Seven names placed into four patterns force at least three pairs to share the same vowel pattern: the most even distribution is `2,2,2,1`, which contributes exactly three same-pattern pairs.

Because the selected construction uses distinct first consonants and distinct second consonants, two names sharing a vowel pattern differ in exactly their two consonant positions. Their Hamming distance is therefore `2/4`.

So a global weekday minimum of `3/4` is impossible under the clean two-vowel model. The selected set reaches the lower bound exactly:

- distance 2: **3 pairs**;
- distance 3: **12 pairs**;
- distance 4: **6 pairs**.

The three unavoidable distance-2 pairs are kept non-adjacent in the actual weekly cycle.

## Selected RC2 candidate

| ID | Name | Syllables | Citation IPA |
|---|---|---|---|
| W1 | **Mene** | ME NE | `/ˈme.ne/` |
| W2 | **Noko** | NO KO | `/ˈno.ko/` |
| W3 | **Kese** | KE SE | `/ˈke.se/` |
| W4 | **Zoyo** | ZO YO | `/ˈzo.jo/` |
| W5 | **Sote** | SO TE | `/ˈso.te/` |
| W6 | **Yemo** | YE MO | `/ˈje.mo/` |
| W7 | **Toze** | TO ZE | `/ˈto.ze/` |

The proposed cycle is therefore:

`Mene → Noko → Kese → Zoyo → Sote → Yemo → Toze → Mene`

Adjacent character-Hamming distances are:

`4, 4, 4, 3, 4, 4, 3`

Thus all adjacent weekdays differ in at least three of four positions, five of the seven transitions differ in all four positions, and none of the unavoidable distance-2 pairs is adjacent.

The unavoidable non-adjacent pairs are:

- `Mene / Kese`;
- `Noko / Zoyo`;
- `Sote / Toze`.

## Semantic clearance policy

The same practical policy used for month naming is retained:

- **BLOCK** — a substantial international negative, unsafe, vulgar, or otherwise unsuitable exact collision;
- **SOFT** — a neutral ordinary word, name, place, brand, or other tolerable coincidence;
- **IGNORE** — an obscure, archaic, reconstructed, materially different, or otherwise insignificant coincidence.

The goal is not impossible worldwide lexical uniqueness. Neutral natural-language words remain acceptable; the search removes material adverse collisions.

### Selected-form review

The selected names have no material BLOCK found in the clearance pass. Known exact coincidences are neutral or sufficiently weak:

- `Mene` is an ordinary neutral Nordic verb/form associated with thinking or meaning; see the Norwegian dictionary search at <https://ordbokene.no/eng/bm%2Cnn/mene>.
- `Noko` is an ordinary Norwegian Nynorsk determiner/pronoun/adverb with senses including “some” and “something”; see <https://en.wiktionary.org/wiki/noko> and its cited Nynorsk dictionary source.
- `Kese` has neutral natural-language senses including Turkish bag/sack-type meanings; see <https://en.wiktionary.org/wiki/kese>.
- `Zoyo` occurs as a rare surname and as commercial naming; see <https://forebears.io/surnames/zoyo>. This is a tolerable onomastic/commercial coincidence, not a reserved lexical claim.
- `Sote` is used in Finnish for social-and-health services and has other neutral language senses; see <https://en.wiktionary.org/wiki/sote>.
- `Yemo` produced no material modern exact negative collision in the reviewed search; obscure reconstructed/proper-name material is classified IGNORE.
- `Toze` is an obsolete English verb associated with teasing/card-combing wool; see <https://www.collinsdictionary.com/dictionary/english/toze>. Archaic material does not by itself block an internationally neutral identifier.

These classifications describe the evidence found during the search and are not claims that the strings are absent from every language, name database, trademark registry, or future corpus.

### Material cuts encountered

The cutting-plane search rejected exact forms only when an optimum candidate exposed a substantial issue. Examples include:

| Form | Reason for BLOCK | Evidence |
|---|---|---|
| `MONE` | Italian exact form includes a vulgar anatomical sense | <https://en.wiktionary.org/wiki/mone> |
| `MEZO` | Breton exact adjective meaning “drunk” | <https://en.wiktionary.org/wiki/mezo> |
| `NOYO` | Shoshoni dictionary exact form includes “testicle” | <https://shoshoniproject.utah.edu/language-materials/shoshoni-dictionary/dictionary.php?filter=N> |
| `SEKO` | Finnish slang includes “nutcase/loon” senses | <https://en.wiktionary.org/wiki/seko> |
| `SEMO` | Venetan exact adjective “stupid/foolish” | <https://en.wiktionary.org/wiki/semo> |
| `ZOTE` | Spanish insult “fool/stupid person”; German also has an obscene-joke noun | <https://en.wiktionary.org/wiki/zote>, <https://www.duden.de/rechtschreibung/Zote> |
| `KEMO` | Danish informal abbreviation for chemotherapy | <https://ordnet.dk/ddo/ordbog/kemo> |
| `KENE` | Turkish exact word for “tick” | <https://en.wiktionary.org/wiki/kene> |
| `KOTE` | German inflected form associated with `Kot` (“feces”) | <https://en.wiktionary.org/wiki/kote> |
| `SOYO` | Korean romanized `소요`, including disorder/riot legal usage | <https://www.korean.go.kr/front/onlineQna/onlineQnaView.do?pageIndex=1&qna_seq=332007> |

The block list is a search ledger, not a general blacklist of natural languages.

## Why not add `A` to the weekday vowels?

A three-vowel `A/E/O` search can eliminate the unavoidable weekday distance-2 pairs, but doing so requires at least three `A` vowel slots in the seven-name set. That weakens the clean category-level distinction between weekday names (`E/O`) and month names (`A/I/U`).

The two-vowel construction therefore deliberately accepts three mathematically unavoidable, non-adjacent distance-2 weekday pairs in exchange for:

- a disjoint weekday/month vowel inventory;
- exact use of all 14 weekday syllables once each;
- minimum distance 3 from every month Short-4;
- an optimized weekly cycle with no close pair adjacent.

## Compatibility consequence

`v1.0.0-rc.1` already froze Monday through Sunday in the intended v1 compatibility surface. Replacing those names is therefore an explicit compatibility-critical RC correction, not an editorial rename.

If this candidate is accepted into the normative registry:

1. the published RC1 tag, release, archive, checksum, and historical identity record remain immutable;
2. Tredecadia publishes a new `v1.0.0-rc.2` rather than silently rewriting RC1;
3. the calendar registry/schema contract changes and the calendar schema version must advance from `1` to `2`;
4. the RC2 identity record freezes `W1..W7`, their order, canonical spellings, and two-syllable segmental identities;
5. stable `v1.0.0` can follow only after the RC2 observation gate completes without a blocking defect.

Localization aliases for the new weekday inventory are a separate review surface. This candidate does not silently extend the already reviewed month localization profiles with unreviewed `E/O` mappings.
