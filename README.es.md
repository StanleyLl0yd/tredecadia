# Tredecadia

[English](README.md) · **Español** · [Todos los idiomas](README.languages.md)

Tredecadia es una propuesta abierta de calendario perpetuo de **13 meses de 28 días**. Todos los meses tienen exactamente cuatro semanas, una misma fecha cae siempre en el mismo día de la semana y los días que ajustan el año quedan fuera de los meses y de la semana de siete días.

> **Versión pública actual: `1.0.0-rc.2`.** Esta segunda candidata introduce nombres canónicos internacionalmente neutros para los días de la semana. La versión estable `v1.0.0` solo podrá publicarse después de un periodo de observación específico de RC2 y una revisión final.

## Cómo funciona

- 13 × 28 = 364 días ordinarios dentro de los meses.
- Cada mes contiene cuatro semanas completas.
- El día `01` siempre es **Mene (`W1`)** y el `28` siempre es **Toze (`W7`)**.
- `EQ` — **Día del Equinoccio / Año Nuevo** — abre cada año y no pertenece a ningún mes ni a la semana.
- En los años bisiestos aparece además `ED` — **Día de la Tierra** — después de `13-28` y antes del siguiente `EQ`.

Ciclo canónico de siete días:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Estos son identificadores canónicos de Tredecadia, no traducciones ni cambios de nombre de los días de lunes a domingo. RC2 no define todavía alias localizados revisados para los días de la semana, por lo que se conservan las formas latinas canónicas.

Año ordinario:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Año bisiesto:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Era Tredecadia

Tredecadia usa una única línea numérica de años y dispone de un **año 0 real**. Dentro del propio calendario no hace falta dividir el tiempo en «antes de la era común» y «era común».

Las siglas inglesas **BCE/CE** significan **Before Common Era / Common Era**, es decir, «antes de la era común / era común».

El origen matemático es:

`TE 00000-EQ ↔ año gregoriano astronómico -9999, 20 de marzo`

En la notación histórica habitual esto corresponde a **10000 antes de la era común (`10000 BCE`)**. No se afirma que sea el comienzo de la humanidad, de la civilización ni de ningún proceso histórico: es simplemente el cero matemático de la escala de Tredecadia.

Para la conversión civil:

`año TE = año gregoriano astronómico + 9999`

Por eso, el año 2026 de la era común corresponde a **TE 12025**.

## Formato de fecha

El formato canónico de intercambio usa ASCII estricto y un campo de año de al menos cinco cifras:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Las interfaces para personas pueden omitir los ceros iniciales y usar un signo menos tipográfico en los años negativos. Son formas de presentación, no identificadores alternativos.

## Meses

Los nombres de los meses son identificadores internacionales y se conservan en su grafía latina canónica.

| # | Nombre completo | Forma de 3 sílabas (`Short-6`) | Forma de 2 sílabas (`Short-4`) |
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

En conversación se prefiere la forma de dos sílabas cuando el contexto ya deja claro que se habla de un mes. La pronunciación de referencia usa una **ligera prominencia en la primera sílaba**; el acento no forma parte de la identidad del nombre.

## Especificación y código

El conversor de referencia en Python está en [`reference/python/tredecadia.py`](reference/python/tredecadia.py). La especificación normativa vive en [`specification/`](specification/) y los registros para máquinas en [`registry/`](registry/).

Este README está redactado para lectores hispanohablantes y no sustituye la especificación normativa.

## Licencias

Documentación, especificaciones y datos: **CC BY 4.0**. Código y scripts: **MIT**, salvo indicación expresa en contrario. Consulta [`LICENSE.md`](LICENSE.md).
