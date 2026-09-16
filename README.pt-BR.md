# Tredecadia

[English](README.md) · **Português (Brasil)** · [Todos os idiomas](README.languages.md)

Tredecadia é uma proposta aberta de calendário perpétuo com **13 meses de 28 dias**. Todos os meses têm exatamente quatro semanas, a mesma data cai sempre no mesmo dia da semana e os dias usados para ajustar o ano ficam fora dos meses e da semana de sete dias.

> **Versão pública atual: `1.0.0-rc.2`.** Esta segunda candidata introduz nomes canônicos internacionalmente neutros para os dias da semana. A versão estável `v1.0.0` só poderá ser publicada depois de um período de observação específico do RC2 e de uma revisão final.

## Como o calendário funciona

- 13 × 28 = 364 dias regulares dentro dos meses.
- Cada mês tem quatro semanas completas.
- O dia `01` é sempre **Mene (`W1`)**; o `28`, **Toze (`W7`)**.
- `EQ` — **Dia do Equinócio / Ano-Novo** — abre cada ano e não pertence a nenhum mês nem à semana.
- Em anos bissextos há também `ED` — **Dia da Terra** — depois de `13-28` e antes do `EQ` do ano seguinte.

Ciclo canônico de sete dias:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Esses nomes são identificadores canônicos da Tredecadia, não traduções nem renomeações de segunda-feira a domingo. O RC2 ainda não define aliases localizados revisados para os dias da semana, portanto são usadas as formas latinas canônicas.

Ano comum:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Ano bissexto:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia usa uma única linha numérica de anos, com um **ano 0 de verdade**. O calendário não precisa dividir internamente o tempo em duas eras.

As siglas inglesas **BCE/CE** significam **Before Common Era / Common Era**, isto é, «antes da Era Comum / Era Comum».

A origem matemática é:

`TE 00000-EQ ↔ ano gregoriano astronômico -9999, 20 de março`

Na notação histórica habitual, isso corresponde a **10000 antes da Era Comum (`10000 BCE`)**. A escolha não representa o “início da humanidade”, da civilização ou de qualquer processo histórico; é apenas o zero matemático da escala de anos.

Para a conversão civil:

`ano TE = ano gregoriano astronômico + 9999`

Assim, o ano 2026 da Era Comum corresponde a **TE 12025**.

## Formato das datas

O formato canônico de intercâmbio usa ASCII estrito e pelo menos cinco dígitos para o ano:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Interfaces voltadas a pessoas podem esconder zeros à esquerda e usar o sinal de menos tipográfico em anos negativos. Isso muda apenas a apresentação, não a forma canônica.

## Meses

Os nomes dos meses são identificadores internacionais e permanecem na grafia latina canônica.

| # | Nome completo | Forma de 3 sílabas (`Short-6`) | Forma de 2 sílabas (`Short-4`) |
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

Na fala, a forma de duas sílabas é a abreviação preferida quando o contexto já deixa claro que se trata de um mês. A pronúncia de referência usa **uma leve proeminência na primeira sílaba**; o acento não faz parte da identidade do nome.

## Especificação e código

O conversor de referência em Python está em [`reference/python/tredecadia.py`](reference/python/tredecadia.py). A especificação normativa fica em [`specification/`](specification/) e os registros legíveis por máquina em [`registry/`](registry/).

Este README foi escrito para leitores de português do Brasil e não substitui a especificação normativa.

## Licenças

Documentação, especificações e dados: **CC BY 4.0**. Código e scripts: **MIT**, salvo indicação em contrário. Consulte [`LICENSE.md`](LICENSE.md).
