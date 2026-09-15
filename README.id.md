# Tredecadia

[English](README.md) · **Bahasa Indonesia** · [Semua bahasa](README.languages.md)

Tredecadia adalah proyek terbuka untuk kalender abadi dengan **13 bulan, masing-masing 28 hari**. Setiap bulan tepat empat minggu, sehingga tanggal yang sama selalu jatuh pada hari yang sama dalam sepekan. Hari tambahan untuk menyesuaikan panjang tahun ditempatkan di luar bulan dan di luar siklus pekan tujuh hari.

> **Versi publik saat ini: `1.0.0-rc.1`.** Ini adalah release candidate. Batas kompatibilitas v1 sudah dibekukan, tetapi masih ada masa observasi dan umpan balik sebelum `v1.0.0` final dirilis.

## Struktur dasar

- 13 × 28 = 364 hari reguler di dalam bulan.
- Setiap bulan terdiri dari tepat empat minggu penuh.
- Tanggal `01` selalu Senin, dan `28` selalu Minggu.
- `EQ` — Hari Ekuinoks / Tahun Baru — membuka setiap tahun dan tidak termasuk bulan maupun pekan.
- Pada tahun kabisat, setelah `13-28` ada `ED` — Hari Bumi — sebelum `EQ` tahun berikutnya.

Tahun biasa:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Tahun kabisat:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia memakai satu garis bilangan bulat yang berkesinambungan untuk tahun, termasuk **tahun 0 yang nyata**. Karena itu kalender ini tidak perlu membagi penomoran internal menjadi BCE dan CE.

Titik asal matematisnya:

`TE 00000-EQ ↔ tahun Gregorius astronomis -9999, 20 Maret`

Secara konvensional ini kira-kira disebut **10000 BCE**. Titik tersebut bukan klaim tentang awal umat manusia, peradaban, atau periode sejarah tertentu; fungsinya hanya sebagai nol matematis untuk koordinat tahun Tredecadia.

Untuk konversi sipil:

`tahun TE = tahun Gregorius astronomis + 9999`

Karena itu 2026 sama dengan **TE 12025**.

## Format tanggal

Format pertukaran kanonik menggunakan ASCII ketat dan bidang tahun minimal lima digit:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Antarmuka untuk manusia boleh menghilangkan nol di depan dan memakai tanda minus tipografis. Itu hanya cara menampilkan tanggal, bukan pengenal kanonik alternatif.

## Bulan

| # | Nama | Short-6 | Short-4 |
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

Dalam percakapan, bentuk empat huruf lebih disukai bila konteks sudah jelas bahwa yang disebut adalah nama bulan. Pelafalan acuan memberi **penonjolan ringan pada suku kata pertama**; tekanan bukan bagian dari identitas nama.

## Spesifikasi dan kode

Konverter referensi Python tersedia di [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Dokumen normatif berada di [`specification/`](specification/), sedangkan registri yang dapat dibaca mesin berada di [`registry/`](registry/).

README ini ditulis agar terasa wajar dalam Bahasa Indonesia, bukan sebagai terjemahan kata demi kata. Untuk aturan normatif, gunakan spesifikasi resmi.

## Lisensi

Dokumentasi, spesifikasi, dan data: **CC BY 4.0**. Kode dan skrip: **MIT**, kecuali dinyatakan lain. Lihat [`LICENSE.md`](LICENSE.md).
