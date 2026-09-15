# Tredecadia Month Naming Standard

Status: **Draft 0.1**

This document defines the canonical names, pronunciation model, and standard abbreviations of Tredecadia's 13 regular months.

## Canonical syllables

`MA MI MU NA NI NU SA SU TA YA KA ZU`

Each canonical month name contains exactly five open CV syllables. Canonical values are `MA /ma/`, `MI /mi/`, `MU /mu/`, `NA /na/`, `NI /ni/`, `NU /nu/`, `SA /sa/`, `SU /su/`, `TA /ta/`, `YA /ja/`, `KA /ka/`, and `ZU /zu/`. Canonical stress is on the first syllable.

## Canonical months

| # | Name | Syllables | IPA | Short-6 | Short-4 |
|---:|---|---|---|---|---|
| 01 | Masanumika | MA-SA-NU-MI-KA | /ˈma.sa.nu.mi.ka/ | Masanu | Masa |
| 02 | Tasuzunumu | TA-SU-ZU-NU-MU | /ˈta.su.zu.nu.mu/ | Tasuzu | Tasu |
| 03 | Nazumasanu | NA-ZU-MA-SA-NU | /ˈna.zu.ma.sa.nu/ | Nazuma | Nazu |
| 04 | Mikasumani | MI-KA-SU-MA-NI | /ˈmi.ka.su.ma.ni/ | Mikasu | Mika |
| 05 | Yanimuzunu | YA-NI-MU-ZU-NU | /ˈja.ni.mu.zu.nu/ | Yanimu | Yani |
| 06 | Zumitanasu | ZU-MI-TA-NA-SU | /ˈzu.mi.ta.na.su/ | Zumita | Zumi |
| 07 | Muyasanumi | MU-YA-SA-NU-MI | /ˈmu.ja.sa.nu.mi/ | Muyasa | Muya |
| 08 | Sunizusaka | SU-NI-ZU-SA-KA | /ˈsu.ni.zu.sa.ka/ | Sunizu | Suni |
| 09 | Numanamuta | NU-MA-NA-MU-TA | /ˈnu.ma.na.mu.ta/ | Numana | Numa |
| 10 | Kazunusuya | KA-ZU-NU-SU-YA | /ˈka.zu.nu.su.ja/ | Kazunu | Kazu |
| 11 | Yanazumasa | YA-NA-ZU-MA-SA | /ˈja.na.zu.ma.sa/ | Yanazu | Yana |
| 12 | Sanumikazu | SA-NU-MI-KA-ZU | /ˈsa.nu.mi.ka.zu/ | Sanumi | Sanu |
| 13 | Nimutazuna | NI-MU-TA-ZU-NA | /ˈni.mu.ta.zu.na/ | Nimuta | Nimu |

The machine-readable registry is `registry/months.json`.

## Canonical spelling

Canonical names use ASCII Latin letters. Display spelling uses initial capital plus lower-case letters. Systems may compare canonical identifiers case-insensitively, but the letter sequence is fixed.

## Abbreviations

**Short-6** is the first three complete syllables. **Short-4** is the first two complete syllables. Both sets are unique across all 13 months.

Five-letter truncation is non-standard because it cuts a CV syllable boundary.

## Stability

After the first stable release, month number, canonical Latin name, syllable sequence, Short-6, and Short-4 are intended to be compatibility-critical.

## Design record (non-normative)

The full-name syllable-frequency vector is `MA=5, MI=5, MU=5, NA=5, NI=4, NU=8, SA=6, SU=5, TA=4, YA=4, KA=5, ZU=9`.

Full-name balance SSD is exactly `323/12` (approximately `26.9166666666667`), with sum of squared syllable counts `379`. Short-6 balance SSD is exactly `41/4` (`10.25`); Short-4 balance SSD is exactly `11/3` (approximately `3.66666666666667`).

The only Short-6 pair at Levenshtein distance 2 is `Yanimu` / `Yanazu`. The Short-4 pairs at distance 1 are `Nazu` / `Kazu` and `Yani` / `Yana`.
