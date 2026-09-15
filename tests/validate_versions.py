#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EXPECTED='1.0.0-rc.1'
def j(p): return json.loads((ROOT/p).read_text())
def main():
 vals=[
  j('registry/months.json')['specVersion'],
  j('registry/calendar.json')['specVersion'],
  j('registry/localizations.json')['specVersion'],
  j('tests/test-vectors.json')['specVersion'],
  j('tests/conversion-vectors.json')['specVersion'],
  j('tests/short4-ux-vectors.json')['specVersion'],
  j('tests/accessibility-vectors.json')['specVersion'],
 ]; assert set(vals)=={EXPECTED}
 assert f'version: "{EXPECTED}"' in (ROOT/'CITATION.cff').read_text()
 for p in ['specification/calendar-standard.md','specification/conversion-standard.md','specification/date-notation.md','specification/month-naming-standard.md','specification/localization.md','specification/localization-profiles.md','specification/compatibility.md']:
  assert f'Status: **{EXPECTED}' in (ROOT/p).read_text(),p
 for p in ['README.md','ROADMAP.md','docs/index.md','CHANGELOG.md','rationale/release-candidate-audit.md']:
  assert EXPECTED in (ROOT/p).read_text(),p
 print('Tredecadia version consistency: OK')
if __name__=='__main__': main()
