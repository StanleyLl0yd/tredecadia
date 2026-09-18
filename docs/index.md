---
layout: default
title: Tredecadia
---

<h2 data-i18n="interactiveCalendar">Interactive calendar</h2>


<div id="interactive-calendar" class="calendar-shell" aria-label="Interactive Tredecadia calendar">
  <div class="calendar-hero">
    <div class="today-card">
      <p class="eyebrow" data-i18n="todayInTredecadia">Today in Tredecadia</p>
      <div id="today-te" class="today-te canonical-date" aria-live="polite" data-i18n-placeholder="loading">Loading…</div>
      <p id="today-description" class="today-description"></p>
      <p id="today-gregorian" class="today-gregorian"></p>
    </div>
    <div id="selected-date" class="selected-card" aria-live="polite">
      <p class="eyebrow" data-i18n="selectedDate">Selected date</p>
      <h3 id="selected-te">—</h3>
      <p id="selected-description"></p>
      <p><strong id="selected-weekday"></strong></p>
      <p><span data-i18n="gregorian">Gregorian</span> <strong id="selected-gregorian" class="canonical-date">—</strong></p>
    </div>
  </div>

  <div class="calendar-toolbar" aria-label="Calendar navigation">
    <button id="calendar-prev" type="button" aria-label="Previous Tredecadia month" data-i18n="previous">← Previous</button>
    <button id="calendar-today" type="button" data-i18n="today">Today</button>
    <label class="month-control"><span data-i18n="month">Month</span>
      <select id="calendar-month" aria-label="Tredecadia month"></select>
    </label>
    <label class="year-control"><span data-i18n="teYear">TE year</span>
      <input id="calendar-year" class="canonical-input" type="text" inputmode="numeric" autocomplete="off" aria-label="Tredecadia year">
    </label>
    <button id="calendar-next" type="button" aria-label="Next Tredecadia month" data-i18n="next">Next →</button>
  </div>

  <div class="calendar-title-row">
    <h2 id="calendar-title" data-i18n-placeholder="tredecadiaMonth">Tredecadia month</h2>
    <p id="calendar-subtitle"></p>
  </div>

  <div class="calendar-scroll">
    <div id="calendar-grid" class="calendar-grid" role="group" aria-label="28-day Tredecadia month"></div>
  </div>
  <div id="intercalary-days" class="intercalary-days" aria-label="Intercalary days"></div>

  <div class="converter-grid">
    <div class="converter-card">
      <p class="eyebrow" data-i18n="gregorianToTredecadia">Gregorian → Tredecadia</p>
      <h3 data-i18n="convertCivilDate">Convert a civil date</h3>
      <form id="gregorian-form">
        <label><span data-i18n="gregorianDate">Gregorian date</span>
          <input id="gregorian-input" class="canonical-input" type="text" inputmode="numeric" autocomplete="off" placeholder="2026-09-18" aria-describedby="gregorian-help">
        </label>
        <button type="submit" data-i18n="convert">Convert</button>
      </form>
      <div id="gregorian-help" class="calendar-note" data-i18n="gregorianHelp">Astronomical year numbering is supported, including year 0 and negative years.</div>
      <div id="gregorian-result" class="converter-result" aria-live="polite"></div>
    </div>

    <div class="converter-card">
      <p class="eyebrow" data-i18n="tredecadiaToGregorian">Tredecadia → Gregorian</p>
      <h3 data-i18n="convertTeDate">Convert a canonical TE date</h3>
      <form id="tredecadia-form">
        <label><span data-i18n="tredecadiaDate">Tredecadia date</span>
          <input id="tredecadia-input" class="canonical-input" type="text" inputmode="numeric" autocomplete="off" placeholder="12025-07-14" aria-describedby="tredecadia-help">
        </label>
        <button type="submit" data-i18n="convert">Convert</button>
      </form>
      <div id="tredecadia-help" class="calendar-note" data-i18n="tredecadiaHelp">Use canonical forms such as 12025-07-14, 00000-EQ, or 09998-ED.</div>
      <div id="tredecadia-result" class="converter-result" aria-live="polite"></div>
    </div>
  </div>

  <p class="calendar-note" data-i18n="widgetNote">The widget is a convenience implementation. The specifications and machine-readable registries remain normative. “Today” uses the browser’s local civil date.</p>

  <noscript>
    <p class="calendar-error">JavaScript is disabled, so the interactive calendar is unavailable. The static specification and canonical tables remain available below.</p>
  </noscript>
</div>

<section id="page-summary" class="page-summary">
  <h2 data-i18n="aboutTitle">About Tredecadia</h2>
  <p data-i18n="aboutSummary">This page is a navigational summary, not a second copy of the standard. Normative requirements remain in the repository specifications and machine-readable registries.</p>
  <ul class="summary-facts">
    <li data-i18n="factStructure">13 equal months × 28 days = 364 regular days; every month contains four complete seven-day weeks.</li>
    <li data-i18n="factIntercalary">EQ — Equinox / New Year Day — opens each year outside the month/week cycle; leap years also contain ED — Earth Day.</li>
    <li data-i18n="factEra">Tredecadia Era (TE) is a single integer year axis with a real year 0.</li>
    <li data-i18n="factWeekdays">Mene, Noko, Kese, Zoyo, Sote, Yemo and Toze are canonical language-neutral weekday identities.</li>
  </ul>

  <h2 data-i18n="resourcesTitle">Standard and resources</h2>
  <p data-i18n="resourcesSummary">Open the full project documentation in the selected language, or inspect the published releases.</p>
  <div class="resource-links">
    <a id="summary-doc-link" class="resource-link" href="https://github.com/StanleyLl0yd/tredecadia/blob/main/README.md" data-i18n="documentation">Documentation</a>
    <a class="resource-link" href="https://github.com/StanleyLl0yd/tredecadia/blob/main/README.languages.md" data-i18n="allLanguages">All languages</a>
    <a class="resource-link" href="https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.0.0" data-i18n="stableRelease">Stable v1.0.0</a>
    <a class="resource-link" href="https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.1.0-rc.1" data-i18n="prerelease">v1.1.0-rc.1 prerelease</a>
  </div>
</section>

<script src="{{ '/assets/tredecadia-engine.js' | relative_url }}"></script>
<script src="{{ '/assets/i18n.js' | relative_url }}"></script>
<script src="{{ '/assets/calendar.js' | relative_url }}" defer></script>
