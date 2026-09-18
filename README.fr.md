# Tredecadia

[English](README.md) · **Français** · [Toutes les langues](README.languages.md)

Tredecadia est un projet ouvert de calendrier perpétuel fondé sur **13 mois de 28 jours**. Chaque mois compte exactement quatre semaines, une même date tombe toujours le même jour de la semaine et les jours d’ajustement de l’année sont placés hors des mois et hors du cycle hebdomadaire.

> **Version publique actuelle : `1.1.0-rc.1`.**

## Principe

- 13 × 28 = 364 jours réguliers dans les mois.
- Chaque mois contient quatre semaines complètes.
- Le `01` est toujours **Mene (`W1`)** et le `28` **Toze (`W7`)**.
- `EQ` — **Jour de l’équinoxe / Nouvel An** — ouvre chaque année et n’appartient ni à un mois ni à la semaine.
- Les années bissextiles ajoutent `ED` — **Jour de la Terre** — après `13-28` et juste avant le `EQ` suivant.

Cycle canonique de sept jours :

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Ces noms sont des identifiants canoniques de Tredecadia, et non des traductions ni des renommages de lundi à dimanche. Aucun alias localisé révisé n’est encore défini pour les jours de la semaine ; les formes latines canoniques sont donc conservées.

Année ordinaire :

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Année bissextile :

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Ère Tredecadia

Tredecadia utilise une seule coordonnée entière pour les années, avec une **véritable année 0**. Le calendrier n’a donc pas besoin de séparer son propre décompte en « avant l’ère commune » et « ère commune ».

Les sigles anglais **BCE/CE** signifient **Before Common Era / Common Era**, c’est-à-dire « avant l’ère commune / ère commune ».

Origine mathématique :

`TE 00000-EQ ↔ année grégorienne astronomique -9999, 20 mars`

Dans la notation historique usuelle, cela correspond à **10000 avant l’ère commune (`10000 BCE`)**. Ce point d’origine ne prétend marquer ni le début de l’humanité, ni celui de la civilisation, ni un événement historique particulier : c’est uniquement le zéro mathématique de l’échelle Tredecadia.

Pour la conversion civile :

`année TE = année grégorienne astronomique + 9999`

Ainsi, l’année 2026 de l’ère commune correspond à **TE 12025**.

## Écriture des dates

Le format canonique d’échange est en ASCII strict, avec au moins cinq chiffres pour l’année :

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Une interface destinée aux personnes peut masquer les zéros initiaux et employer un vrai signe moins typographique. Il s’agit uniquement de présentation, pas d’un second format canonique.

## Mois

Les noms des mois sont des identifiants internationaux. En français, on conserve leur forme latine canonique.

| # | Nom complet | Forme à 3 syllabes (`Short-6`) | Forme à 2 syllabes (`Short-4`) |
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

À l’oral, la forme à deux syllabes est privilégiée lorsque le contexte indique déjà qu’il s’agit d’un mois. La prononciation de référence donne **une légère proéminence à la première syllabe** ; l’accent n’est pas un élément distinctif du nom.

## Spécification et code

Le convertisseur Python de référence se trouve dans [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Les textes normatifs sont dans [`specification/`](specification/) et les registres lisibles par machine dans [`registry/`](registry/).

Ce README est une introduction rédigée pour des lecteurs francophones ; il ne remplace pas la spécification normative.

## Licences

Documentation, spécifications et données : **CC BY 4.0**. Code et scripts : **MIT**, sauf mention contraire. Voir [`LICENSE.md`](LICENSE.md).
