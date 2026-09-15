# Tredecadia Localization

Status: **Draft 0.3**

Localization must preserve the identity of each canonical month while allowing natural presentation in local writing systems and speech communities.

## 1. Canonical source form

The canonical Latin form defined by the Month Naming Standard is the stable identifier. Localized spellings are aliases, not independent month identifiers.

A localization should preserve:

- the five-syllable order;
- the intended consonant/vowel sequence as closely as the target language allows;
- one-to-one mapping back to the canonical month number and Latin name.

A localization MUST NOT silently redefine the canonical Latin spelling, month number, or ordered syllable sequence.

## 2. Pronunciation adaptation

Tredecadia distinguishes canonical **segmental identity** from a **citation pronunciation**.

The ordered CV syllables are identity-critical. Tredecadia's citation pronunciation uses **weak initial prominence** on the first syllable, but stress placement or strength is not part of month identity.

A localized spoken form MAY use the stress placement, rhythm, pitch-accent behavior, vowel reduction, and predictable allophony natural to the target language. A difference in stress placement or strength alone MUST NOT create a different month identity.

Full, Short-6, and Short-4 forms inherit the same initial reference-prominence location because every abbreviation is a complete-syllable prefix of the full form. Localization SHOULD preserve that reference pattern when natural, but MAY adapt prosody when the target language strongly favors another realization.

A localization profile SHOULD document systematic approximations when the target language lacks a canonical sound or contrast. Such approximations are properties of the localized profile, not changes to the canonical pronunciation inventory.

For example, canonical `YA` remains /ja/ and canonical `ZU` remains /zu/ even where a target language uses its nearest conventional sequence rather than those exact phonetic values.

## 3. Russian Cyrillic profile

Draft 0.3 registers the following Russian display forms:

| # | Canonical | Russian |
|---:|---|---|
| 01 | Masanumika | Масанумика |
| 02 | Tasuzunumu | Тасузунуму |
| 03 | Nazumasanu | Назумасану |
| 04 | Mikasumani | Микасумани |
| 05 | Yanimuzunu | Янимузуну |
| 06 | Zumitanasu | Зумитанасу |
| 07 | Muyasanumi | Муясануми |
| 08 | Sunizusaka | Сунизусака |
| 09 | Numanamuta | Нуманамута |
| 10 | Kazunusuya | Казунусуя |
| 11 | Yanazumasa | Яназумаса |
| 12 | Sanumikazu | Санумиказу |
| 13 | Nimutazuna | Нимутазуна |

The Russian display profile maps canonical `YA /ja/` to `Я/я` and `ZU /zu/` to `ЗУ/зу`.

The Russian profile does not impose the citation prominence as a lexical requirement; ordinary Russian prosodic realization may adapt stress while preserving the recognizable segmental sequence.

## 4. Profile maturity

Additional script/language profiles should be reviewed independently by competent speakers/readers or strong orthographic references before being marked stable.

Unreviewed transliterations SHOULD be recorded as candidates outside the canonical registry rather than presented as normative aliases.

A future registry revision may add reviewed script/language aliases without changing canonical month identifiers.
