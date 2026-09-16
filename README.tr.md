# Tredecadia

[English](README.md) · **Türkçe** · [Tüm diller](README.languages.md)

Tredecadia, **28 günlük 13 aydan** oluşan açık bir sürekli takvim projesidir. Her ay tam dört haftadır; aynı ay günü her yıl aynı haftanın gününe denk gelir. Yılı güneş döngüsüyle uyumlu tutan ek günler ise ayların ve yedi günlük haftanın dışında yer alır.

> **Güncel herkese açık sürüm: `1.0.0-rc.2`.** Bu ikinci sürüm adayı, uluslararası açıdan tarafsız olacak şekilde tasarlanmış kanonik hafta günü adlarını getirir. Kararlı `v1.0.0`, yalnızca RC2'ye özgü gözlem döneminden ve son doğrulamadan sonra yayımlanabilir.

## Temel yapı

- 13 × 28 = ayların içinde 364 normal gün.
- Her ay tam dört haftadan oluşur.
- Her ayın `01` günü **Mene (`W1`)**, `28` günü **Toze (`W7`)** olur.
- `EQ` — **Ekinoks / Yeni Yıl Günü** — yılı başlatır; hiçbir aya ve haftaya ait değildir.
- Artık yıllarda `13-28` sonrasında ek olarak `ED` — **Dünya Günü** — gelir; ardından bir sonraki yılın `EQ` günü başlar.

Kanonik yedi günlük döngü:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Bu adlar Tredecadia'nın kanonik kimlikleridir; pazartesiden pazara kadar olan Gregoryen adların çevirileri veya yeniden adlandırmaları değildir. RC2 henüz hafta günleri için incelenmiş yerelleştirilmiş takma adlar tanımlamaz; bu nedenle kanonik Latin biçimleri kullanılır.

Normal yıl:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Artık yıl:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Çağı

Tredecadia, gerçek bir **0 yılı** içeren tek bir tam sayı yıl ekseni kullanır. Bu nedenle kendi içinde zamanı iki ayrı çağa bölmeye ihtiyaç duymaz.

İngilizce **BCE/CE** kısaltmaları **Before Common Era / Common Era** anlamına gelir; Türkçede karşılığı kabaca **Ortak Çağ'dan Önce / Ortak Çağ** şeklindedir.

Matematiksel başlangıç noktası:

`TE 00000-EQ ↔ astronomik Gregoryen yıl -9999, 20 Mart`

Alışılmış tarihsel gösterimde bu, **Ortak Çağ'dan Önce 10000 (`10000 BCE`)** yılına karşılık gelir. Bu noktanın insanlığın, uygarlığın ya da herhangi bir tarihsel dönemin başlangıcı olduğu iddia edilmez; yalnızca Tredecadia yıl koordinatının matematiksel sıfırıdır.

Sivil dönüşüm için:

`TE yılı = astronomik Gregoryen yıl + 9999`

Bu nedenle Ortak Çağ'ın 2026 yılı **TE 12025** olur.

## Tarih yazımı

Kanonik veri alışverişi biçimi yalnızca ASCII kullanır ve yıl alanı en az beş basamaktır:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

İnsanlara yönelik arayüzlerde baştaki sıfırlar kaldırılabilir ve negatif yıllarda tipografik eksi işareti kullanılabilir. Bunlar yalnızca gösterim tercihidir; alternatif kanonik kimlikler değildir.

## Aylar

Ay adları uluslararası kimliklerdir ve Türkçede kanonik Latin yazımı korunur.

| # | Tam ad | 3 heceli kısa biçim (`Short-6`) | 2 heceli konuşma biçimi (`Short-4`) |
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

Konuşmada bağlamın bir aydan söz edildiğini açıkça gösterdiği durumlarda iki heceli kısa biçim tercih edilir. Referans telaffuzunda **ilk hece hafifçe öne çıkarılır**; vurgu adın kimliğinin bir parçası değildir.

## Belge ve kod

Python referans dönüştürücüsü [`reference/python/tredecadia.py`](reference/python/tredecadia.py) dosyasındadır. Normatif belgeler [`specification/`](specification/), makine tarafından okunabilir kayıtlar ise [`registry/`](registry/) altındadır.

Bu Türkçe README, Türkçe okurlar için hazırlanmış bir giriş metnidir; normatif şartnamenin yerine geçmez.

## Lisanslar

Belgeler, şartnameler ve veriler: **CC BY 4.0**. Kod ve betikler: aksi belirtilmedikçe **MIT**. Ayrıntılar için [`LICENSE.md`](LICENSE.md).
