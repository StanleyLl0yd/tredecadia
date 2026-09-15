# Tredecadia

[English](README.md) · **हिन्दी** · [सभी भाषाएँ](README.languages.md)

Tredecadia एक खुली, स्थायी कैलेंडर प्रणाली का प्रस्ताव है जिसमें **28 दिनों के 13 महीने** होते हैं। हर महीना ठीक चार सप्ताह का है, इसलिए किसी महीने की वही तारीख हर साल उसी वार पर आती है। वर्ष की लंबाई को संतुलित करने वाले अतिरिक्त दिन महीनों और सात-दिवसीय सप्ताह दोनों से बाहर रखे जाते हैं।

> **मौजूदा सार्वजनिक संस्करण: `1.0.0-rc.1`।** यह release candidate है। v1 की compatibility surface अब स्थिर है, लेकिन अंतिम `v1.0.0` से पहले वास्तविक उपयोग और प्रतिक्रिया के लिए observation period रखा गया है।

## मूल संरचना

- 13 × 28 = महीनों के भीतर 364 सामान्य दिन।
- हर महीना ठीक चार पूरे सप्ताह का है।
- हर महीने का `01` हमेशा सोमवार और `28` हमेशा रविवार होता है।
- `EQ` — Equinox / New Year Day — वर्ष की शुरुआत करता है और किसी महीने या सप्ताह का हिस्सा नहीं है।
- leap year में `13-28` के बाद अतिरिक्त `ED` — Earth Day — आता है; उसके बाद अगले वर्ष का `EQ` शुरू होता है।

सामान्य वर्ष:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

leap year:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia वर्ष-गणना के लिए एक ही निरंतर पूर्णांक रेखा का उपयोग करता है, जिसमें वास्तविक **वर्ष 0** मौजूद है। इसलिए कैलेंडर के भीतर BCE/CE जैसी दो अलग दिशाओं वाली गणना की आवश्यकता नहीं रहती।

गणितीय origin:

`TE 00000-EQ ↔ astronomical Gregorian year -9999, 20 March`

यह सामान्य ऐतिहासिक अभिव्यक्ति में लगभग **10000 BCE** के बराबर है। इसका अर्थ मानवता, सभ्यता या किसी ऐतिहासिक युग की “शुरुआत” नहीं है; यह केवल Tredecadia year coordinate का गणितीय शून्य है।

civil conversion के लिए:

`TE year = astronomical Gregorian year + 9999`

इसलिए 2026 का वर्ष **TE 12025** है।

## तारीख का प्रारूप

canonical interchange format केवल ASCII का उपयोग करता है और वर्ष कम-से-कम पाँच अंकों का होता है:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

मानव-पठनीय UI में शुरुआती शून्य हटाए जा सकते हैं और typographic minus इस्तेमाल किया जा सकता है। ये display रूप हैं, वैकल्पिक canonical identifiers नहीं।

## महीने

| # | नाम | Short-6 | Short-4 |
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

बातचीत में, जब संदर्भ से स्पष्ट हो कि किसी महीने की बात हो रही है, चार-अक्षरी Short-4 रूप को प्राथमिकता दी जाती है। reference pronunciation में **पहले syllable पर हल्का prominence** रहता है; stress नाम की पहचान का हिस्सा नहीं है।

## specification और code

Python reference converter [`reference/python/tredecadia.py`](reference/python/tredecadia.py) में है। normative documents [`specification/`](specification/) में और machine-readable registries [`registry/`](registry/) में हैं।

यह हिन्दी README शब्दशः अनुवाद नहीं है; इसे हिन्दी पाठक के लिए स्वाभाविक परिचय की तरह लिखा गया है। normative authority आधिकारिक specification ही है।

## लाइसेंस

Documentation, specifications और data: **CC BY 4.0**। Code और scripts: **MIT**, जब तक अलग से न कहा गया हो। विवरण के लिए [`LICENSE.md`](LICENSE.md) देखें।
