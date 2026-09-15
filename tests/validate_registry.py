#!/usr/bin/env python3
"""Validate the Tredecadia month registry and naming invariants."""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INVENTORY=["MA","MI","MU","NA","NI","NU","SA","SU","TA","YA","KA","ZU"]
BANNED={("MA","ZU"),("ZU","NI"),("ZU","MU"),("NU","ZU"),("ZU","SU"),("ZU","YA")}
IPA={"MA":"ma","MI":"mi","MU":"mu","NA":"na","NI":"ni","NU":"nu","SA":"sa","SU":"su","TA":"ta","YA":"ja","KA":"ka","ZU":"zu"}
def h(a,b): return sum(x!=y for x,y in zip(a,b))
def lev(a,b):
 r=list(range(len(b)+1))
 for i,ca in enumerate(a,1):
  n=[i]
  for j,cb in enumerate(b,1): n.append(min(n[-1]+1,r[j]+1,r[j-1]+(ca!=cb)))
  r=n
 return r[-1]
def ssd(c,p):
 mean=Fraction(13*p,12); return sum((Fraction(c[s])-mean)**2 for s in INVENTORY)
def frac(v): return Fraction(v["numerator"],v["denominator"])
def cyc(i,j,n=13):
 d=abs(i-j); return min(d,n-d)
def main():
 d=json.loads((ROOT/'registry/months.json').read_text()); v=json.loads((ROOT/'tests/test-vectors.json').read_text()); s=json.loads((ROOT/'registry/months.schema.json').read_text()); m=d['months']
 assert d['schemaVersion']==1 and d['status']=='draft' and d['specVersion']==v['specVersion']=='0.2.0-draft'
 assert s['$schema']=='https://json-schema.org/draft/2020-12/schema' and d['syllableInventory']==INVENTORY and len(m)==13
 assert [x['number'] for x in m]==list(range(1,14))
 c=[x['canonical'] for x in m]; a6=[x['short6'] for x in m]; a4=[x['short4'] for x in m]; assert len(set(c))==len(set(a6))==len(set(a4))==13
 for x in m:
  sy=x['syllables']; assert len(sy)==len(set(sy))==5 and all(q in INVENTORY for q in sy)
  assert all(a[0]!=b[0] and (a,b) not in BANNED for a,b in zip(sy,sy[1:]))
  assert x['canonical']==''.join(sy).lower().capitalize() and x['short6']==''.join(sy[:3]).lower().capitalize() and x['short4']==''.join(sy[:2]).lower().capitalize()
  assert x['ipa']=='ˈ'+'.'.join(IPA[q] for q in sy) and x['localizations'].get('ru')
 for i in range(13):
  for j in range(i+1,13): assert h(m[i]['syllables'],m[j]['syllables'])>=4 and h(m[i]['syllables'][:3],m[j]['syllables'][:3])>=2
 full=Counter(q for x in m for q in x['syllables']); c6=Counter(q for x in m for q in x['syllables'][:3]); c4=Counter(q for x in m for q in x['syllables'][:2]); n=v['naming']
 assert dict(full)==n['fullFrequencyVector'] and sum(x*x for x in full.values())==379 and ssd(full,5)==frac(n['fullSsd'])==Fraction(323,12) and ssd(c6,3)==frac(n['short6Ssd'])==Fraction(41,4) and ssd(c4,2)==frac(n['short4Ssd'])==Fraction(11,3)
 d26=[]; d14=[]
 for i in range(13):
  for j in range(i+1,13):
   if lev(a6[i].lower(),a6[j].lower())==2: d26.append([a6[i],a6[j]])
   if lev(a4[i].lower(),a4[j].lower())==1: d14.append([a4[i],a4[j]])
 assert d26==n['short6LevenshteinDistance2Pairs'] and d14==n['short4LevenshteinDistance1Pairs']
 f=[]; q6=[]; q4=[]; sh=[]
 for i in range(13):
  a=m[i]['syllables']; b=m[(i+1)%13]['syllables']; f.append(h(a,b)); q6.append(h(a[:3],b[:3])); q4.append(h(a[:2],b[:2])); sh.append(len(set(a)&set(b)))
 cv=v['cycle']; assert min(f)==cv['minimumAdjacentFullHamming']==5 and min(q6)==cv['minimumAdjacentShort6SyllableHamming']==3 and min(q4)==cv['minimumAdjacentShort4SyllableHamming']==2 and max(sh)==cv['maximumAdjacentSharedSyllables']==2
 i6={x['short6']:i for i,x in enumerate(m)}; i4={x['short4']:i for i,x in enumerate(m)}
 assert {'Yanimu/Yanazu':cyc(i6['Yanimu'],i6['Yanazu']),'Nazu/Kazu':cyc(i4['Nazu'],i4['Kazu']),'Yani/Yana':cyc(i4['Yani'],i4['Yana'])}==cv['closePairCyclicDistances']
 print('Tredecadia registry validation: OK')
if __name__=='__main__': main()
