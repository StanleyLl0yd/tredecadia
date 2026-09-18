// SPDX-License-Identifier: MIT
(function () {
  "use strict";

  const T = window.Tredecadia;
  const I = window.TredecadiaI18n;
  if (!T || !I) {
    throw new Error("Tredecadia browser modules failed to load");
  }

  const $ = (selector) => document.querySelector(selector);
  const $$ = (selector) => Array.from(document.querySelectorAll(selector));
  const REPO_BLOB = "https://github.com/StanleyLl0yd/tredecadia/blob/main/";

  const todayGregorian = (() => {
    const now = new Date();
    return { year: now.getFullYear(), month: now.getMonth() + 1, day: now.getDate() };
  })();
  const todayTredecadia = T.fromGregorian(todayGregorian);

  let selectedYear = todayTredecadia.year;
  let selectedMonth = todayTredecadia.month || (todayTredecadia.special === "ED" ? 13 : 1);
  let selectedDay = todayTredecadia.day || 1;
  let languagePreference = loadLanguagePreference();
  let currentLocale = effectiveLocale();

  function safeStorageGet(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (_error) {
      return null;
    }
  }

  function safeStorageSet(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (_error) {
      // Storage can be disabled by browser privacy settings. The current
      // session still works; only persistence is unavailable.
    }
  }

  function loadLanguagePreference() {
    const saved = safeStorageGet(I.STORAGE_KEY);
    return saved && (saved === "auto" || I.LOCALES[saved]) ? saved : "auto";
  }

  function browserLanguages() {
    if (Array.isArray(navigator.languages) && navigator.languages.length) {
      return navigator.languages;
    }
    return [navigator.language || "en"];
  }

  function effectiveLocale() {
    return languagePreference === "auto"
      ? I.detectLanguage(browserLanguages())
      : languagePreference;
  }

  function s(key) {
    return I.string(currentLocale, key);
  }

  function formatTemplate(template, values) {
    return String(template).replace(/{([a-zA-Z0-9_]+)}/g, (_match, key) =>
      Object.prototype.hasOwnProperty.call(values, key) ? String(values[key]) : "{" + key + "}"
    );
  }

  function monthRecord(month) {
    return T.MONTHS[month - 1];
  }

  function monthDisplay(monthNumber) {
    const canonical = monthRecord(monthNumber);
    const alias = I.monthAlias(currentLocale, monthNumber);
    return {
      canonical,
      full: alias ? alias.full : canonical.canonical,
      short6: alias ? alias.short6 : canonical.short6,
      short4: alias ? alias.short4 : canonical.short4,
      localized: Boolean(alias),
    };
  }

  function sameTredecadia(a, b) {
    return a.year === b.year && a.month === b.month && a.day === b.day && a.special === b.special;
  }

  function compactGregorian(value) {
    return String(value.month).padStart(2, "0") + "-" + String(value.day).padStart(2, "0");
  }

  function describeTredecadia(value) {
    if (value.special === "EQ") {
      return s("eqName");
    }
    if (value.special === "ED") {
      return s("edName");
    }
    const month = monthDisplay(value.month);
    const weekday = T.weekdayForDay(value.day);
    const monthText = month.localized
      ? month.full + " (" + month.canonical.canonical + ")"
      : month.full;
    return monthText + " · " + weekday.id + " / " + weekday.canonical;
  }

  function setText(id, value) {
    const node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  function applyStaticTranslations() {
    document.documentElement.lang = currentLocale;
    document.documentElement.dir = I.LOCALES[currentLocale].dir;
    document.body.classList.toggle("is-rtl", I.LOCALES[currentLocale].dir === "rtl");

    $$("[data-i18n]").forEach((node) => {
      node.textContent = s(node.dataset.i18n);
    });

    ["#localized-doc-link", "#summary-doc-link"].forEach((selector) => {
      const docs = $(selector);
      if (docs) {
        docs.href = REPO_BLOB + I.readmePath(currentLocale);
        docs.hreflang = currentLocale;
      }
    });

    const calendar = $("#interactive-calendar");
    if (calendar) calendar.setAttribute("aria-label", s("interactiveCalendar"));

    const toolbar = $(".calendar-toolbar");
    if (toolbar) toolbar.setAttribute("aria-label", s("interactiveCalendar"));

    const grid = $("#calendar-grid");
    if (grid) grid.setAttribute("aria-label", s("tredecadiaMonth"));

    const intercalary = $("#intercalary-days");
    if (intercalary) intercalary.setAttribute("aria-label", s("outsideWeekdayCycle"));

    const prev = $("#calendar-prev");
    if (prev) prev.setAttribute("aria-label", s("previous"));
    const next = $("#calendar-next");
    if (next) next.setAttribute("aria-label", s("next"));
    const year = $("#calendar-year");
    if (year) year.setAttribute("aria-label", s("teYear"));
    const month = $("#calendar-month");
    if (month) month.setAttribute("aria-label", s("month"));
  }

  function populateLanguageSelect() {
    const select = $("#display-language");
    if (!select) return;

    select.innerHTML = "";

    const auto = document.createElement("option");
    auto.value = "auto";
    auto.textContent = s("autoSystem");
    select.appendChild(auto);

    Object.entries(I.LOCALES).forEach(([code, meta]) => {
      const option = document.createElement("option");
      option.value = code;
      option.textContent = meta.name;
      option.lang = code;
      option.dir = meta.dir;
      select.appendChild(option);
    });

    select.value = languagePreference;
  }

  function renderToday() {
    setText("today-te", T.formatTredecadia(todayTredecadia));
    setText("today-description", describeTredecadia(todayTredecadia));
    setText("today-gregorian", s("gregorian") + " " + T.formatGregorian(todayGregorian));
  }

  function populateMonthSelect() {
    const select = $("#calendar-month");
    select.innerHTML = "";
    T.MONTHS.forEach((month) => {
      const display = monthDisplay(month.number);
      const option = document.createElement("option");
      option.value = String(month.number);
      option.textContent =
        String(month.number).padStart(2, "0") +
        " · " +
        display.full +
        (display.localized ? " — " + month.canonical : "");
      select.appendChild(option);
    });
    select.value = String(selectedMonth);
  }

  function updateSelectedDetail(value) {
    const panel = $("#selected-date");
    const te = T.formatTredecadia(value);
    const gregorian = T.toGregorian(value);
    let detail = describeTredecadia(value);

    if (!value.special) {
      const weekday = T.weekdayForDay(value.day);
      detail += " · " + formatTemplate(s("dayOf"), { day: value.day });
      setText("selected-weekday", weekday.id + " · " + weekday.canonical);
    } else {
      setText("selected-weekday", s("outsideWeekdayCycle"));
    }

    setText("selected-te", te);
    setText("selected-description", detail);
    setText("selected-gregorian", T.formatGregorian(gregorian));
    panel.hidden = false;
  }

  function specialButton(label, value, className) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "special-day " + className;

    const strong = document.createElement("strong");
    strong.textContent = label;
    const span = document.createElement("span");
    span.className = "canonical-date";
    span.textContent = T.formatGregorian(T.toGregorian(value));
    button.append(strong, span);

    button.addEventListener("click", () => updateSelectedDetail(value));
    return button;
  }

  function renderIntercalary() {
    const container = $("#intercalary-days");
    container.innerHTML = "";
    container.appendChild(
      specialButton("EQ · " + s("eqName"), { year: selectedYear, special: "EQ" }, "eq")
    );

    if (T.tredecadiaIsLeap(selectedYear)) {
      container.appendChild(
        specialButton("ED · " + s("edName"), { year: selectedYear, special: "ED" }, "ed")
      );
    } else {
      const ordinary = document.createElement("div");
      ordinary.className = "special-day muted";
      const strong = document.createElement("strong");
      strong.textContent = s("noEarthDay");
      const span = document.createElement("span");
      span.textContent = s("ordinaryYear");
      ordinary.append(strong, span);
      container.appendChild(ordinary);
    }
  }

  function renderCalendar() {
    const display = monthDisplay(selectedMonth);
    $("#calendar-year").value = String(selectedYear);
    $("#calendar-month").value = String(selectedMonth);

    setText(
      "calendar-title",
      String(selectedMonth).padStart(2, "0") + " · " + display.full
    );

    const subtitleParts = ["TE " + T.formatDisplayYear(selectedYear)];
    if (display.localized) subtitleParts.push(display.canonical.canonical);
    subtitleParts.push(display.short6, display.short4);
    setText("calendar-subtitle", subtitleParts.join(" · "));

    const grid = $("#calendar-grid");
    grid.innerHTML = "";

    T.WEEKDAYS.forEach((weekday) => {
      const head = document.createElement("div");
      head.className = "weekday-head";
      head.dir = "ltr";
      const strong = document.createElement("strong");
      strong.textContent = weekday.canonical;
      const span = document.createElement("span");
      span.textContent = weekday.id;
      head.append(strong, span);
      grid.appendChild(head);
    });

    for (let day = 1; day <= 28; day += 1) {
      const value = { year: selectedYear, month: selectedMonth, day };
      const gregorian = T.toGregorian(value);
      const button = document.createElement("button");
      button.type = "button";
      button.className = "calendar-day";
      button.dataset.day = String(day);
      button.dir = "ltr";
      button.setAttribute(
        "aria-label",
        T.formatTredecadia(value) +
          ", " +
          T.weekdayForDay(day).canonical +
          ", " +
          s("gregorian") +
          " " +
          T.formatGregorian(gregorian)
      );

      const number = document.createElement("span");
      number.className = "day-number";
      number.textContent = String(day).padStart(2, "0");
      const mini = document.createElement("span");
      mini.className = "gregorian-mini";
      mini.textContent = "G " + compactGregorian(gregorian);
      button.append(number, mini);

      if (!todayTredecadia.special && sameTredecadia(value, todayTredecadia)) {
        button.classList.add("is-today");
        button.title = s("today");
        const badge = document.createElement("span");
        badge.className = "today-badge";
        badge.textContent = s("today");
        badge.dir = I.LOCALES[currentLocale].dir;
        button.appendChild(badge);
      }
      if (day === selectedDay) {
        button.classList.add("is-selected");
      }

      button.addEventListener("click", () => {
        selectedDay = day;
        renderCalendar();
        updateSelectedDetail(value);
      });
      grid.appendChild(button);
    }

    renderIntercalary();
    updateSelectedDetail({ year: selectedYear, month: selectedMonth, day: selectedDay });
  }

  function stepMonth(delta) {
    const index = selectedYear * 13 + (selectedMonth - 1) + delta;
    selectedYear = Math.floor(index / 13);
    selectedMonth = ((index % 13) + 13) % 13 + 1;
    selectedDay = Math.min(selectedDay, 28);
    renderCalendar();
  }

  function goToday() {
    selectedYear = todayTredecadia.year;
    selectedMonth = todayTredecadia.month || (todayTredecadia.special === "ED" ? 13 : 1);
    selectedDay = todayTredecadia.day || 1;
    populateMonthSelect();
    renderCalendar();
    updateSelectedDetail(todayTredecadia);
  }

  function showResult(target, primary, secondary, isError) {
    const node = $(target);
    node.classList.toggle("is-error", Boolean(isError));
    node.innerHTML = "";
    const strong = document.createElement("strong");
    strong.className = "canonical-date";
    strong.textContent = primary;
    const span = document.createElement("span");
    span.textContent = secondary || "";
    node.append(strong, span);
  }

  function renderGregorianConversion() {
    const input = $("#gregorian-input");
    try {
      const gregorian = T.parseGregorian(input.value.trim());
      const te = T.fromGregorian(gregorian);
      showResult("#gregorian-result", T.formatTredecadia(te), describeTredecadia(te), false);
    } catch (error) {
      showResult("#gregorian-result", s("invalidGregorian"), "", true);
    }
  }

  function renderTredecadiaConversion() {
    const input = $("#tredecadia-input");
    try {
      const te = T.parseTredecadia(input.value.trim());
      const gregorian = T.toGregorian(te);
      showResult("#tredecadia-result", T.formatGregorian(gregorian), describeTredecadia(te), false);
    } catch (error) {
      showResult("#tredecadia-result", s("invalidTredecadia"), "", true);
    }
  }

  function bindConverters() {
    const gInput = $("#gregorian-input");
    const tInput = $("#tredecadia-input");

    gInput.value = T.formatGregorian(todayGregorian);
    tInput.value = T.formatTredecadia(todayTredecadia);

    $("#gregorian-form").addEventListener("submit", (event) => {
      event.preventDefault();
      renderGregorianConversion();
    });

    $("#tredecadia-form").addEventListener("submit", (event) => {
      event.preventDefault();
      renderTredecadiaConversion();
    });

    renderGregorianConversion();
    renderTredecadiaConversion();
  }

  function switchLanguage(preference, persist) {
    languagePreference = preference && (preference === "auto" || I.LOCALES[preference])
      ? preference
      : "auto";
    if (persist) safeStorageSet(I.STORAGE_KEY, languagePreference);

    currentLocale = effectiveLocale();
    applyStaticTranslations();
    populateLanguageSelect();
    populateMonthSelect();
    renderToday();
    renderCalendar();
    renderGregorianConversion();
    renderTredecadiaConversion();
  }

  function bindLanguageSelector() {
    const select = $("#display-language");
    if (!select) return;
    select.addEventListener("change", (event) => {
      switchLanguage(event.target.value, true);
    });

    window.addEventListener("languagechange", () => {
      if (languagePreference === "auto") switchLanguage("auto", false);
    });
  }

  function bindControls() {
    $("#calendar-prev").addEventListener("click", () => stepMonth(-1));
    $("#calendar-next").addEventListener("click", () => stepMonth(1));
    $("#calendar-today").addEventListener("click", goToday);

    $("#calendar-month").addEventListener("change", (event) => {
      selectedMonth = Number(event.target.value);
      selectedDay = 1;
      renderCalendar();
    });

    $("#calendar-year").addEventListener("change", (event) => {
      const value = Number(event.target.value.trim());
      if (!Number.isSafeInteger(value) || Math.abs(value) > T.MAX_ABS_YEAR) {
        event.target.setCustomValidity(s("enterIntegerYear"));
        event.target.reportValidity();
        event.target.value = String(selectedYear);
        return;
      }
      event.target.setCustomValidity("");
      selectedYear = value;
      selectedDay = 1;
      renderCalendar();
    });
  }

  function selfCheck() {
    const checks = [
      [{ year: 2026, month: 9, day: 15 }, "12025-07-11"],
      [{ year: -9999, month: 3, day: 20 }, "00000-EQ"],
      [{ year: 0, month: 3, day: 20 }, "09999-EQ"],
    ];
    checks.forEach(([gregorian, expected]) => {
      const actual = T.formatTredecadia(T.fromGregorian(gregorian));
      if (actual !== expected) {
        throw new Error("calendar self-check failed: " + actual + " !== " + expected);
      }
    });
  }

  function init() {
    selfCheck();
    applyStaticTranslations();
    populateLanguageSelect();
    populateMonthSelect();
    bindLanguageSelector();
    bindControls();
    bindConverters();
    renderToday();
    renderCalendar();
    document.documentElement.classList.add("tredecadia-interactive-ready");
  }

  try {
    init();
  } catch (error) {
    console.error(error);
    const root = $("#interactive-calendar");
    if (root) {
      root.classList.add("calendar-failed");
      const message = document.createElement("p");
      message.className = "calendar-error";
      message.textContent =
        "Interactive calendar could not start. The static Tredecadia specification below is still available.";
      root.prepend(message);
    }
  }
})();
