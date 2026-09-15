# Tredecadia

[English](README.md) · **বাংলা** · [সব ভাষা](README.languages.md)

Tredecadia হলো একটি উন্মুক্ত স্থায়ী ক্যালেন্ডার প্রকল্প, যেখানে বছরে **২৮ দিনের ১৩টি মাস** থাকে। প্রতিটি মাস ঠিক চার সপ্তাহের, তাই একই তারিখ প্রতি বছর একই বারেই পড়ে। বছরের দৈর্ঘ্য সামঞ্জস্য করার অতিরিক্ত দিনগুলো মাস ও সাত দিনের সাপ্তাহিক চক্র—দুটোরই বাইরে থাকে।

> **বর্তমান প্রকাশ্য সংস্করণ: `1.0.0-rc.1`।** এটি একটি release candidate। v1-এর compatibility surface ইতিমধ্যে স্থির করা হয়েছে, তবে চূড়ান্ত `v1.0.0` প্রকাশের আগে বাস্তব ব্যবহার ও মতামত পর্যবেক্ষণের একটি সময় রাখা হয়েছে।

## মূল কাঠামো

- 13 × 28 = মাসের ভেতরে 364টি নিয়মিত দিন।
- প্রতিটি মাসে ঠিক চারটি পূর্ণ সপ্তাহ।
- প্রতি মাসের `01` সবসময় সোমবার, `28` সবসময় রবিবার।
- `EQ` — Equinox / New Year Day — বছর শুরু করে এবং কোনো মাস বা সপ্তাহের অংশ নয়।
- leap year-এ `13-28`-এর পরে অতিরিক্ত `ED` — Earth Day — থাকে; তার পরেই পরের বছরের `EQ` আসে।

সাধারণ বছর:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

leap year:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia বছর গণনার জন্য একটি ধারাবাহিক পূর্ণসংখ্যার অক্ষ ব্যবহার করে, যেখানে প্রকৃত **বছর 0** রয়েছে। ফলে ক্যালেন্ডারের ভেতরে BCE/CE আলাদা করে ব্যবহার করার দরকার হয় না।

গাণিতিক origin:

`TE 00000-EQ ↔ astronomical Gregorian year -9999, 20 March`

এটি প্রচলিত ভাষায় প্রায় **10000 BCE**-এর সমতুল্য। এর অর্থ মানবসভ্যতার বা কোনো ঐতিহাসিক যুগের “শুরু” নয়; এটি কেবল Tredecadia year coordinate-এর গাণিতিক শূন্যবিন্দু।

civil conversion-এর জন্য:

`TE year = astronomical Gregorian year + 9999`

তাই 2026 সাল হলো **TE 12025**।

## তারিখের বিন্যাস

canonical interchange format কেবল ASCII ব্যবহার করে এবং বছর অন্তত পাঁচ অঙ্কের হয়:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

মানুষের জন্য তৈরি UI-তে শুরুতে থাকা শূন্য বাদ দেওয়া যেতে পারে এবং typographic minus ব্যবহার করা যেতে পারে। এগুলো শুধু display form, আলাদা canonical identifier নয়।

## মাস

| # | নাম | Short-6 | Short-4 |
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

কথোপকথনে, প্রসঙ্গ থেকে মাসের কথা বোঝা গেলে চার অক্ষরের Short-4 রূপটি অগ্রাধিকার পায়। reference pronunciation-এ **প্রথম syllable-এ হালকা prominence** থাকে; stress নামের পরিচয়ের অংশ নয়।

## specification ও code

Python reference converter রয়েছে [`reference/python/tredecadia.py`](reference/python/tredecadia.py)-এ। normative documents আছে [`specification/`](specification/)-এ এবং machine-readable registries আছে [`registry/`](registry/)-এ।

এই বাংলা README শব্দে-শব্দে অনুবাদ নয়; বাংলা পাঠকের কাছে স্বাভাবিক শোনায় এমনভাবে লেখা হয়েছে। normative authority হলো আনুষ্ঠানিক specification।

## লাইসেন্স

Documentation, specification ও data: **CC BY 4.0**। Code ও script: আলাদা করে কিছু না বলা থাকলে **MIT**। বিস্তারিত [`LICENSE.md`](LICENSE.md)-এ।
