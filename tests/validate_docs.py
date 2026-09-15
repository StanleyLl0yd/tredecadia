#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'registry/months.json').read_text()); MONTHS=DATA['months']; IPA=DATA['pronunciation']['syllableIpa']
LOC=json.loads((ROOT/'registry/localizations.json').read_text())
def t(p): return (ROOT/p).read_text()
def once(doc,row,p): assert doc.count(row)==1,f'{p}: {row}'
def main():
 r=t('README.md'); n=t('specification/month-naming-standard.md'); l=t('specification/localization.md'); lp=t('specification/localization-profiles.md')
 for m in MONTHS:
  i=m['number']; segmental='.'.join(IPA[s] for s in m['syllables'])
  once(r,f"| {i:02d} | {m['canonical']} | {m['short6']} | {m['short4']} |",'README')
  once(n,f"| {i:02d} | {m['canonical']} | {'-'.join(m['syllables'])} | /{segmental}/ | [{m['citationIpa']}] | {m['short6']} | {m['short4']} |",'naming')
 for profile in LOC['profiles']:
  assert profile['id'] in l and profile['id'] in lp
 docs='\n'.join(t(p) for p in ['README.md','ROADMAP.md','specification/calendar-standard.md','specification/conversion-standard.md','specification/date-notation.md','specification/month-naming-standard.md','specification/localization.md','specification/localization-profiles.md','rationale/design.md','rationale/pronunciation.md','rationale/short4-ux.md','rationale/accessibility-years.md'])
 for stale in ['leap-year determination as an external parameter','does not yet define a mandatory epoch','symbolic forms are provisional','positive year numbers beginning with year `1`','Y-EQ is the final day associated with year']: assert stale not in docs
 for required in ['Tredecadia Era','year `0`','10000 BCE','Y - 9999','Y - 9998','astronomical','weak initial prominence','Short-4','candidate','reviewed','stable','ASCII decimal digits','Accessible semantic labels','Unicode MINUS SIGN']: assert required in docs
 assert '`Y-EQ` is the first civil day' in docs and '12025-07-11' in docs and 'Status: **complete**' in t('ROADMAP.md')
 assert 'stressIdentityCritical' in (ROOT/'registry/months.json').read_text() and 'citationProminence' in (ROOT/'registry/months.json').read_text()
 assert all('localizations' not in m for m in MONTHS)
 u=t('LICENSE.md').lower(); c=t('LICENSES/CC-BY-4.0.md').lower(); assert all(x in u and x in c for x in ['documentation','machine-readable registries','test vectors']) and 'source code' in u
 print('Tredecadia documentation consistency: OK')
if __name__=='__main__': main()
