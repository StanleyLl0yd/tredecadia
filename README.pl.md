# Tredecadia

[English](README.md) · **Polski** · [Wszystkie języki](README.languages.md)

Tredecadia to otwarty projekt kalendarza wiecznego z **13 miesiącami po 28 dni**. Każdy miesiąc ma dokładnie cztery pełne tygodnie, ta sama data zawsze przypada na ten sam dzień tygodnia, a dni korygujące długość roku znajdują się poza miesiącami i poza siedmiodniowym tygodniem.

> **Aktualna wersja publiczna: `1.0.0-rc.1`.** To release candidate: zakres zgodności v1 jest już zamrożony, ale przed wydaniem `v1.0.0` trwa jeszcze okres obserwacji i zbierania uwag.

## Zasada działania

- 13 × 28 = 364 zwykłe dni w miesiącach.
- Każdy miesiąc to cztery pełne tygodnie.
- Dzień `01` zawsze wypada w poniedziałek, a `28` w niedzielę.
- `EQ` — Dzień Równonocy / Nowy Rok — otwiera rok i nie należy ani do miesiąca, ani do tygodnia.
- W roku przestępnym po `13-28` występuje dodatkowo `ED` — Dzień Ziemi — a dopiero potem rozpoczyna się kolejne `EQ`.

Rok zwykły:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Rok przestępny:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia używa jednej ciągłej osi całkowitoliczbowej z prawdziwym **rokiem 0**. W samym kalendarzu nie ma potrzeby rozdzielania czasu na BCE/CE.

Początek matematyczny:

`TE 00000-EQ ↔ astronomiczny rok gregoriański -9999, 20 marca`

Odpowiada to temu, co zwykle zapisuje się jako **10000 BCE**. Nie jest to deklaracja początku ludzkości, cywilizacji ani żadnego procesu historycznego — wyłącznie matematyczne zero współrzędnej lat Tredecadia.

Dla konwersji cywilnej:

`rok TE = astronomiczny rok gregoriański + 9999`

Dlatego rok 2026 odpowiada **TE 12025**.

## Zapis dat

Kanonicalny format wymiany używa wyłącznie ASCII i co najmniej pięciu cyfr w polu roku:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

W interfejsach dla ludzi można ukrywać zera wiodące i stosować typograficzny znak minus. To sposób prezentacji, a nie alternatywny identyfikator.

## Miesiące

| # | Nazwa | Short-6 | Short-4 |
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

W mowie preferowana jest forma czteroliterowa, jeśli z kontekstu wiadomo już, że chodzi o miesiąc. Wymowa referencyjna ma **lekkie uwydatnienie pierwszej sylaby**; akcent nie jest częścią tożsamości nazwy.

## Specyfikacja i kod

Referencyjny konwerter Python znajduje się w [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Dokumenty normatywne są w [`specification/`](specification/), a rejestry maszynowe w [`registry/`](registry/).

Ten polski README ma być naturalnym wprowadzeniem dla czytelnika i nie zastępuje specyfikacji normatywnej.

## Licencje

Dokumentacja, specyfikacje i dane: **CC BY 4.0**. Kod i skrypty: **MIT**, o ile nie zaznaczono inaczej. Zobacz [`LICENSE.md`](LICENSE.md).
