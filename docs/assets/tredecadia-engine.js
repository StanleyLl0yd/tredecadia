// SPDX-License-Identifier: MIT
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    root.Tredecadia = api;
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  const TE_GREGORIAN_YEAR_OFFSET = 9999;
  const GREGORIAN_MONTH_LENGTHS = Object.freeze([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]);

  const MONTHS = Object.freeze([
    { number: 1, canonical: "Masanumika", short6: "Masanu", short4: "Masa" },
    { number: 2, canonical: "Tasuzunumu", short6: "Tasuzu", short4: "Tasu" },
    { number: 3, canonical: "Nazumasanu", short6: "Nazuma", short4: "Nazu" },
    { number: 4, canonical: "Mikasumani", short6: "Mikasu", short4: "Mika" },
    { number: 5, canonical: "Yanimuzunu", short6: "Yanimu", short4: "Yani" },
    { number: 6, canonical: "Zumitanasu", short6: "Zumita", short4: "Zumi" },
    { number: 7, canonical: "Muyasanumi", short6: "Muyasa", short4: "Muya" },
    { number: 8, canonical: "Sunizusaka", short6: "Sunizu", short4: "Suni" },
    { number: 9, canonical: "Numanamuta", short6: "Numana", short4: "Numa" },
    { number: 10, canonical: "Kazunusuya", short6: "Kazunu", short4: "Kazu" },
    { number: 11, canonical: "Yanazumasa", short6: "Yanazu", short4: "Yana" },
    { number: 12, canonical: "Sanumikazu", short6: "Sanumi", short4: "Sanu" },
    { number: 13, canonical: "Nimutazuna", short6: "Nimuta", short4: "Nimu" },
  ]);

  const WEEKDAYS = Object.freeze([
    { id: "W1", canonical: "Mene" },
    { id: "W2", canonical: "Noko" },
    { id: "W3", canonical: "Kese" },
    { id: "W4", canonical: "Zoyo" },
    { id: "W5", canonical: "Sote" },
    { id: "W6", canonical: "Yemo" },
    { id: "W7", canonical: "Toze" },
  ]);

  function assertInteger(value, label) {
    if (!Number.isSafeInteger(value)) {
      throw new RangeError(label + " must be a safe integer");
    }
  }

  function gregorianIsLeap(year) {
    assertInteger(year, "Gregorian year");
    return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
  }

  function tredecadiaIsLeap(year) {
    assertInteger(year, "Tredecadia year");
    return gregorianIsLeap(year - 9998);
  }

  function gregorianMonthLength(year, month) {
    assertInteger(year, "Gregorian year");
    assertInteger(month, "Gregorian month");
    if (month < 1 || month > 12) {
      throw new RangeError("Gregorian month must be in 1..12");
    }
    if (month === 2 && gregorianIsLeap(year)) {
      return 29;
    }
    return GREGORIAN_MONTH_LENGTHS[month - 1];
  }

  function validateGregorian(value) {
    const { year, month, day } = value;
    assertInteger(year, "Gregorian year");
    assertInteger(month, "Gregorian month");
    assertInteger(day, "Gregorian day");
    const length = gregorianMonthLength(year, month);
    if (day < 1 || day > length) {
      throw new RangeError("invalid Gregorian day");
    }
    return value;
  }

  function daysBeforeGregorianYear(year) {
    assertInteger(year, "Gregorian year");
    const y = year - 1;
    return 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400);
  }

  function gregorianOrdinal(year, month, day) {
    validateGregorian({ year, month, day });
    let ordinal = daysBeforeGregorianYear(year);
    for (let m = 1; m < month; m += 1) {
      ordinal += gregorianMonthLength(year, m);
    }
    return ordinal + day - 1;
  }

  function gregorianFromOrdinal(ordinal) {
    assertInteger(ordinal, "Gregorian ordinal");
    const cycle = Math.floor(ordinal / 146097);
    let lo = cycle * 400 + 1;
    let hi = lo + 399;

    while (lo < hi) {
      const mid = Math.floor((lo + hi + 1) / 2);
      if (daysBeforeGregorianYear(mid) <= ordinal) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }

    const year = lo;
    let dayOfYear = ordinal - daysBeforeGregorianYear(year);
    let month = 1;

    while (true) {
      const length = gregorianMonthLength(year, month);
      if (dayOfYear < length) {
        return { year, month, day: dayOfYear + 1 };
      }
      dayOfYear -= length;
      month += 1;
    }
  }

  function formatYear(year) {
    assertInteger(year, "Tredecadia year");
    const magnitude = String(Math.abs(year)).padStart(5, "0");
    return year < 0 ? "-" + magnitude : magnitude;
  }

  function formatDisplayYear(year) {
    assertInteger(year, "Tredecadia year");
    return year < 0 ? "−" + Math.abs(year) : String(year);
  }

  function formatGregorianYear(year) {
    assertInteger(year, "Gregorian year");
    const magnitude = String(Math.abs(year)).padStart(4, "0");
    return year < 0 ? "-" + magnitude : magnitude;
  }

  function formatGregorian(value) {
    validateGregorian(value);
    return formatGregorianYear(value.year) + "-" + String(value.month).padStart(2, "0") + "-" + String(value.day).padStart(2, "0");
  }

  function validateTredecadia(value) {
    assertInteger(value.year, "Tredecadia year");
    if (value.special != null) {
      if (value.special !== "EQ" && value.special !== "ED") {
        throw new RangeError("special date must be EQ or ED");
      }
      if (value.special === "ED" && !tredecadiaIsLeap(value.year)) {
        throw new RangeError("Earth Day exists only in a leap Tredecadia year");
      }
      return value;
    }

    assertInteger(value.month, "Tredecadia month");
    assertInteger(value.day, "Tredecadia day");
    if (value.month < 1 || value.month > 13) {
      throw new RangeError("Tredecadia month must be in 1..13");
    }
    if (value.day < 1 || value.day > 28) {
      throw new RangeError("Tredecadia day must be in 1..28");
    }
    return value;
  }

  function formatTredecadia(value) {
    validateTredecadia(value);
    const year = formatYear(value.year);
    if (value.special != null) {
      return year + "-" + value.special;
    }
    return year + "-" + String(value.month).padStart(2, "0") + "-" + String(value.day).padStart(2, "0");
  }

  function parseGregorian(text) {
    const match = /^(-?[0-9]+)-([0-9]{2})-([0-9]{2})$/.exec(text);
    if (!match) {
      throw new RangeError("Use astronomical Gregorian YYYY-MM-DD, for example 2026-09-18 or -9999-03-20.");
    }
    const value = { year: Number(match[1]), month: Number(match[2]), day: Number(match[3]) };
    return validateGregorian(value);
  }

  function parseTredecadia(text) {
    const match = /^(-?[0-9]{5,})-(?:([0-9]{2})-([0-9]{2})|(EQ|ED))$/.exec(text);
    if (!match) {
      throw new RangeError("Use canonical Tredecadia notation, for example 12025-07-14 or 00000-EQ.");
    }

    const yearField = match[1];
    const year = Number(yearField);
    assertInteger(year, "Tredecadia year");
    if (formatYear(year) !== yearField) {
      throw new RangeError("Tredecadia year field is not canonical.");
    }

    if (match[4]) {
      return validateTredecadia({ year, special: match[4] });
    }
    return validateTredecadia({ year, month: Number(match[2]), day: Number(match[3]) });
  }

  function toGregorian(value) {
    validateTredecadia(value);
    const startYear = value.year - TE_GREGORIAN_YEAR_OFFSET;

    if (value.special === "EQ") {
      return { year: startYear, month: 3, day: 20 };
    }
    if (value.special === "ED") {
      return { year: startYear + 1, month: 3, day: 19 };
    }

    const regularOffset = (value.month - 1) * 28 + value.day - 1;
    const ordinal = gregorianOrdinal(startYear, 3, 21) + regularOffset;
    return gregorianFromOrdinal(ordinal);
  }

  function fromGregorian(value) {
    validateGregorian(value);
    const afterBoundary = value.month > 3 || (value.month === 3 && value.day >= 20);
    const year = value.year + (afterBoundary ? 9999 : 9998);
    const startGregorianYear = year - 9999;
    const start = gregorianOrdinal(startGregorianYear, 3, 20);
    const delta = gregorianOrdinal(value.year, value.month, value.day) - start;

    if (delta === 0) {
      return { year, special: "EQ" };
    }
    if (delta >= 1 && delta <= 364) {
      const zeroBased = delta - 1;
      return {
        year,
        month: Math.floor(zeroBased / 28) + 1,
        day: (zeroBased % 28) + 1,
      };
    }
    if (delta === 365 && tredecadiaIsLeap(year)) {
      return { year, special: "ED" };
    }
    throw new Error("derived Gregorian date is outside its Tredecadia year");
  }

  function weekdayForDay(day) {
    assertInteger(day, "Tredecadia day");
    if (day < 1 || day > 28) {
      throw new RangeError("Tredecadia day must be in 1..28");
    }
    return WEEKDAYS[(day - 1) % 7];
  }

  return Object.freeze({
    TE_GREGORIAN_YEAR_OFFSET,
    MONTHS,
    WEEKDAYS,
    gregorianIsLeap,
    tredecadiaIsLeap,
    gregorianMonthLength,
    gregorianOrdinal,
    gregorianFromOrdinal,
    formatYear,
    formatDisplayYear,
    formatGregorianYear,
    formatGregorian,
    formatTredecadia,
    parseGregorian,
    parseTredecadia,
    toGregorian,
    fromGregorian,
    weekdayForDay,
  });
});
