# Tredecadia

[English](README.md) · **繁體中文** · [所有語言](README.languages.md)

Tredecadia 是一套開放的永久曆方案：一年分成 **13 個月，每月 28 天**。每個月剛好四週，同一個月日永遠落在同一個星期幾；用來補足太陽年的額外日則獨立於月份與七日星期週期之外。

> **目前公開版本：`1.0.0-rc.1`。** 這是正式版 `v1.0.0` 之前的候選版本。v1 的相容性邊界已經凍結，但最終版仍會經過一段觀察與驗證期後才發布。

## 基本結構

- 13 × 28 = 364 個一般月內日。
- 每個月都是完整的四週。
- 每月 `01` 日固定是星期一，`28` 日固定是星期日。
- `EQ`（**春分／新年日**）開啟新的一年，不屬於任何月份，也不屬於星期週期。
- 閏年在 `13-28` 之後增加 `ED`（**地球日**），之後才進入下一年的 `EQ`。

平年：

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

閏年：

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia 紀年

Tredecadia 採用單一連續的整數年份軸，並且有真正的 **0 年**。因此系統內部不需要把年份分成兩套紀元。

英文縮寫 **BCE/CE** 分別來自 **Before Common Era / Common Era**，中文可理解為 **公元前／公元（共同紀元）**。

數學原點是：

`TE 00000-EQ ↔ 格里高利曆天文紀年 -9999 年 3 月 20 日`

依一般歷史寫法，這相當於 **公元前 10000 年（`10000 BCE`）**。這個原點並不宣稱是人類、文明、農業或任何歷史階段的「起點」；它只是 Tredecadia 年份座標的數學零點。

民用換算關係：

`TE 年 = 格里高利曆天文年份 + 9999`

所以公元 2026 年對應 **TE 12025**。

## 日期格式

標準交換格式使用嚴格 ASCII，年份至少五位：

`12025-07-11` · `00000-EQ` · `-00001-01-01`

面向使用者的介面可以省略前導零，也可以在負年份中使用排版上的真正負號。這些只是顯示方式，不是另一套標準識別格式。

## 月份

月份名稱本身是國際化的標準識別符。目前還沒有經過審核的繁體中文漢字轉寫方案，因此這裡**刻意保留標準拉丁字母寫法**，而不是自行創造中文譯名。

| # | 完整名稱 | 三音節短式 (`Short-6`) | 兩音節口語短式 (`Short-4`) |
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

在口語中，如果語境已經清楚是在談月份，優先使用兩音節短式。參考發音採用**第一音節輕微突出**的方式；重音位置不是月份名稱身分的一部分。

## 規範與程式碼

Python 參考轉換器位於 [`reference/python/tredecadia.py`](reference/python/tredecadia.py)。規範性文件在 [`specification/`](specification/)，機器可讀登錄資料在 [`registry/`](registry/)。

這份 README 是面向繁體中文讀者的介紹，不取代正式規範。

## 授權

文件、規範與資料採用 **CC BY 4.0**；程式碼與腳本預設採用 **MIT**。詳見 [`LICENSE.md`](LICENSE.md)。
