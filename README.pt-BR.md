# Tredecadia

[English](README.md) · **Português (Brasil)** · [Todos os idiomas](README.languages.md)

Tredecadia é uma proposta aberta de calendário perpétuo com **13 meses de 28 dias**. Todos os meses têm exatamente quatro semanas, a mesma data cai sempre no mesmo dia da semana e os dias usados para ajustar o ano ficam fora dos meses e da semana de sete dias.

> **Versão pública atual: `1.0.0-rc.1`.** Esta é uma release candidate: a superfície de compatibilidade da v1 já está congelada, mas o projeto ainda passa por um período de observação antes da versão final `v1.0.0`.

## Como o calendário funciona

- 13 × 28 = 364 dias regulares dentro dos meses.
- Cada mês tem quatro semanas completas.
- O dia `01` é sempre segunda-feira; o `28`, domingo.
- `EQ` — Dia do Equinócio / Ano-Novo — abre cada ano e não pertence a nenhum mês nem à semana.
- Em anos bissextos há também `ED` — Dia da Terra — depois de `13-28` e antes do `EQ` do ano seguinte.

Ano comum:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Ano bissexto:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia usa uma única linha numérica de anos, com um **ano 0 de verdade**. O calendário não precisa dividir internamente o tempo em BCE/CE.

A origem matemática é:

`TE 00000-EQ ↔ ano gregoriano astronômico -9999, 20 de março`

Isso corresponde ao que normalmente se chama de **10000 BCE**. A escolha não representa o “início da humanidade”, da civilização ou de qualquer processo histórico; é apenas o zero matemático da escala de anos.

Para a conversão civil:

`ano TE = ano gregoriano astronômico + 9999`

Assim, 2026 corresponde a **TE 12025**.

## Formato das datas

O formato canônico de intercâmbio usa ASCII estrito e pelo menos cinco dígitos para o ano:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Interfaces voltadas a pessoas podem esconder zeros à esquerda e usar o sinal de menos tipográfico. Isso muda apenas a apresentação, não a forma canônica.

## Meses

| # | Nome | Short-6 | Short-4 |
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

Na fala, a forma de quatro letras é a abreviação preferida quando o contexto já deixa claro que se trata de um mês. A pronúncia de referência usa **uma leve proeminência na primeira sílaba**; o acento não faz parte da identidade do nome.

## Especificação e código

O conversor de referência em Python está em [`reference/python/tredecadia.py`](reference/python/tredecadia.py). A especificação normativa fica em [`specification/`](specification/) e os registros legíveis por máquina em [`registry/`](registry/).

Este README foi escrito para soar natural em português; ele serve como introdução e não substitui a especificação normativa.

## Licenças

Documentação, especificações e dados: **CC BY 4.0**. Código e scripts: **MIT**, salvo indicação em contrário. Consulte [`LICENSE.md`](LICENSE.md).
