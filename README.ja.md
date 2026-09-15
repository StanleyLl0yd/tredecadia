# Tredecadia

[English](README.md) · **日本語** · [すべての言語](README.languages.md)

Tredecadia は、**1年を28日×13か月**で構成するオープンな永久暦プロジェクトです。すべての月がちょうど4週間なので、同じ日付は毎年同じ曜日になります。年の長さを調整する日は、月にも7日周期の週にも属しません。

> **現在の公開版は `1.0.0-rc.1` です。** v1 の互換性範囲はすでに凍結されていますが、正式な `v1.0.0` の前に実際の利用とフィードバックを確認する観察期間を設けています。

## 基本構造

- 13 × 28 = 月に属する通常日が364日。
- 1か月は常に4週間ちょうどです。
- 各月の `01` は必ず月曜日、`28` は必ず日曜日です。
- `EQ`（Equinox / New Year Day、春分・新年の日）が年の最初に置かれ、月にも週にも属しません。
- うるう年には `13-28` の後に `ED`（Earth Day、地球の日）が入り、その次に翌年の `EQ` が来ます。

通常年：

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

うるう年：

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia の年は、**0年を含む1本の整数軸**で数えます。暦の内部では BCE/CE のように紀元前と紀元後を分ける必要がありません。

数学上の原点は次のとおりです。

`TE 00000-EQ ↔ グレゴリオ暦の天文学的年番号 -9999年 3月20日`

一般的な表現ではおおむね **10000 BCE** に相当します。ただし、これを人類や文明の「始まり」とみなすわけではありません。あくまで Tredecadia の年座標を定義する数学的なゼロ点です。

民用変換では：

`TE年 = グレゴリオ暦の天文学的年番号 + 9999`

したがって 2026年は **TE 12025** です。

## 日付表記

機械交換用の正規形式は厳密な ASCII で、年は最低5桁です。

`12025-07-11` · `00000-EQ` · `-00001-01-01`

画面表示では先頭のゼロを省いたり、組版用のマイナス記号を使ったりできます。これは見せ方の違いであり、別の正規形式ではありません。

## 月名

| # | 正式名 | Short-6 | Short-4 |
|---:|---|---|---|
| 01 | Masanumika | Masanu | Masa |
| 02 | Tasuzunumu | Tasuzu | Tasu |
| 03 | Nazumasanu | Nazuma | Nazu |
| 04 | Mikasumani | Mikasu | Mika |
| 05 | Yanimuzunu | Yanimu | Yani |
| 06 | Zumitanasu | Zumita | Zumi |
| 07 | Muyasanumi | Muyasa | Muya |
| 08 | Sunizusaka | Sunizu | Suni |
| 09 | Numanamuta | Numana | Numa |
| 10 | Kazunusuya | Kazunu | Kazu |
| 11 | Yanazumasa | Yanazu | Yana |
| 12 | Sanumikazu | Sanumi | Sanu |
| 13 | Nimutazuna | Nimuta | Nimu |

会話では、月の話だと分かっている場面なら4文字の Short-4 を優先します。基準発音では**第1音節を弱く目立たせる**程度で、アクセント位置そのものは月名の識別条件ではありません。

## 仕様とコード

Python の参照変換器は [`reference/python/tredecadia.py`](reference/python/tredecadia.py) にあります。規範文書は [`specification/`](specification/)、機械可読レジストリは [`registry/`](registry/) です。

この日本語 README は、日本語として自然に読める導入文として書かれており、英語版の逐語訳ではありません。規範上の判断は正式な仕様を参照してください。

## ライセンス

文書・仕様・データは **CC BY 4.0**、コードとスクリプトは特記がない限り **MIT** です。詳しくは [`LICENSE.md`](LICENSE.md) を参照してください。
