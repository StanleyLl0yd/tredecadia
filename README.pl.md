# Tredecadia

[English](README.md) · **Polski** · [Wszystkie języki](README.languages.md)

Tredecadia to otwarty projekt kalendarza wiecznego z **13 miesiącami po 28 dni**. Każdy miesiąc ma dokładnie cztery pełne tygodnie, ta sama data zawsze przypada na ten sam dzień tygodnia, a dni korygujące długość roku znajdują się poza miesiącami i poza siedmiodniowym tygodniem.

> **Aktualna wersja publiczna: `1.0.0-rc.2`.** Ten drugi kandydat do wydania wprowadza kanoniczne nazwy dni tygodnia zaprojektowane jako międzynarodowo neutralne. Stabilne `v1.0.0` może zostać opublikowane dopiero po osobnym okresie obserwacji RC2 i końcowej weryfikacji.

## Zasada działania

- 13 × 28 = 364 zwykłe dni w miesiącach.
- Każdy miesiąc to cztery pełne tygodnie.
- Dzień `01` zawsze ma nazwę **Mene (`W1`)**, a `28` — **Toze (`W7`)**.
- `EQ` — **Dzień Równonocy / Nowy Rok** — otwiera rok i nie należy ani do miesiąca, ani do tygodnia.
- W roku przestępnym po `13-28` występuje dodatkowo `ED` — **Dzień Ziemi** — a dopiero potem rozpoczyna się kolejne `EQ`.

Kanoniczny cykl siedmiodniowy:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Te nazwy są kanonicznymi identyfikatorami Tredecadia, a nie tłumaczeniami ani zmianą nazw poniedziałku–niedzieli. RC2 nie definiuje jeszcze sprawdzonych lokalizowanych aliasów dni tygodnia, dlatego używane są kanoniczne formy łacińskie.

Rok zwykły:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Rok przestępny:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia używa jednej ciągłej osi całkowitoliczbowej z prawdziwym **rokiem 0**. W samym kalendarzu nie ma potrzeby dzielenia czasu na dwie odrębne ery.

Angielskie skróty **BCE/CE** oznaczają **Before Common Era / Common Era**. Po polsku odpowiada im sens „przed naszą erą / naszej ery”, czyli **p.n.e. / n.e.**

Początek matematyczny:

`TE 00000-EQ ↔ astronomiczny rok gregoriański -9999, 20 marca`

W zwykłym zapisie historycznym odpowiada to **10000 p.n.e. (`10000 BCE`)**. Nie jest to deklaracja początku ludzkości, cywilizacji ani żadnego procesu historycznego — wyłącznie matematyczne zero współrzędnej lat Tredecadia.

Dla konwersji cywilnej:

`rok TE = astronomiczny rok gregoriański + 9999`

Dlatego rok 2026 n.e. odpowiada **TE 12025**.

## Zapis dat

Kanoniczny format wymiany używa wyłącznie ASCII i co najmniej pięciu cyfr w polu roku:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

W interfejsach dla ludzi można ukrywać zera wiodące i stosować typograficzny znak minus przy latach ujemnych. To sposób prezentacji, a nie alternatywny identyfikator.

## Miesiące

Nazwy miesięcy są międzynarodowymi identyfikatorami i w języku polskim zachowują kanoniczną pisownię łacińską.

| # | Pełna nazwa | Skrót 3-sylabowy (`Short-6`) | Forma 2-sylabowa (`Short-4`) |
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

W mowie preferowana jest forma dwusylabowa, jeśli z kontekstu wiadomo już, że chodzi o miesiąc. Wymowa referencyjna ma **lekkie uwydatnienie pierwszej sylaby**; akcent nie jest częścią tożsamości nazwy.

## Specyfikacja i kod

Referencyjny konwerter Python znajduje się w [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Dokumenty normatywne są w [`specification/`](specification/), a rejestry maszynowe w [`registry/`](registry/).

Ten polski README jest wprowadzeniem dla polskojęzycznego czytelnika i nie zastępuje specyfikacji normatywnej.

## Licencje

Dokumentacja, specyfikacje i dane: **CC BY 4.0**. Kod i skrypty: **MIT**, o ile nie zaznaczono inaczej. Zobacz [`LICENSE.md`](LICENSE.md).
