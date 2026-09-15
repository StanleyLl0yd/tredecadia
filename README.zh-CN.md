# Tredecadia

[English](README.md) · **简体中文** · [所有语言](README.languages.md)

Tredecadia 是一个开放的永久历方案：一年分为 **13 个月，每月 28 天**。每个月正好四周，同一个月日永远对应同一个星期几；用于补齐太阳年的附加日则独立于月份和七日星期周期。

> **当前公开版本：`1.0.0-rc.1`。** 这是候选发布版。v1 的兼容性边界已经冻结，但在发布最终 `v1.0.0` 之前仍会保留一段实际观察和反馈期。

## 基本结构

- 13 × 28 = 364 个常规月内日。
- 每个月都是完整的四周。
- 每月 `01` 日总是星期一，`28` 日总是星期日。
- `EQ`（春分／新年日）开启新的一年，不属于任何月份，也不属于星期周期。
- 闰年在 `13-28` 之后增加 `ED`（地球日），随后才进入下一年的 `EQ`。

平年：

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

闰年：

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia 纪年

Tredecadia 使用一条连续的整数年份轴，并且存在真正的 **0 年**。因此系统内部不需要 BCE/CE 这样的双向纪年分界。

数学原点为：

`TE 00000-EQ ↔ 格里高利历天文纪年 -9999 年 3 月 20 日`

这大致对应通常所说的 **10000 BCE**。这里并不声称它代表人类、文明、农业或某个历史时代的“开端”；它只是 Tredecadia 年份坐标的数学零点。

民用换算关系：

`TE 年 = 格里高利历天文年份 + 9999`

因此 2026 年对应 **TE 12025**。

## 日期格式

规范交换格式使用严格 ASCII，年份至少五位：

`12025-07-11` · `00000-EQ` · `-00001-01-01`

面向用户的界面可以省略前导零，也可以使用排版上的真正负号。这些只是显示方式，不是另一套规范标识符。

## 月份

| # | 名称 | Short-6 | Short-4 |
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

在口语中，如果语境已经明确是在说月份，优先使用四字母短名。参考发音采用**第一音节轻微突出**的方式；重音位置不属于月份名称的身份信息。

## 规范与代码

Python 参考转换器位于 [`reference/python/tredecadia.py`](reference/python/tredecadia.py)。规范性文档在 [`specification/`](specification/)，机器可读注册表在 [`registry/`](registry/)。

本中文 README 旨在自然地介绍项目，不是对英文逐句翻译，也不取代规范性文档。

## 许可证

文档、规范和数据使用 **CC BY 4.0**；代码和脚本默认使用 **MIT**。详情见 [`LICENSE.md`](LICENSE.md)。
