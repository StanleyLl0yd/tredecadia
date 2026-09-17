# Tredecadia

[English](README.md) · **Bahasa Indonesia** · [Semua bahasa](README.languages.md)

Tredecadia adalah proyek terbuka untuk kalender abadi dengan **13 bulan, masing-masing 28 hari**. Setiap bulan tepat empat minggu, sehingga tanggal yang sama selalu berada pada posisi yang sama dalam siklus pekan. Hari tambahan untuk menyesuaikan panjang tahun ditempatkan di luar bulan dan di luar siklus pekan tujuh hari.

> **Versi publik saat ini: `1.0.0`.**

## Struktur dasar

- 13 × 28 = 364 hari reguler di dalam bulan.
- Setiap bulan terdiri dari tepat empat minggu penuh.
- Tanggal `01` selalu **Mene (`W1`)**, dan `28` selalu **Toze (`W7`)**.
- `EQ` — **Hari Ekuinoks / Tahun Baru** — membuka setiap tahun dan tidak termasuk bulan maupun pekan.
- Pada tahun kabisat, setelah `13-28` ada `ED` — **Hari Bumi** — sebelum `EQ` tahun berikutnya.

Siklus tujuh hari kanonik:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Nama-nama ini adalah pengenal kanonik Tredecadia, bukan terjemahan atau penggantian nama Senin sampai Minggu. RC2 belum menetapkan alias hari pekan yang dilokalkan dan ditinjau, sehingga bentuk Latin kanonik digunakan.

Tahun biasa:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Tahun kabisat:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia memakai satu garis bilangan bulat yang berkesinambungan untuk tahun, termasuk **tahun 0 yang nyata**. Karena itu kalender ini tidak perlu membagi penomoran internal menjadi dua era.

Singkatan Inggris **BCE/CE** berasal dari **Before Common Era / Common Era**, secara harfiah **sebelum Era Umum / Era Umum**. Dalam penulisan sejarah Indonesia, pembagian waktunya secara kronologis sepadan dengan **SM/M (Sebelum Masehi/Masehi)**, tetapi Tredecadia sendiri tidak memakai pembagian tersebut.

Titik asal matematisnya:

`TE 00000-EQ ↔ tahun Gregorius astronomis -9999, 20 Maret`

Dalam penanggalan sejarah biasa, ini setara dengan **10000 sebelum Era Umum (`10000 BCE`)**. Titik tersebut bukan klaim tentang awal umat manusia, peradaban, atau periode sejarah tertentu; fungsinya hanya sebagai nol matematis untuk koordinat tahun Tredecadia.

Untuk konversi sipil:

`tahun TE = tahun Gregorius astronomis + 9999`

Karena itu tahun 2026 Era Umum sama dengan **TE 12025**.

## Format tanggal

Format pertukaran kanonik menggunakan ASCII ketat dan bidang tahun minimal lima digit:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Antarmuka untuk manusia boleh menghilangkan nol di depan dan memakai tanda minus tipografis untuk tahun negatif. Itu hanya cara menampilkan tanggal, bukan pengenal kanonik alternatif.

## Bulan

Nama bulan adalah pengenal internasional yang tetap. Karena belum ada profil ejaan lokal lain yang diperlukan untuk alfabet Indonesia, bentuk Latin kanonik dipakai langsung.

| # | Nama lengkap | Bentuk singkat 3 suku kata (`Short-6`) | Bentuk lisan 2 suku kata (`Short-4`) |
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

Dalam percakapan, bentuk dua suku kata lebih disukai bila konteks sudah jelas bahwa yang disebut adalah nama bulan. Pelafalan acuan memberi **penonjolan ringan pada suku kata pertama**; tekanan bukan bagian dari identitas nama.

## Spesifikasi dan kode

Konverter acuan Python tersedia di [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Dokumen normatif berada di [`specification/`](specification/), sedangkan registri yang dapat dibaca mesin berada di [`registry/`](registry/).

README ini merupakan pengantar bagi pembaca berbahasa Indonesia dan tidak menggantikan spesifikasi normatif.

## Lisensi

Dokumentasi, spesifikasi, dan data: **CC BY 4.0**. Kode dan skrip: **MIT**, kecuali dinyatakan lain. Lihat [`LICENSE.md`](LICENSE.md).
