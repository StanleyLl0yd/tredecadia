// SPDX-License-Identifier: MIT
(function () {
  "use strict";

  const T = window.Tredecadia;
  if (!T) {
    throw new Error("Tredecadia engine failed to load");
  }

  const $ = (selector) => document.querySelector(selector);
  const todayGregorian = (() => {
    const now = new Date();
    return { year: now.getFullYear(), month: now.getMonth() + 1, day: now.getDate() };
  })();
  const todayTredecadia = T.fromGregorian(todayGregorian);

  let selectedYear = todayTredecadia.year;
  let selectedMonth = todayTredecadia.month || (todayTredecadia.special === "ED" ? 13 : 1);
  let selectedDay = todayTredecadia.day || 1;

  function monthRecord(month) {
    return T.MONTHS[month - 1];
  }

  function sameGregorian(a, b) {
    return a.year === b.year && a.month === b.month && a.day === b.day;
  }

  function sameTredecadia(a, b) {
    return a.year === b.year && a.month === b.month && a.day === b.day && a.special === b.special;
  }

  function compactGregorian(value) {
    return String(value.month).padStart(2, "0") + "-" + String(value.day).padStart(2, "0");
  }

  function describeTredecadia(value) {
    if (value.special === "EQ") {
      return "Equinox / New Year Day";
    }
    if (value.special === "ED") {
      return "Earth Day";
    }
    const month = monthRecord(value.month);
    const weekday = T.weekdayForDay(value.day);
    return month.canonical + " · " + weekday.id + " / " + weekday.canonical;
  }

  function setText(id, value) {
    const node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  function renderToday() {
    setText("today-te", T.formatTredecadia(todayTredecadia));
    setText("today-description", describeTredecadia(todayTredecadia));
    setText("today-gregorian", "Gregorian " + T.formatGregorian(todayGregorian));
  }

  function populateMonthSelect() {
    const select = $("#calendar-month");
    select.innerHTML = "";
    T.MONTHS.forEach((month) => {
      const option = document.createElement("option");
      option.value = String(month.number);
      option.textContent = String(month.number).padStart(2, "0") + " · " + month.canonical;
      select.appendChild(option);
    });
  }

  function updateSelectedDetail(value) {
    const panel = $("#selected-date");
    const te = T.formatTredecadia(value);
    const gregorian = T.toGregorian(value);
    let detail = describeTredecadia(value);

    if (!value.special) {
      const weekday = T.weekdayForDay(value.day);
      detail += " · day " + value.day + " / 28";
      setText("selected-weekday", weekday.id + " · " + weekday.canonical);
    } else {
      setText("selected-weekday", "Outside the weekday cycle");
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
    button.innerHTML = "<strong>" + label + "</strong><span>" + T.formatGregorian(T.toGregorian(value)) + "</span>";
    button.addEventListener("click", () => updateSelectedDetail(value));
    return button;
  }

  function renderIntercalary() {
    const container = $("#intercalary-days");
    container.innerHTML = "";
    container.appendChild(
      specialButton("EQ · Equinox / New Year Day", { year: selectedYear, special: "EQ" }, "eq")
    );
    if (T.tredecadiaIsLeap(selectedYear)) {
      container.appendChild(
        specialButton("ED · Earth Day", { year: selectedYear, special: "ED" }, "ed")
      );
    } else {
      const ordinary = document.createElement("div");
      ordinary.className = "special-day muted";
      ordinary.innerHTML = "<strong>No Earth Day</strong><span>ordinary Tredecadia year</span>";
      container.appendChild(ordinary);
    }
  }

  function renderCalendar() {
    const month = monthRecord(selectedMonth);
    $("#calendar-year").value = String(selectedYear);
    $("#calendar-month").value = String(selectedMonth);
    setText("calendar-title", String(selectedMonth).padStart(2, "0") + " · " + month.canonical);
    setText("calendar-subtitle", "TE " + T.formatDisplayYear(selectedYear) + " · " + month.short6 + " · " + month.short4);

    const grid = $("#calendar-grid");
    grid.innerHTML = "";

    T.WEEKDAYS.forEach((weekday) => {
      const head = document.createElement("div");
      head.className = "weekday-head";
      head.innerHTML = "<strong>" + weekday.canonical + "</strong><span>" + weekday.id + "</span>";
      grid.appendChild(head);
    });

    for (let day = 1; day <= 28; day += 1) {
      const value = { year: selectedYear, month: selectedMonth, day };
      const gregorian = T.toGregorian(value);
      const button = document.createElement("button");
      button.type = "button";
      button.className = "calendar-day";
      button.dataset.day = String(day);
      button.setAttribute(
        "aria-label",
        T.formatTredecadia(value) + ", " + T.weekdayForDay(day).canonical + ", Gregorian " + T.formatGregorian(gregorian)
      );
      button.innerHTML =
        "<span class=\"day-number\">" + String(day).padStart(2, "0") + "</span>" +
        "<span class=\"gregorian-mini\">G " + compactGregorian(gregorian) + "</span>";

      if (!todayTredecadia.special && sameTredecadia(value, todayTredecadia)) {
        button.classList.add("is-today");
        button.title = "Today";
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
    let index = (selectedYear * 13 + (selectedMonth - 1)) + delta;
    selectedYear = Math.floor(index / 13);
    selectedMonth = ((index % 13) + 13) % 13 + 1;
    selectedDay = Math.min(selectedDay, 28);
    renderCalendar();
  }

  function goToday() {
    selectedYear = todayTredecadia.year;
    selectedMonth = todayTredecadia.month || (todayTredecadia.special === "ED" ? 13 : 1);
    selectedDay = todayTredecadia.day || 1;
    renderCalendar();
    updateSelectedDetail(todayTredecadia);
  }

  function showResult(target, primary, secondary, isError) {
    const node = $(target);
    node.classList.toggle("is-error", Boolean(isError));
    node.innerHTML = "";
    const strong = document.createElement("strong");
    strong.textContent = primary;
    const span = document.createElement("span");
    span.textContent = secondary || "";
    node.append(strong, span);
  }

  function bindConverters() {
    const gInput = $("#gregorian-input");
    const tInput = $("#tredecadia-input");

    gInput.value = T.formatGregorian(todayGregorian);
    tInput.value = T.formatTredecadia(todayTredecadia);

    $("#gregorian-form").addEventListener("submit", (event) => {
      event.preventDefault();
      try {
        const gregorian = T.parseGregorian(gInput.value.trim());
        const te = T.fromGregorian(gregorian);
        showResult("#gregorian-result", T.formatTredecadia(te), describeTredecadia(te), false);
      } catch (error) {
        showResult("#gregorian-result", "Invalid Gregorian date", error.message, true);
      }
    });

    $("#tredecadia-form").addEventListener("submit", (event) => {
      event.preventDefault();
      try {
        const te = T.parseTredecadia(tInput.value.trim());
        const gregorian = T.toGregorian(te);
        showResult("#tredecadia-result", T.formatGregorian(gregorian), describeTredecadia(te), false);
      } catch (error) {
        showResult("#tredecadia-result", "Invalid Tredecadia date", error.message, true);
      }
    });

    $("#gregorian-form").requestSubmit();
    $("#tredecadia-form").requestSubmit();
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
      if (!Number.isSafeInteger(value)) {
        event.target.setCustomValidity("Enter an integer Tredecadia year.");
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
    renderToday();
    populateMonthSelect();
    bindControls();
    bindConverters();
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
      message.textContent = "Interactive calendar could not start. The static Tredecadia specification below is still available.";
      root.prepend(message);
    }
  }
})();
