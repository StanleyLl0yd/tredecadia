# Japanese Katakana Profile Review

This document records the evidence used to promote `ja-Kana` from `candidate` to `reviewed`. It does not make the profile stable.

## External reference

The primary reference is Japan's Agency for Cultural Affairs (`文化庁`) publication **外来語の表記**, adopted by Cabinet Notification No. 2 on 1991-06-28 as guidance for representing foreign words and foreign place/person names in modern Japanese.

Primary pages:

- https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/
- https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/honbun01.html
- https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/honbun02.html

The guidance states that its first kana table contains forms generally used for foreign words and foreign place/person names, while additional forms may be used when trying to approach the source sound or spelling more closely. It also explicitly permits established usage and acknowledges that exact source sounds need not always be preserved.

## Tredecadia mapping

Tredecadia uses only basic open CV sequences that have straightforward Katakana representations in this profile:

`MA マ · MI ミ · MU ム · NA ナ · NI ニ · NU ヌ · SA サ · SU ス · TA タ · YA ヤ · KA カ · ZU ズ`

The profile intentionally does not introduce extended foreign-sound kana because the canonical inventory does not require them.

## Approximation boundary

The mapping is orthographically conventional but not phonetically identical to every Tredecadia canonical IPA value. In particular:

- Japanese `ウ`-series vowels are not required to equal canonical /u/ phonetically;
- `ズ` is the conventional profile representation of canonical `ZU /zu/`, while actual Japanese realization may include language-specific allophony.

These are localization approximations, not changes to canonical Tredecadia segmental identity.

## Result

All 13 Full, Short-6, and Short-4 aliases are deterministically generated from the profile syllable map and remain unique within `ja-Kana`. CI verifies those properties.

The official Japanese orthographic guidance is sufficient independent standards evidence for `reviewed` status. The profile is not marked `stable`, and this review does not claim a separate native-speaker usability evaluation.
