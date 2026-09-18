#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the interactive GitHub Pages calendar and its JS conversion engine."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "index.md"
ENGINE = ROOT / "docs" / "assets" / "tredecadia-engine.js"
UI = ROOT / "docs" / "assets" / "calendar.js"
CSS = ROOT / "docs" / "assets" / "calendar.css"
I18N = ROOT / "docs" / "assets" / "i18n.js"
LAYOUT = ROOT / "docs" / "_layouts" / "default.html"

NODE_TEST = r"""
const assert = require("assert");
const T = require("./docs/assets/tredecadia-engine.js");
const I = require("./docs/assets/i18n.js");
const fs = require("fs");
const vectors = require("./tests/conversion-vectors.json");
const monthRegistry = require("./registry/months.json");
const calendarRegistry = require("./registry/calendar.json");

assert.deepStrictEqual(
  T.MONTHS,
  monthRegistry.months.map(({number, canonical, short6, short4}) => ({number, canonical, short6, short4}))
);
assert.deepStrictEqual(
  T.WEEKDAYS,
  calendarRegistry.regularGrid.weekdays.map(({id, canonical}) => ({id, canonical}))
);

const profileLocale = {
  "ru-Cyrl": "ru",
  "ja-Kana": "ja",
  "ko-Hang": "ko",
  "ka-Geor": "ka",
  "hy-Armn": "hy",
  "ar-Arab": "ar",
  "hi-Deva": "hi",
  "bn-Beng": "bn",
  "fa-Arab": "fa",
};
const localizationRegistry = require("./registry/localizations.json");
for (const profile of localizationRegistry.profiles) {
  const locale = profileLocale[profile.id];
  assert(locale, profile.id);
  assert.deepStrictEqual(I.MONTH_PROFILES[locale], profile.aliases, profile.id);
}

const englishKeys = Object.keys(I.LOCALES.en.s).sort();
for (const [locale, meta] of Object.entries(I.LOCALES)) {
  assert(meta.name);
  assert(["ltr", "rtl"].includes(meta.dir), locale);
  assert(fs.existsSync("./" + meta.readme), meta.readme);
  assert.deepStrictEqual(Object.keys(meta.s).sort(), englishKeys, locale + " translation keys");
}
assert.strictEqual(I.resolveLanguage("ru-RU"), "ru");
assert.strictEqual(I.resolveLanguage("pt-PT"), "pt-BR");
assert.strictEqual(I.resolveLanguage("zh-Hant-HK"), "zh-TW");
assert.strictEqual(I.resolveLanguage("zh-Hans-CN"), "zh-CN");
assert.strictEqual(I.detectLanguage(["xx-ZZ", "ja-JP"]), "ja");
assert.strictEqual(I.detectLanguage(["xx-ZZ"]), "en");
assert.strictEqual(I.monthAlias("ru", 1).full, "Масанумика");
assert.strictEqual(I.monthAlias("es", 1), null);

for (const item of vectors.pairs) {
  const g = item.gregorianAstronomical;
  const te = T.fromGregorian(g);
  assert.strictEqual(T.formatTredecadia(te), item.tredecadia, JSON.stringify(item));
  assert.deepStrictEqual(T.toGregorian(T.parseTredecadia(item.tredecadia)), g, JSON.stringify(item));
}

for (const item of vectors.leapPredicates) {
  assert.strictEqual(T.tredecadiaIsLeap(item.tredecadiaYear), item.isLeap, JSON.stringify(item));
}

for (let day = 1; day <= 28; day += 1) {
  const weekday = T.weekdayForDay(day);
  assert.strictEqual(weekday.id, "W" + (((day - 1) % 7) + 1));
}

const canonical = [
  "00000-EQ",
  "00000-01-01",
  "09998-ED",
  "12025-07-11",
  "-00001-EQ",
  "-10000-13-28",
];
for (const value of canonical) {
  assert.strictEqual(T.formatTredecadia(T.parseTredecadia(value)), value);
}

const invalid = [
  "0000-EQ",
  "+00001-EQ",
  "-00000-EQ",
  "000001-EQ",
  "-000001-EQ",
  "−00001-EQ",
  " 12025-07-11",
  "12025-07-11 ",
  "12025/07/11",
  "١٢٠٢٥-07-11",
  "１２０２５-07-11",
  "12025-00-01",
  "12025-14-01",
  "12025-01-00",
  "12025-01-29",
  "12023-ED",
  "12025-eq",
];
for (const value of invalid) {
  assert.throws(() => T.parseTredecadia(value), value);
}

assert.strictEqual(
  T.formatTredecadia(T.fromGregorian({year: 2026, month: 9, day: 15})),
  "12025-07-11"
);
assert.deepStrictEqual(
  T.toGregorian(T.parseTredecadia("00000-EQ")),
  {year: -9999, month: 3, day: 20}
);

assert.throws(
  () => T.fromGregorian({year: T.MAX_ABS_YEAR + 1, month: 1, day: 1}),
  /interactive converter range/
);
assert.throws(
  () => T.parseTredecadia(String(T.MAX_ABS_YEAR + 1) + "-01-01"),
  /interactive converter range/
);

console.log("Tredecadia browser engine vectors: OK");
"""


def main() -> None:
    for path in (INDEX, ENGINE, UI, CSS, I18N, LAYOUT):
        assert path.is_file(), path

    index = INDEX.read_text(encoding="utf-8")
    engine = ENGINE.read_text(encoding="utf-8")
    ui = UI.read_text(encoding="utf-8")
    css = CSS.read_text(encoding="utf-8")
    i18n = I18N.read_text(encoding="utf-8")
    layout = LAYOUT.read_text(encoding="utf-8")

    for marker in (
        'id="interactive-calendar"',
        'id="calendar-grid"',
        'id="calendar-month"',
        'id="calendar-year"',
        'id="gregorian-form"',
        'id="tredecadia-form"',
        'id="page-summary"',
        'id="summary-doc-link"',
        'data-i18n="aboutTitle"',
        'data-i18n="resourcesTitle"',
        "'/assets/tredecadia-engine.js' | relative_url",
        "'/assets/i18n.js' | relative_url",
        "'/assets/calendar.js' | relative_url",
        "The widget is a convenience implementation",
    ):
        assert marker in index, marker

    for marker in (
        "function fromGregorian",
        "function toGregorian",
        "function parseTredecadia",
        "function parseGregorian",
        "function tredecadiaIsLeap",
        "MONTHS",
        "WEEKDAYS",
    ):
        assert marker in engine, marker

    for marker in (
        "renderCalendar",
        "renderToday",
        "bindConverters",
        "calendar-prev",
        "calendar-next",
        "calendar-today",
        "switchLanguage",
        "browserLanguages",
        "display-language",
    ):
        assert marker in ui, marker

    assert "@media (max-width: 900px)" in css
    assert "@media (max-width: 620px)" in css
    assert "@media (prefers-reduced-motion: reduce)" in css
    assert ".site-shell" in css
    assert ".calendar-scroll" in css
    assert ".wrapper" not in css, "Pages must not rely on jekyll-theme-minimal two-column geometry"
    assert "float:" not in css, "site layout should not reintroduce float-based theme columns"
    assert 'id="display-language"' in layout
    assert 'class="site-shell"' in layout
    assert 'class="site-header"' in layout
    assert 'class="site-main"' in layout
    assert "TredecadiaI18n" in i18n
    assert "MONTH_PROFILES" in i18n
    assert "resolveLanguage" in i18n
    assert "aboutTitle" in i18n
    assert "aboutSummary" in i18n
    assert "resourcesTitle" in i18n
    assert "allLanguages" in i18n
    assert "html.js:not(.tredecadia-interactive-ready) [data-i18n]" in css

    for stale_heading in (
        "## Calendar at a glance",
        "## Canonical weekdays",
        "## Canonical months",
        "## Published RC2 identity",
        "## Standard and data",
    ):
        assert stale_heading not in index, stale_heading

    # Keep runtime behavior dependency-free: no network data fetch is needed
    # to calculate dates, localize controls, or obtain month aliases.
    assert "fetch(" not in engine + ui + i18n

    node = shutil.which("node")
    if node is None:
        print("Node.js unavailable: static web-calendar checks passed; JS vector execution skipped")
    else:
        subprocess.run([node, "-e", NODE_TEST], cwd=ROOT, check=True)

    print("Tredecadia interactive Pages calendar validation: OK")


if __name__ == "__main__":
    main()
