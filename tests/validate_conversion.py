#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
from __future__ import annotations
import json,re
from pathlib import Path
from calendar_math import *
ROOT=Path(__file__).resolve().parents[1]; RX=re.compile(r'^(-?\d{5,})-(?:(\d{2})-(\d{2})|(ED|EQ))$')
def gd(v): return GregorianDate(v['year'],v['month'],v['day'])
def td(s):
 m=RX.fullmatch(s)
 if not m: raise ValueError(s)
 y=int(m.group(1))
 if format_year(y)!=m.group(1): raise ValueError(s)
 return TredecadiaDate(y,special=m.group(4)) if m.group(4) else TredecadiaDate(y,int(m.group(2)),int(m.group(3)))
def raises(fn,*a):
 try: fn(*a)
 except ValueError: return
 raise AssertionError
def main():
 p=json.loads((ROOT/'registry/calendar.json').read_text()); v=json.loads((ROOT/'tests/conversion-vectors.json').read_text()); s=json.loads((ROOT/'registry/calendar.schema.json').read_text())
 assert p['specVersion']==v['specVersion']=='0.2.0-draft' and p['profile']==v['profile']=='tredecadia-civil' and p['era']['yearZero'] is True and p['era']['canonicalMinimumDigits']==5 and s['properties']['profile']['const']=='tredecadia-civil'
 assert p['epoch']=={'tredecadia':'00000-EQ','gregorianAstronomical':{'year':-9999,'month':3,'day':20}}
 assert tredecadia_to_gregorian(TredecadiaDate(0,special='EQ'))==GregorianDate(-9999,3,20)
 for e in v['yearCoordinateExamples']: assert e['tredecadiaYear']==e['gregorianAstronomicalYear']+9999
 for e in v['leapPredicates']: assert e['reasonGregorianAstronomicalYear']==e['tredecadiaYear']-9998 and tredecadia_is_leap(e['tredecadiaYear']) is e['isLeap']
 for e in v['pairs']:
  g=gd(e['gregorianAstronomical']); t=td(e['tredecadia']); assert tredecadia_to_gregorian(t)==g and gregorian_to_tredecadia(g)==t and t.canonical==e['tredecadia']
 for start in (-800,-400,0,9600,10000,11600,12000): assert sum(tredecadia_is_leap(y) for y in range(start,start+400))==97
 assert tredecadia_is_leap(9998) and not tredecadia_is_leap(9999) and not tredecadia_is_leap(12098) and tredecadia_is_leap(12398)
 for y in range(9600,10400):
  vals=[TredecadiaDate(y,special='EQ')]+[TredecadiaDate(y,m,d) for m in range(1,14) for d in range(1,29)]
  if tredecadia_is_leap(y): vals.append(TredecadiaDate(y,special='ED'))
  for t in vals: assert gregorian_to_tredecadia(tredecadia_to_gregorian(t))==t
 for o in range(gregorian_to_ordinal(-399,3,20),gregorian_to_ordinal(401,3,20)):
  g=ordinal_to_gregorian(o); assert tredecadia_to_gregorian(gregorian_to_tredecadia(g))==g
 assert format_year(0)=='00000' and format_year(-1)=='-00001' and format_year(12025)=='12025'
 for bad in ('0000-EQ','+00001-EQ','-00000-EQ','000001-EQ','-000001-EQ'): raises(td,bad)
 raises(TredecadiaDate,12023,None,None,'ED')
 assert gregorian_to_tredecadia(GregorianDate(2026,9,15))==TredecadiaDate(12025,7,11)
 print('Tredecadia Era/conversion validation: OK')
if __name__=='__main__': main()
