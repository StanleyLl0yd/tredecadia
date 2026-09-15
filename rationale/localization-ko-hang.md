# Korean Hangul Profile Review

This document records the standards evidence used for the `ko-Hang` localization profile. The profile is reviewed, not stable.

## External reference

The primary reference is the National Institute of Korean Language (`국립국어원`) **외래어 표기법**, Ministry of Culture Notice No. 2017-14.

Primary rule page:

https://www.korean.go.kr/kornorms/m/m_regltn.do?regltn_code=0003

The standard's IPA-to-Hangul table directly gives the mappings needed by Tredecadia:

- /m/ → ㅁ before a vowel;
- /n/ → ㄴ before a vowel;
- /s/ → ㅅ before a vowel;
- /t/ → ㅌ before a vowel;
- /k/ → ㅋ before a vowel;
- /z/ → ㅈ before a vowel;
- /a/ → 아;
- /i/ → 이;
- /u/ → 우.

Its semivowel rule further states that [j] combines with the following vowel into Korean sequences including [ja] → 야.

## Tredecadia mapping

Combining those official correspondences yields:

`MA 마 · MI 미 · MU 무 · NA 나 · NI 니 · NU 누 · SA 사 · SU 수 · TA 타 · YA 야 · KA 카 · ZU 주`

No ad-hoc letter choice is required for any of the 12 canonical syllables.

## Approximation boundary

Korean does not preserve every canonical Tredecadia phonetic detail. Most notably, the official foreign-word table represents source /z/ before a vowel with ㅈ, so canonical `ZU /zu/` is displayed as `주` in this profile. This is a Korean localization approximation and does not redefine canonical /z/ or /zu/.

Likewise, Korean stop and vowel realizations follow normal Korean phonetics; canonical Tredecadia IPA remains the source identity.

## Result

All 13 Full, Short-6, and Short-4 aliases are generated from the same reviewed syllable map and remain unique within `ko-Hang`. CI verifies derivation and reverse mapping.

Because the mapping follows a directly applicable official IPA-to-Hangul standard, `reviewed` status is justified. The profile remains non-stable while Tredecadia is pre-1.0.
