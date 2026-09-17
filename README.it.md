# Tredecadia

[English](README.md) · **Italiano** · [Tutte le lingue](README.languages.md)

Tredecadia è un progetto aperto per un calendario perpetuo di **13 mesi da 28 giorni**. Ogni mese contiene esattamente quattro settimane, la stessa data cade sempre nello stesso giorno della settimana e i giorni usati per riallineare l’anno restano fuori sia dai mesi sia dal ciclo settimanale.

> **Versione pubblica attuale: `1.0.0`.**

## Come funziona

- 13 × 28 = 364 giorni regolari all’interno dei mesi.
- Ogni mese comprende quattro settimane complete.
- Il giorno `01` è sempre **Mene (`W1`)** e il `28` sempre **Toze (`W7`)**.
- `EQ` — **Giorno dell’Equinozio / Capodanno** — apre ogni anno e non appartiene né a un mese né alla settimana.
- Negli anni bisestili si aggiunge `ED` — **Giorno della Terra** — dopo `13-28` e prima del successivo `EQ`.

Ciclo canonico di sette giorni:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Questi nomi sono identificatori canonici di Tredecadia, non traduzioni o rinominazioni di lunedì–domenica. RC2 non definisce ancora alias localizzati revisionati per i giorni della settimana; vengono quindi mantenute le forme latine canoniche.

Anno ordinario:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Anno bisestile:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia usa un’unica linea numerica intera degli anni, con un vero **anno 0**. Perciò non ha bisogno di dividere internamente il tempo in due ere.

Le sigle inglesi **BCE/CE** significano **Before Common Era / Common Era**, cioè «prima dell’era comune / era comune».

Origine matematica:

`TE 00000-EQ ↔ anno gregoriano astronomico -9999, 20 marzo`

Nella consueta notazione storica questo corrisponde al **10000 prima dell’era comune (`10000 BCE`)**. Non è presentato come l’inizio dell’umanità, della civiltà o di un processo storico: è semplicemente lo zero matematico della coordinata temporale di Tredecadia.

Per la conversione civile:

`anno TE = anno gregoriano astronomico + 9999`

Di conseguenza, l’anno 2026 dell’era comune corrisponde a **TE 12025**.

## Formato delle date

Il formato canonico di scambio usa ASCII rigoroso e almeno cinque cifre per l’anno:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Nelle interfacce per persone si possono omettere gli zeri iniziali e usare il segno meno tipografico per gli anni negativi. Sono scelte di visualizzazione, non identificatori alternativi.

## Mesi

I nomi dei mesi sono identificatori internazionali; in italiano si mantiene la grafia latina canonica.

| # | Nome completo | Forma di 3 sillabe (`Short-6`) | Forma di 2 sillabe (`Short-4`) |
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

Nel parlato è preferibile la forma di due sillabe quando dal contesto è già chiaro che si sta nominando un mese. La pronuncia di riferimento usa **una lieve prominenza sulla prima sillaba**; l’accento non fa parte dell’identità del nome.

## Specifica e codice

Il convertitore Python di riferimento è in [`reference/python/tredecadia.py`](reference/python/tredecadia.py). I documenti normativi sono in [`specification/`](specification/) e i registri leggibili dalle macchine in [`registry/`](registry/).

Questo README è un’introduzione pensata per lettori italofoni e non sostituisce la specifica normativa.

## Licenze

Documentazione, specifiche e dati: **CC BY 4.0**. Codice e script: **MIT**, salvo diversa indicazione. Vedi [`LICENSE.md`](LICENSE.md).
