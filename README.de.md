# Tredecadia

[English](README.md) · **Deutsch** · [Alle Sprachen](README.languages.md)

Tredecadia ist ein offener Entwurf für einen immerwährenden Kalender mit **13 Monaten zu je 28 Tagen**. Jeder Monat besteht aus genau vier vollständigen Wochen, ein bestimmtes Monatsdatum fällt immer auf denselben Wochentag, und die zusätzlichen Ausgleichstage des Jahres liegen außerhalb von Monaten und Wochenzyklus.

> **Aktuelle öffentliche Version: `1.1.0-rc.1`.**

## Grundidee

- 13 × 28 = 364 reguläre Monatstage.
- Jeder Monat hat genau vier volle Wochen.
- Der `01` ist immer **Mene (`W1`)**, der `28` immer **Toze (`W7`)**.
- `EQ` — **Tag der Tagundnachtgleiche / Neujahr** — eröffnet jedes Jahr und gehört weder zu einem Monat noch zur Woche.
- In Schaltjahren kommt nach `13-28` zusätzlich `ED` — **Tag der Erde** — bevor das nächste `EQ` beginnt.

Kanonischer Sieben-Tage-Zyklus:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Diese Namen sind kanonische Tredecadia-Identifikatoren, keine Übersetzungen oder Umbenennungen von Montag bis Sonntag. RC2 enthält noch keine geprüften lokalisierten Aliasnamen für Wochentage; deshalb werden die kanonischen lateinischen Formen verwendet.

Normales Jahr:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Schaltjahr:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia-Ära

Tredecadia verwendet eine durchgehende ganzzahlige Jahresachse mit einem echten **Jahr 0**. Deshalb muss die interne Jahreszählung nicht in zwei Epochen aufgeteilt werden.

Die englischen Kürzel **BCE/CE** stehen für **Before Common Era / Common Era**, sinngemäß „vor der gemeinsamen Zeitrechnung / gemeinsame Zeitrechnung“.

Mathematischer Ursprung:

`TE 00000-EQ ↔ astronomisches gregorianisches Jahr -9999, 20. März`

In üblicher historischer Schreibweise entspricht das **10000 vor der gemeinsamen Zeitrechnung (`10000 BCE`)**. Dieser Nullpunkt soll weder den Beginn der Menschheit noch der Zivilisation oder irgendeines historischen Prozesses markieren; er ist ausschließlich der mathematische Ursprung der Jahreskoordinate.

Für die zivile Umrechnung gilt:

`TE-Jahr = astronomisches gregorianisches Jahr + 9999`

Damit entspricht das Jahr 2026 der gemeinsamen Zeitrechnung dem Jahr **TE 12025**.

## Datumsformat

Das kanonische Austauschformat verwendet striktes ASCII und mindestens fünf Stellen für das Jahr:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Benutzeroberflächen dürfen führende Nullen weglassen und bei negativen Jahren ein typografisches Minus verwenden. Das sind Darstellungsformen, keine alternativen kanonischen Bezeichner.

## Monate

Die Monatsnamen sind internationale Identifikatoren. Im Deutschen bleibt ihre kanonische lateinische Schreibweise erhalten.

| # | Voller Name | 3-Silben-Kurzform (`Short-6`) | 2-Silben-Sprechform (`Short-4`) |
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

Im Gespräch ist die zweisilbige Form die bevorzugte Kurzform, sobald aus dem Kontext klar ist, dass ein Monat gemeint ist. Die Referenzaussprache hat **eine leichte Hervorhebung der ersten Silbe**; Betonung ist nicht Teil der Namensidentität.

## Spezifikation und Code

Der Python-Referenzkonverter liegt unter [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Normative Texte befinden sich in [`specification/`](specification/), maschinenlesbare Register in [`registry/`](registry/).

Dieses README ist als deutschsprachige Einführung gedacht und ersetzt nicht die normative Spezifikation.

## Lizenzen

Dokumentation, Spezifikationen und Daten: **CC BY 4.0**. Code und Skripte: **MIT**, sofern nicht anders angegeben. Siehe [`LICENSE.md`](LICENSE.md).
