# Month Naming Methodology

This document is non-normative. It records the design method used to select the canonical 13-name set.

## Structural model

A candidate month name is exactly five CV syllables drawn from:

`MA MI MU NA NI NU SA SU TA YA KA ZU`

The five syllables in one name are distinct. Adjacent syllables must not share the same consonant onset. Canonical names were selected with pairwise positional Hamming distance at least 4 of 5 syllables.

## Human shortening model

The search explicitly treated shortening as part of the design rather than as an afterthought:

- full form: 5 syllables / 10 letters;
- normal short form: first 3 syllables / 6 letters;
- compact form: first 2 syllables / 4 letters.

Five-letter truncation was excluded because it cuts through a CV syllable.

The selected set minimizes short-form syllable-frequency imbalance while retaining the full-name balance optimum. It also avoids adding any new close edit-distance pairs beyond the unavoidable close pairs already present in the fixed core used during the search.

## Semantic clearance policy

Potential cross-language matches were classified by practical severity:

- **BLOCK** — a substantial international risk that should exclude a candidate;
- **SOFT** — a neutral word, name, place, or other real but tolerable coincidence;
- **IGNORE** — obscure, materially different, fictional, or otherwise insignificant coincidence.

The search used a lazy cutting-plane process: semantic clearance focused on names that actually appeared in exact optimum solutions rather than attempting to enumerate every possible lexical coincidence in the full structural search space.

## Balance record

For the selected 13 names, the 65-syllable frequency vector has sum of squared counts `379`, corresponding to SSD `26.916666666666664` around the uniform 12-syllable mean.

The Short-6 SSD is `10.25`; the Short-4 SSD is `3.6666666666666665`.

The canonical cyclic order was then chosen to separate the closest shortened forms while keeping adjacent full and shortened names maximally distinct by positional Hamming distance.
