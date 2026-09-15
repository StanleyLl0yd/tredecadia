# Tredecadia

[English](README.md) · **Türkçe** · [Tüm diller](README.languages.md)

Tredecadia, **28 günlük 13 aydan** oluşan açık bir sürekli takvim projesidir. Her ay tam dört haftadır; aynı ay günü her yıl aynı haftanın gününe denk gelir. Yılı güneş döngüsüyle uyumlu tutan ek günler ise ayların ve yedi günlük haftanın dışında yer alır.

> **Güncel herkese açık sürüm: `1.0.0-rc.1`.** Bu bir release candidate sürümüdür. v1 için uyumluluk yüzeyi dondurulmuştur; ancak `v1.0.0` yayımlanmadan önce gerçek kullanım ve geri bildirim için gözlem dönemi devam eder.

## Temel yapı

- 13 × 28 = ayların içinde 364 normal gün.
- Her ay tam dört haftadan oluşur.
- Her ayın `01` günü pazartesi, `28` günü pazardır.
- `EQ` — Ekinoks / Yeni Yıl Günü — yılı başlatır; hiçbir aya ve haftaya ait değildir.
- Artık yıllarda `13-28` sonrasında ek olarak `ED` — Dünya Günü — gelir; ardından bir sonraki yılın `EQ` günü başlar.

Normal yıl:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Artık yıl:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia, gerçek bir **0 yılı** içeren tek bir tam sayı yıl ekseni kullanır. Takvimin kendi içinde BCE/CE ayrımına ihtiyaç yoktur.

Matematiksel başlangıç noktası:

`TE 00000-EQ ↔ astronomik Gregoryen yıl -9999, 20 Mart`

Bu tarih geleneksel gösterimde **10000 BCE** olarak adlandırılır. İnsanlığın, uygarlığın ya da herhangi bir tarihsel dönemin başlangıcı olduğu iddia edilmez; yalnızca Tredecadia yıl koordinatının matematiksel sıfırıdır.

Sivil dönüşüm için:

`TE yılı = astronomik Gregoryen yıl + 9999`

Bu nedenle 2026 yılı **TE 12025** olur.

## Tarih yazımı

Kanonik veri alışverişi biçimi yalnızca ASCII kullanır ve yıl alanı en az beş basamaktır:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

İnsanlara yönelik arayüzlerde baştaki sıfırlar kaldırılabilir ve tipografik eksi işareti kullanılabilir. Bunlar yalnızca gösterim tercihidir; alternatif kanonik kimlikler değildir.

## Aylar

| # | Ad | Short-6 | Short-4 |
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

Konuşmada bağlamın bir aydan söz edildiğini açıkça gösterdiği durumlarda dört harfli biçim tercih edilir. Referans telaffuzunda **ilk hece hafifçe öne çıkarılır**; vurgu adın kimliğinin bir parçası değildir.

## Belge ve kod

Python referans dönüştürücüsü [`reference/python/tredecadia.py`](reference/python/tredecadia.py) dosyasındadır. Normatif belgeler [`specification/`](specification/), makine tarafından okunabilir kayıtlar ise [`registry/`](registry/) altındadır.

Bu Türkçe README, doğal bir giriş metni olarak hazırlanmıştır; normatif şartnamenin yerine geçmez.

## Lisanslar

Belgeler, şartnameler ve veriler: **CC BY 4.0**. Kod ve betikler: aksi belirtilmedikçe **MIT**. Ayrıntılar için [`LICENSE.md`](LICENSE.md).
