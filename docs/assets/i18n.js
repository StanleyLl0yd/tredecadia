// SPDX-License-Identifier: MIT
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    root.TredecadiaI18n = api;
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  const STORAGE_KEY = "tredecadia-display-language";
  const LOCALES = Object.freeze({
  "en": {
    "name": "English",
    "dir": "ltr",
    "readme": "README.md",
    "s": {
      "tagline": "A 13 × 28 perennial calendar standard.",
      "displayLanguage": "Display language",
      "autoSystem": "Auto (system)",
      "documentation": "Documentation",
      "footerSource": "The GitHub repository is the canonical source.",
      "interactiveCalendar": "Interactive calendar",
      "todayInTredecadia": "Today in Tredecadia",
      "selectedDate": "Selected date",
      "gregorian": "Gregorian",
      "previous": "← Previous",
      "today": "Today",
      "month": "Month",
      "teYear": "TE year",
      "next": "Next →",
      "tredecadiaMonth": "Tredecadia month",
      "eqName": "Equinox / New Year Day",
      "edName": "Earth Day",
      "noEarthDay": "No Earth Day",
      "ordinaryYear": "ordinary Tredecadia year",
      "outsideWeekdayCycle": "Outside the weekday cycle",
      "dayOf": "day {day} / 28",
      "gregorianToTredecadia": "Gregorian → Tredecadia",
      "convertCivilDate": "Convert a civil date",
      "gregorianDate": "Gregorian date",
      "gregorianHelp": "Astronomical year numbering is supported, including year 0 and negative years.",
      "convert": "Convert",
      "tredecadiaToGregorian": "Tredecadia → Gregorian",
      "convertTeDate": "Convert a canonical TE date",
      "tredecadiaDate": "Tredecadia date",
      "tredecadiaHelp": "Use canonical forms such as 12025-07-14, 00000-EQ, or 09998-ED.",
      "widgetNote": "The widget is a convenience implementation. The specifications and machine-readable registries remain normative. “Today” uses the browser’s local civil date.",
      "invalidGregorian": "Invalid Gregorian date",
      "invalidTredecadia": "Invalid Tredecadia date",
      "enterIntegerYear": "Enter an integer Tredecadia year.",
      "loading": "Loading…"
    }
  },
  "ru": {
    "name": "Русский",
    "dir": "ltr",
    "readme": "README.ru.md",
    "s": {
      "tagline": "Вечный календарь 13 × 28.",
      "displayLanguage": "Язык отображения",
      "autoSystem": "Авто (язык системы)",
      "documentation": "Документация",
      "footerSource": "Канонический источник — репозиторий GitHub.",
      "interactiveCalendar": "Интерактивный календарь",
      "todayInTredecadia": "Сегодня в Tredecadia",
      "selectedDate": "Выбранная дата",
      "gregorian": "Григорианская дата",
      "previous": "← Назад",
      "today": "Сегодня",
      "month": "Месяц",
      "teYear": "Год TE",
      "next": "Вперёд →",
      "tredecadiaMonth": "Месяц Tredecadia",
      "eqName": "День равноденствия / Новый год",
      "edName": "День Земли",
      "noEarthDay": "Без Дня Земли",
      "ordinaryYear": "обычный год Tredecadia",
      "outsideWeekdayCycle": "Вне недельного цикла",
      "dayOf": "день {day} / 28",
      "gregorianToTredecadia": "Григорианская → Tredecadia",
      "convertCivilDate": "Преобразовать гражданскую дату",
      "gregorianDate": "Григорианская дата",
      "gregorianHelp": "Поддерживается астрономическая нумерация лет, включая год 0 и отрицательные годы.",
      "convert": "Преобразовать",
      "tredecadiaToGregorian": "Tredecadia → Григорианская",
      "convertTeDate": "Преобразовать каноническую дату TE",
      "tredecadiaDate": "Дата Tredecadia",
      "tredecadiaHelp": "Используйте канонические формы: 12025-07-14, 00000-EQ или 09998-ED.",
      "widgetNote": "Виджет — вспомогательная реализация. Нормативными остаются спецификации и машиночитаемые реестры. «Сегодня» определяется по локальной дате браузера.",
      "invalidGregorian": "Некорректная григорианская дата",
      "invalidTredecadia": "Некорректная дата Tredecadia",
      "enterIntegerYear": "Введите целый год Tredecadia.",
      "loading": "Загрузка…"
    }
  },
  "es": {
    "name": "Español",
    "dir": "ltr",
    "readme": "README.es.md",
    "s": {
      "tagline": "Un calendario perpetuo de 13 × 28.",
      "displayLanguage": "Idioma de visualización",
      "autoSystem": "Automático (sistema)",
      "documentation": "Documentación",
      "footerSource": "El repositorio de GitHub es la fuente canónica.",
      "interactiveCalendar": "Calendario interactivo",
      "todayInTredecadia": "Hoy en Tredecadia",
      "selectedDate": "Fecha seleccionada",
      "gregorian": "Gregoriano",
      "previous": "← Anterior",
      "today": "Hoy",
      "month": "Mes",
      "teYear": "Año TE",
      "next": "Siguiente →",
      "tredecadiaMonth": "Mes de Tredecadia",
      "eqName": "Equinoccio / Año Nuevo",
      "edName": "Día de la Tierra",
      "noEarthDay": "Sin Día de la Tierra",
      "ordinaryYear": "año ordinario de Tredecadia",
      "outsideWeekdayCycle": "Fuera del ciclo semanal",
      "dayOf": "día {day} / 28",
      "gregorianToTredecadia": "Gregoriano → Tredecadia",
      "convertCivilDate": "Convertir una fecha civil",
      "gregorianDate": "Fecha gregoriana",
      "gregorianHelp": "Se admite numeración astronómica, incluido el año 0 y años negativos.",
      "convert": "Convertir",
      "tredecadiaToGregorian": "Tredecadia → Gregoriano",
      "convertTeDate": "Convertir una fecha TE canónica",
      "tredecadiaDate": "Fecha Tredecadia",
      "tredecadiaHelp": "Use formas canónicas como 12025-07-14, 00000-EQ o 09998-ED.",
      "widgetNote": "El widget es una implementación auxiliar. Las especificaciones y registros legibles por máquina siguen siendo normativos. «Hoy» usa la fecha civil local del navegador.",
      "invalidGregorian": "Fecha gregoriana no válida",
      "invalidTredecadia": "Fecha Tredecadia no válida",
      "enterIntegerYear": "Introduzca un año Tredecadia entero.",
      "loading": "Cargando…"
    }
  },
  "pt-BR": {
    "name": "Português (Brasil)",
    "dir": "ltr",
    "readme": "README.pt-BR.md",
    "s": {
      "tagline": "Um calendário perpétuo de 13 × 28.",
      "displayLanguage": "Idioma de exibição",
      "autoSystem": "Automático (sistema)",
      "documentation": "Documentação",
      "footerSource": "O repositório GitHub é a fonte canônica.",
      "interactiveCalendar": "Calendário interativo",
      "todayInTredecadia": "Hoje em Tredecadia",
      "selectedDate": "Data selecionada",
      "gregorian": "Gregoriano",
      "previous": "← Anterior",
      "today": "Hoje",
      "month": "Mês",
      "teYear": "Ano TE",
      "next": "Próximo →",
      "tredecadiaMonth": "Mês Tredecadia",
      "eqName": "Equinócio / Ano-Novo",
      "edName": "Dia da Terra",
      "noEarthDay": "Sem Dia da Terra",
      "ordinaryYear": "ano comum de Tredecadia",
      "outsideWeekdayCycle": "Fora do ciclo semanal",
      "dayOf": "dia {day} / 28",
      "gregorianToTredecadia": "Gregoriano → Tredecadia",
      "convertCivilDate": "Converter uma data civil",
      "gregorianDate": "Data gregoriana",
      "gregorianHelp": "A numeração astronômica é aceita, incluindo o ano 0 e anos negativos.",
      "convert": "Converter",
      "tredecadiaToGregorian": "Tredecadia → Gregoriano",
      "convertTeDate": "Converter uma data TE canônica",
      "tredecadiaDate": "Data Tredecadia",
      "tredecadiaHelp": "Use formas canônicas como 12025-07-14, 00000-EQ ou 09998-ED.",
      "widgetNote": "O widget é uma implementação auxiliar. As especificações e registros legíveis por máquina continuam normativos. “Hoje” usa a data civil local do navegador.",
      "invalidGregorian": "Data gregoriana inválida",
      "invalidTredecadia": "Data Tredecadia inválida",
      "enterIntegerYear": "Digite um ano Tredecadia inteiro.",
      "loading": "Carregando…"
    }
  },
  "fr": {
    "name": "Français",
    "dir": "ltr",
    "readme": "README.fr.md",
    "s": {
      "tagline": "Un calendrier perpétuel de 13 × 28.",
      "displayLanguage": "Langue d’affichage",
      "autoSystem": "Auto (système)",
      "documentation": "Documentation",
      "footerSource": "Le dépôt GitHub est la source canonique.",
      "interactiveCalendar": "Calendrier interactif",
      "todayInTredecadia": "Aujourd’hui dans Tredecadia",
      "selectedDate": "Date sélectionnée",
      "gregorian": "Grégorien",
      "previous": "← Précédent",
      "today": "Aujourd’hui",
      "month": "Mois",
      "teYear": "Année TE",
      "next": "Suivant →",
      "tredecadiaMonth": "Mois Tredecadia",
      "eqName": "Équinoxe / Nouvel An",
      "edName": "Jour de la Terre",
      "noEarthDay": "Pas de Jour de la Terre",
      "ordinaryYear": "année ordinaire Tredecadia",
      "outsideWeekdayCycle": "Hors du cycle hebdomadaire",
      "dayOf": "jour {day} / 28",
      "gregorianToTredecadia": "Grégorien → Tredecadia",
      "convertCivilDate": "Convertir une date civile",
      "gregorianDate": "Date grégorienne",
      "gregorianHelp": "La numérotation astronomique est prise en charge, y compris l’année 0 et les années négatives.",
      "convert": "Convertir",
      "tredecadiaToGregorian": "Tredecadia → Grégorien",
      "convertTeDate": "Convertir une date TE canonique",
      "tredecadiaDate": "Date Tredecadia",
      "tredecadiaHelp": "Utilisez des formes canoniques comme 12025-07-14, 00000-EQ ou 09998-ED.",
      "widgetNote": "Le widget est une implémentation pratique. Les spécifications et registres lisibles par machine restent normatifs. « Aujourd’hui » utilise la date civile locale du navigateur.",
      "invalidGregorian": "Date grégorienne invalide",
      "invalidTredecadia": "Date Tredecadia invalide",
      "enterIntegerYear": "Saisissez une année Tredecadia entière.",
      "loading": "Chargement…"
    }
  },
  "de": {
    "name": "Deutsch",
    "dir": "ltr",
    "readme": "README.de.md",
    "s": {
      "tagline": "Ein immerwährender 13 × 28-Kalender.",
      "displayLanguage": "Anzeigesprache",
      "autoSystem": "Automatisch (System)",
      "documentation": "Dokumentation",
      "footerSource": "Das GitHub-Repository ist die kanonische Quelle.",
      "interactiveCalendar": "Interaktiver Kalender",
      "todayInTredecadia": "Heute in Tredecadia",
      "selectedDate": "Ausgewähltes Datum",
      "gregorian": "Gregorianisch",
      "previous": "← Zurück",
      "today": "Heute",
      "month": "Monat",
      "teYear": "TE-Jahr",
      "next": "Weiter →",
      "tredecadiaMonth": "Tredecadia-Monat",
      "eqName": "Tagundnachtgleiche / Neujahr",
      "edName": "Tag der Erde",
      "noEarthDay": "Kein Tag der Erde",
      "ordinaryYear": "gewöhnliches Tredecadia-Jahr",
      "outsideWeekdayCycle": "Außerhalb des Wochenzyklus",
      "dayOf": "Tag {day} / 28",
      "gregorianToTredecadia": "Gregorianisch → Tredecadia",
      "convertCivilDate": "Zivildatum umrechnen",
      "gregorianDate": "Gregorianisches Datum",
      "gregorianHelp": "Astronomische Jahreszählung einschließlich Jahr 0 und negativer Jahre wird unterstützt.",
      "convert": "Umrechnen",
      "tredecadiaToGregorian": "Tredecadia → Gregorianisch",
      "convertTeDate": "Kanonisches TE-Datum umrechnen",
      "tredecadiaDate": "Tredecadia-Datum",
      "tredecadiaHelp": "Verwenden Sie kanonische Formen wie 12025-07-14, 00000-EQ oder 09998-ED.",
      "widgetNote": "Das Widget ist eine Hilfsimplementierung. Spezifikationen und maschinenlesbare Register bleiben normativ. „Heute“ verwendet das lokale zivile Datum des Browsers.",
      "invalidGregorian": "Ungültiges gregorianisches Datum",
      "invalidTredecadia": "Ungültiges Tredecadia-Datum",
      "enterIntegerYear": "Geben Sie ein ganzzahliges Tredecadia-Jahr ein.",
      "loading": "Wird geladen…"
    }
  },
  "it": {
    "name": "Italiano",
    "dir": "ltr",
    "readme": "README.it.md",
    "s": {
      "tagline": "Un calendario perpetuo 13 × 28.",
      "displayLanguage": "Lingua di visualizzazione",
      "autoSystem": "Automatico (sistema)",
      "documentation": "Documentazione",
      "footerSource": "Il repository GitHub è la fonte canonica.",
      "interactiveCalendar": "Calendario interattivo",
      "todayInTredecadia": "Oggi in Tredecadia",
      "selectedDate": "Data selezionata",
      "gregorian": "Gregoriano",
      "previous": "← Precedente",
      "today": "Oggi",
      "month": "Mese",
      "teYear": "Anno TE",
      "next": "Successivo →",
      "tredecadiaMonth": "Mese Tredecadia",
      "eqName": "Equinozio / Capodanno",
      "edName": "Giornata della Terra",
      "noEarthDay": "Nessuna Giornata della Terra",
      "ordinaryYear": "anno ordinario Tredecadia",
      "outsideWeekdayCycle": "Fuori dal ciclo settimanale",
      "dayOf": "giorno {day} / 28",
      "gregorianToTredecadia": "Gregoriano → Tredecadia",
      "convertCivilDate": "Converti una data civile",
      "gregorianDate": "Data gregoriana",
      "gregorianHelp": "È supportata la numerazione astronomica, incluso l’anno 0 e gli anni negativi.",
      "convert": "Converti",
      "tredecadiaToGregorian": "Tredecadia → Gregoriano",
      "convertTeDate": "Converti una data TE canonica",
      "tredecadiaDate": "Data Tredecadia",
      "tredecadiaHelp": "Usa forme canoniche come 12025-07-14, 00000-EQ o 09998-ED.",
      "widgetNote": "Il widget è un’implementazione di servizio. Specifiche e registri leggibili dalla macchina restano normativi. “Oggi” usa la data civile locale del browser.",
      "invalidGregorian": "Data gregoriana non valida",
      "invalidTredecadia": "Data Tredecadia non valida",
      "enterIntegerYear": "Inserisci un anno Tredecadia intero.",
      "loading": "Caricamento…"
    }
  },
  "tr": {
    "name": "Türkçe",
    "dir": "ltr",
    "readme": "README.tr.md",
    "s": {
      "tagline": "13 × 28 kalıcı takvim standardı.",
      "displayLanguage": "Görüntüleme dili",
      "autoSystem": "Otomatik (sistem)",
      "documentation": "Belgeler",
      "footerSource": "Kanonik kaynak GitHub deposudur.",
      "interactiveCalendar": "Etkileşimli takvim",
      "todayInTredecadia": "Bugün Tredecadia’da",
      "selectedDate": "Seçili tarih",
      "gregorian": "Gregoryen",
      "previous": "← Önceki",
      "today": "Bugün",
      "month": "Ay",
      "teYear": "TE yılı",
      "next": "Sonraki →",
      "tredecadiaMonth": "Tredecadia ayı",
      "eqName": "Ekinoks / Yeni Yıl",
      "edName": "Dünya Günü",
      "noEarthDay": "Dünya Günü yok",
      "ordinaryYear": "normal Tredecadia yılı",
      "outsideWeekdayCycle": "Hafta döngüsünün dışında",
      "dayOf": "gün {day} / 28",
      "gregorianToTredecadia": "Gregoryen → Tredecadia",
      "convertCivilDate": "Sivil tarihi dönüştür",
      "gregorianDate": "Gregoryen tarih",
      "gregorianHelp": "0 yılı ve negatif yıllar dahil astronomik yıl numaralandırması desteklenir.",
      "convert": "Dönüştür",
      "tredecadiaToGregorian": "Tredecadia → Gregoryen",
      "convertTeDate": "Kanonik TE tarihini dönüştür",
      "tredecadiaDate": "Tredecadia tarihi",
      "tredecadiaHelp": "12025-07-14, 00000-EQ veya 09998-ED gibi kanonik biçimleri kullanın.",
      "widgetNote": "Bu araç yardımcı bir uygulamadır. Spesifikasyonlar ve makinece okunabilir kayıtlar normatif kalır. “Bugün” tarayıcının yerel sivil tarihini kullanır.",
      "invalidGregorian": "Geçersiz Gregoryen tarih",
      "invalidTredecadia": "Geçersiz Tredecadia tarihi",
      "enterIntegerYear": "Tam sayı bir Tredecadia yılı girin.",
      "loading": "Yükleniyor…"
    }
  },
  "pl": {
    "name": "Polski",
    "dir": "ltr",
    "readme": "README.pl.md",
    "s": {
      "tagline": "Wieczny kalendarz 13 × 28.",
      "displayLanguage": "Język wyświetlania",
      "autoSystem": "Automatycznie (system)",
      "documentation": "Dokumentacja",
      "footerSource": "Repozytorium GitHub jest źródłem kanonicznym.",
      "interactiveCalendar": "Kalendarz interaktywny",
      "todayInTredecadia": "Dziś w Tredecadii",
      "selectedDate": "Wybrana data",
      "gregorian": "Gregoriański",
      "previous": "← Poprzedni",
      "today": "Dzisiaj",
      "month": "Miesiąc",
      "teYear": "Rok TE",
      "next": "Następny →",
      "tredecadiaMonth": "Miesiąc Tredecadii",
      "eqName": "Równonoc / Nowy Rok",
      "edName": "Dzień Ziemi",
      "noEarthDay": "Brak Dnia Ziemi",
      "ordinaryYear": "zwykły rok Tredecadii",
      "outsideWeekdayCycle": "Poza cyklem tygodnia",
      "dayOf": "dzień {day} / 28",
      "gregorianToTredecadia": "Gregoriański → Tredecadia",
      "convertCivilDate": "Przelicz datę cywilną",
      "gregorianDate": "Data gregoriańska",
      "gregorianHelp": "Obsługiwana jest astronomiczna numeracja lat, w tym rok 0 i lata ujemne.",
      "convert": "Przelicz",
      "tredecadiaToGregorian": "Tredecadia → Gregoriański",
      "convertTeDate": "Przelicz kanoniczną datę TE",
      "tredecadiaDate": "Data Tredecadii",
      "tredecadiaHelp": "Użyj form kanonicznych, np. 12025-07-14, 00000-EQ lub 09998-ED.",
      "widgetNote": "Widżet jest implementacją pomocniczą. Specyfikacje i rejestry maszynowe pozostają normatywne. „Dzisiaj” używa lokalnej daty cywilnej przeglądarki.",
      "invalidGregorian": "Nieprawidłowa data gregoriańska",
      "invalidTredecadia": "Nieprawidłowa data Tredecadii",
      "enterIntegerYear": "Wprowadź całkowity rok Tredecadii.",
      "loading": "Ładowanie…"
    }
  },
  "uk": {
    "name": "Українська",
    "dir": "ltr",
    "readme": "README.uk.md",
    "s": {
      "tagline": "Вічний календар 13 × 28.",
      "displayLanguage": "Мова відображення",
      "autoSystem": "Авто (система)",
      "documentation": "Документація",
      "footerSource": "Канонічне джерело — репозиторій GitHub.",
      "interactiveCalendar": "Інтерактивний календар",
      "todayInTredecadia": "Сьогодні в Tredecadia",
      "selectedDate": "Вибрана дата",
      "gregorian": "Григоріанська",
      "previous": "← Назад",
      "today": "Сьогодні",
      "month": "Місяць",
      "teYear": "Рік TE",
      "next": "Вперед →",
      "tredecadiaMonth": "Місяць Tredecadia",
      "eqName": "Рівнодення / Новий рік",
      "edName": "День Землі",
      "noEarthDay": "Без Дня Землі",
      "ordinaryYear": "звичайний рік Tredecadia",
      "outsideWeekdayCycle": "Поза тижневим циклом",
      "dayOf": "день {day} / 28",
      "gregorianToTredecadia": "Григоріанська → Tredecadia",
      "convertCivilDate": "Перетворити цивільну дату",
      "gregorianDate": "Григоріанська дата",
      "gregorianHelp": "Підтримується астрономічна нумерація років, включно з роком 0 і від’ємними роками.",
      "convert": "Перетворити",
      "tredecadiaToGregorian": "Tredecadia → Григоріанська",
      "convertTeDate": "Перетворити канонічну дату TE",
      "tredecadiaDate": "Дата Tredecadia",
      "tredecadiaHelp": "Використовуйте канонічні форми: 12025-07-14, 00000-EQ або 09998-ED.",
      "widgetNote": "Віджет є допоміжною реалізацією. Нормативними залишаються специфікації та машинозчитувані реєстри. «Сьогодні» використовує локальну цивільну дату браузера.",
      "invalidGregorian": "Некоректна григоріанська дата",
      "invalidTredecadia": "Некоректна дата Tredecadia",
      "enterIntegerYear": "Введіть цілий рік Tredecadia.",
      "loading": "Завантаження…"
    }
  },
  "ka": {
    "name": "ქართული",
    "dir": "ltr",
    "readme": "README.ka.md",
    "s": {
      "tagline": "13 × 28 მუდმივი კალენდრის სტანდარტი.",
      "displayLanguage": "ჩვენების ენა",
      "autoSystem": "ავტო (სისტემა)",
      "documentation": "დოკუმენტაცია",
      "footerSource": "კანონიკური წყაროა GitHub-ის რეპოზიტორია.",
      "interactiveCalendar": "ინტერაქტიული კალენდარი",
      "todayInTredecadia": "დღეს Tredecadia-ში",
      "selectedDate": "არჩეული თარიღი",
      "gregorian": "გრიგორიანული",
      "previous": "← წინა",
      "today": "დღეს",
      "month": "თვე",
      "teYear": "TE წელი",
      "next": "შემდეგი →",
      "tredecadiaMonth": "Tredecadia-ს თვე",
      "eqName": "ბუნიობა / ახალი წელი",
      "edName": "დედამიწის დღე",
      "noEarthDay": "დედამიწის დღის გარეშე",
      "ordinaryYear": "ჩვეულებრივი Tredecadia წელი",
      "outsideWeekdayCycle": "კვირის ციკლის გარეთ",
      "dayOf": "დღე {day} / 28",
      "gregorianToTredecadia": "გრიგორიანული → Tredecadia",
      "convertCivilDate": "სამოქალაქო თარიღის გარდაქმნა",
      "gregorianDate": "გრიგორიანული თარიღი",
      "gregorianHelp": "მხარდაჭერილია ასტრონომიული წლების ნუმერაცია, მათ შორის 0 და უარყოფითი წლები.",
      "convert": "გარდაქმნა",
      "tredecadiaToGregorian": "Tredecadia → გრიგორიანული",
      "convertTeDate": "კანონიკური TE თარიღის გარდაქმნა",
      "tredecadiaDate": "Tredecadia თარიღი",
      "tredecadiaHelp": "გამოიყენეთ კანონიკური ფორმები: 12025-07-14, 00000-EQ ან 09998-ED.",
      "widgetNote": "ვიჯეტი დამხმარე რეალიზაციაა. სპეციფიკაციები და მანქანურად წაკითხვადი რეესტრები ნორმატიული რჩება. „დღეს“ იყენებს ბრაუზერის ადგილობრივ სამოქალაქო თარიღს.",
      "invalidGregorian": "არასწორი გრიგორიანული თარიღი",
      "invalidTredecadia": "არასწორი Tredecadia თარიღი",
      "enterIntegerYear": "შეიყვანეთ მთელი Tredecadia წელი.",
      "loading": "იტვირთება…"
    }
  },
  "hy": {
    "name": "Հայերեն",
    "dir": "ltr",
    "readme": "README.hy.md",
    "s": {
      "tagline": "13 × 28 մշտական օրացույցի ստանդարտ։",
      "displayLanguage": "Ցուցադրման լեզու",
      "autoSystem": "Ավտոմատ (համակարգ)",
      "documentation": "Փաստաթղթեր",
      "footerSource": "Կանոնական աղբյուրը GitHub պահոցն է։",
      "interactiveCalendar": "Ինտերակտիվ օրացույց",
      "todayInTredecadia": "Այսօր Tredecadia-ում",
      "selectedDate": "Ընտրված ամսաթիվ",
      "gregorian": "Գրիգորյան",
      "previous": "← Նախորդ",
      "today": "Այսօր",
      "month": "Ամիս",
      "teYear": "TE տարի",
      "next": "Հաջորդ →",
      "tredecadiaMonth": "Tredecadia ամիս",
      "eqName": "Գիշերահավասար / Նոր տարի",
      "edName": "Երկրի օր",
      "noEarthDay": "Առանց Երկրի օրվա",
      "ordinaryYear": "սովորական Tredecadia տարի",
      "outsideWeekdayCycle": "Շաբաթական շրջանից դուրս",
      "dayOf": "օր {day} / 28",
      "gregorianToTredecadia": "Գրիգորյան → Tredecadia",
      "convertCivilDate": "Փոխարկել քաղաքացիական ամսաթիվը",
      "gregorianDate": "Գրիգորյան ամսաթիվ",
      "gregorianHelp": "Աջակցվում է աստղագիտական տարեթվերի համարակալումը՝ ներառյալ 0 և բացասական տարիները։",
      "convert": "Փոխարկել",
      "tredecadiaToGregorian": "Tredecadia → Գրիգորյան",
      "convertTeDate": "Փոխարկել կանոնական TE ամսաթիվը",
      "tredecadiaDate": "Tredecadia ամսաթիվ",
      "tredecadiaHelp": "Օգտագործեք կանոնական ձևեր՝ 12025-07-14, 00000-EQ կամ 09998-ED։",
      "widgetNote": "Վիջեթը օժանդակ իրականացում է։ Նորմատիվ են մնում բնութագրերն ու մեքենայական ռեգիստրները։ «Այսօր»-ը օգտագործում է դիտարկչի տեղական քաղաքացիական ամսաթիվը։",
      "invalidGregorian": "Անվավեր գրիգորյան ամսաթիվ",
      "invalidTredecadia": "Անվավեր Tredecadia ամսաթիվ",
      "enterIntegerYear": "Մուտքագրեք ամբողջ Tredecadia տարի։",
      "loading": "Բեռնվում է…"
    }
  },
  "zh-CN": {
    "name": "简体中文",
    "dir": "ltr",
    "readme": "README.zh-CN.md",
    "s": {
      "tagline": "13 × 28 永久历标准。",
      "displayLanguage": "显示语言",
      "autoSystem": "自动（系统）",
      "documentation": "文档",
      "footerSource": "GitHub 仓库是规范来源。",
      "interactiveCalendar": "交互式日历",
      "todayInTredecadia": "今天的 Tredecadia 日期",
      "selectedDate": "所选日期",
      "gregorian": "公历",
      "previous": "← 上一月",
      "today": "今天",
      "month": "月份",
      "teYear": "TE 年",
      "next": "下一月 →",
      "tredecadiaMonth": "Tredecadia 月",
      "eqName": "春分 / 新年日",
      "edName": "地球日",
      "noEarthDay": "无地球日",
      "ordinaryYear": "Tredecadia 平年",
      "outsideWeekdayCycle": "不属于星期循环",
      "dayOf": "第 {day} 天 / 28",
      "gregorianToTredecadia": "公历 → Tredecadia",
      "convertCivilDate": "转换民用日期",
      "gregorianDate": "公历日期",
      "gregorianHelp": "支持天文纪年，包括 0 年和负年份。",
      "convert": "转换",
      "tredecadiaToGregorian": "Tredecadia → 公历",
      "convertTeDate": "转换规范 TE 日期",
      "tredecadiaDate": "Tredecadia 日期",
      "tredecadiaHelp": "请使用规范格式，如 12025-07-14、00000-EQ 或 09998-ED。",
      "widgetNote": "此组件是便捷实现。规范与机器可读注册表仍是权威来源。“今天”使用浏览器的本地民用日期。",
      "invalidGregorian": "无效的公历日期",
      "invalidTredecadia": "无效的 Tredecadia 日期",
      "enterIntegerYear": "请输入整数 Tredecadia 年。",
      "loading": "加载中…"
    }
  },
  "zh-TW": {
    "name": "繁體中文",
    "dir": "ltr",
    "readme": "README.zh-TW.md",
    "s": {
      "tagline": "13 × 28 永久曆標準。",
      "displayLanguage": "顯示語言",
      "autoSystem": "自動（系統）",
      "documentation": "文件",
      "footerSource": "GitHub 儲存庫是規範來源。",
      "interactiveCalendar": "互動式日曆",
      "todayInTredecadia": "今天的 Tredecadia 日期",
      "selectedDate": "所選日期",
      "gregorian": "公曆",
      "previous": "← 上一月",
      "today": "今天",
      "month": "月份",
      "teYear": "TE 年",
      "next": "下一月 →",
      "tredecadiaMonth": "Tredecadia 月",
      "eqName": "春分 / 新年日",
      "edName": "地球日",
      "noEarthDay": "無地球日",
      "ordinaryYear": "Tredecadia 平年",
      "outsideWeekdayCycle": "不屬於星期循環",
      "dayOf": "第 {day} 天 / 28",
      "gregorianToTredecadia": "公曆 → Tredecadia",
      "convertCivilDate": "轉換民用日期",
      "gregorianDate": "公曆日期",
      "gregorianHelp": "支援天文紀年，包括 0 年與負年份。",
      "convert": "轉換",
      "tredecadiaToGregorian": "Tredecadia → 公曆",
      "convertTeDate": "轉換規範 TE 日期",
      "tredecadiaDate": "Tredecadia 日期",
      "tredecadiaHelp": "請使用規範格式，例如 12025-07-14、00000-EQ 或 09998-ED。",
      "widgetNote": "此元件是便捷實作。規範與機器可讀登錄仍為權威來源。「今天」使用瀏覽器的本地民用日期。",
      "invalidGregorian": "無效的公曆日期",
      "invalidTredecadia": "無效的 Tredecadia 日期",
      "enterIntegerYear": "請輸入整數 Tredecadia 年。",
      "loading": "載入中…"
    }
  },
  "ja": {
    "name": "日本語",
    "dir": "ltr",
    "readme": "README.ja.md",
    "s": {
      "tagline": "13 × 28 の永久カレンダー標準。",
      "displayLanguage": "表示言語",
      "autoSystem": "自動（システム）",
      "documentation": "ドキュメント",
      "footerSource": "GitHub リポジトリが正規の情報源です。",
      "interactiveCalendar": "インタラクティブ・カレンダー",
      "todayInTredecadia": "今日の Tredecadia",
      "selectedDate": "選択した日付",
      "gregorian": "グレゴリオ暦",
      "previous": "← 前へ",
      "today": "今日",
      "month": "月",
      "teYear": "TE 年",
      "next": "次へ →",
      "tredecadiaMonth": "Tredecadia の月",
      "eqName": "春分 / 元日",
      "edName": "アースデイ",
      "noEarthDay": "アースデイなし",
      "ordinaryYear": "通常の Tredecadia 年",
      "outsideWeekdayCycle": "曜日サイクル外",
      "dayOf": "{day} 日 / 28",
      "gregorianToTredecadia": "グレゴリオ暦 → Tredecadia",
      "convertCivilDate": "暦日を変換",
      "gregorianDate": "グレゴリオ暦の日付",
      "gregorianHelp": "0 年および負の年を含む天文学的年番号を使用できます。",
      "convert": "変換",
      "tredecadiaToGregorian": "Tredecadia → グレゴリオ暦",
      "convertTeDate": "正規 TE 日付を変換",
      "tredecadiaDate": "Tredecadia 日付",
      "tredecadiaHelp": "12025-07-14、00000-EQ、09998-ED などの正規形式を使用してください。",
      "widgetNote": "このウィジェットは補助実装です。仕様と機械可読レジストリが規範です。「今日」はブラウザのローカル暦日を使用します。",
      "invalidGregorian": "無効なグレゴリオ暦日付",
      "invalidTredecadia": "無効な Tredecadia 日付",
      "enterIntegerYear": "整数の Tredecadia 年を入力してください。",
      "loading": "読み込み中…"
    }
  },
  "ko": {
    "name": "한국어",
    "dir": "ltr",
    "readme": "README.ko.md",
    "s": {
      "tagline": "13 × 28 영구 달력 표준.",
      "displayLanguage": "표시 언어",
      "autoSystem": "자동(시스템)",
      "documentation": "문서",
      "footerSource": "GitHub 저장소가 정식 기준입니다.",
      "interactiveCalendar": "대화형 달력",
      "todayInTredecadia": "오늘의 Tredecadia",
      "selectedDate": "선택한 날짜",
      "gregorian": "그레고리력",
      "previous": "← 이전",
      "today": "오늘",
      "month": "월",
      "teYear": "TE 연도",
      "next": "다음 →",
      "tredecadiaMonth": "Tredecadia 월",
      "eqName": "춘분 / 새해 첫날",
      "edName": "지구의 날",
      "noEarthDay": "지구의 날 없음",
      "ordinaryYear": "일반 Tredecadia 연도",
      "outsideWeekdayCycle": "요일 주기 밖",
      "dayOf": "{day}일 / 28",
      "gregorianToTredecadia": "그레고리력 → Tredecadia",
      "convertCivilDate": "민간 날짜 변환",
      "gregorianDate": "그레고리력 날짜",
      "gregorianHelp": "0년과 음수 연도를 포함한 천문학적 연도 번호를 지원합니다.",
      "convert": "변환",
      "tredecadiaToGregorian": "Tredecadia → 그레고리력",
      "convertTeDate": "정규 TE 날짜 변환",
      "tredecadiaDate": "Tredecadia 날짜",
      "tredecadiaHelp": "12025-07-14, 00000-EQ, 09998-ED 같은 정규 형식을 사용하세요.",
      "widgetNote": "이 위젯은 편의 구현입니다. 규격과 기계 판독 가능 레지스트리가 규범입니다. ‘오늘’은 브라우저의 로컬 민간 날짜를 사용합니다.",
      "invalidGregorian": "잘못된 그레고리력 날짜",
      "invalidTredecadia": "잘못된 Tredecadia 날짜",
      "enterIntegerYear": "정수 Tredecadia 연도를 입력하세요.",
      "loading": "불러오는 중…"
    }
  },
  "ar": {
    "name": "العربية",
    "dir": "rtl",
    "readme": "README.ar.md",
    "s": {
      "tagline": "معيار تقويم دائم 13 × 28.",
      "displayLanguage": "لغة العرض",
      "autoSystem": "تلقائي (النظام)",
      "documentation": "التوثيق",
      "footerSource": "مستودع GitHub هو المصدر المعياري.",
      "interactiveCalendar": "تقويم تفاعلي",
      "todayInTredecadia": "اليوم في Tredecadia",
      "selectedDate": "التاريخ المحدد",
      "gregorian": "الميلادي",
      "previous": "السابق →",
      "today": "اليوم",
      "month": "الشهر",
      "teYear": "سنة TE",
      "next": "← التالي",
      "tredecadiaMonth": "شهر Tredecadia",
      "eqName": "الاعتدال / رأس السنة",
      "edName": "يوم الأرض",
      "noEarthDay": "لا يوجد يوم أرض",
      "ordinaryYear": "سنة Tredecadia عادية",
      "outsideWeekdayCycle": "خارج دورة الأسبوع",
      "dayOf": "اليوم {day} / 28",
      "gregorianToTredecadia": "الميلادي ← Tredecadia",
      "convertCivilDate": "تحويل تاريخ مدني",
      "gregorianDate": "التاريخ الميلادي",
      "gregorianHelp": "يُدعم ترقيم السنوات الفلكي، بما في ذلك السنة 0 والسنوات السالبة.",
      "convert": "تحويل",
      "tredecadiaToGregorian": "Tredecadia ← الميلادي",
      "convertTeDate": "تحويل تاريخ TE معياري",
      "tredecadiaDate": "تاريخ Tredecadia",
      "tredecadiaHelp": "استخدم الصيغ المعيارية مثل 12025-07-14 أو 00000-EQ أو 09998-ED.",
      "widgetNote": "الأداة تنفيذ مساعد. تبقى المواصفات والسجلات المقروءة آليًا هي المرجع المعياري. «اليوم» يستخدم التاريخ المدني المحلي للمتصفح.",
      "invalidGregorian": "تاريخ ميلادي غير صالح",
      "invalidTredecadia": "تاريخ Tredecadia غير صالح",
      "enterIntegerYear": "أدخل سنة Tredecadia صحيحة.",
      "loading": "جارٍ التحميل…"
    }
  },
  "fa": {
    "name": "فارسی",
    "dir": "rtl",
    "readme": "README.fa.md",
    "s": {
      "tagline": "استاندارد تقویم همیشگی ۱۳ × ۲۸.",
      "displayLanguage": "زبان نمایش",
      "autoSystem": "خودکار (سیستم)",
      "documentation": "مستندات",
      "footerSource": "مخزن GitHub منبع معیار است.",
      "interactiveCalendar": "تقویم تعاملی",
      "todayInTredecadia": "امروز در Tredecadia",
      "selectedDate": "تاریخ انتخاب‌شده",
      "gregorian": "میلادی",
      "previous": "قبلی →",
      "today": "امروز",
      "month": "ماه",
      "teYear": "سال TE",
      "next": "← بعدی",
      "tredecadiaMonth": "ماه Tredecadia",
      "eqName": "اعتدال / سال نو",
      "edName": "روز زمین",
      "noEarthDay": "بدون روز زمین",
      "ordinaryYear": "سال عادی Tredecadia",
      "outsideWeekdayCycle": "خارج از چرخه هفته",
      "dayOf": "روز {day} / 28",
      "gregorianToTredecadia": "میلادی ← Tredecadia",
      "convertCivilDate": "تبدیل تاریخ مدنی",
      "gregorianDate": "تاریخ میلادی",
      "gregorianHelp": "شماره‌گذاری نجومی سال‌ها، شامل سال ۰ و سال‌های منفی، پشتیبانی می‌شود.",
      "convert": "تبدیل",
      "tredecadiaToGregorian": "Tredecadia ← میلادی",
      "convertTeDate": "تبدیل تاریخ معیار TE",
      "tredecadiaDate": "تاریخ Tredecadia",
      "tredecadiaHelp": "از قالب‌های معیار مانند 12025-07-14، 00000-EQ یا 09998-ED استفاده کنید.",
      "widgetNote": "این ابزار یک پیاده‌سازی کمکی است. مشخصات و رجیسترهای ماشین‌خوان همچنان معیار هستند. «امروز» از تاریخ مدنی محلی مرورگر استفاده می‌کند.",
      "invalidGregorian": "تاریخ میلادی نامعتبر",
      "invalidTredecadia": "تاریخ Tredecadia نامعتبر",
      "enterIntegerYear": "یک سال صحیح Tredecadia وارد کنید.",
      "loading": "در حال بارگذاری…"
    }
  },
  "hi": {
    "name": "हिन्दी",
    "dir": "ltr",
    "readme": "README.hi.md",
    "s": {
      "tagline": "13 × 28 स्थायी कैलेंडर मानक।",
      "displayLanguage": "प्रदर्शन भाषा",
      "autoSystem": "स्वचालित (सिस्टम)",
      "documentation": "दस्तावेज़",
      "footerSource": "GitHub रिपॉज़िटरी मानक स्रोत है।",
      "interactiveCalendar": "इंटरैक्टिव कैलेंडर",
      "todayInTredecadia": "आज Tredecadia में",
      "selectedDate": "चुनी हुई तारीख",
      "gregorian": "ग्रेगोरियन",
      "previous": "← पिछला",
      "today": "आज",
      "month": "माह",
      "teYear": "TE वर्ष",
      "next": "अगला →",
      "tredecadiaMonth": "Tredecadia माह",
      "eqName": "विषुव / नववर्ष दिवस",
      "edName": "पृथ्वी दिवस",
      "noEarthDay": "पृथ्वी दिवस नहीं",
      "ordinaryYear": "सामान्य Tredecadia वर्ष",
      "outsideWeekdayCycle": "सप्ताह चक्र से बाहर",
      "dayOf": "दिन {day} / 28",
      "gregorianToTredecadia": "ग्रेगोरियन → Tredecadia",
      "convertCivilDate": "नागरिक तारीख बदलें",
      "gregorianDate": "ग्रेगोरियन तारीख",
      "gregorianHelp": "वर्ष 0 और ऋणात्मक वर्षों सहित खगोलीय वर्ष-गणना समर्थित है।",
      "convert": "बदलें",
      "tredecadiaToGregorian": "Tredecadia → ग्रेगोरियन",
      "convertTeDate": "मानक TE तारीख बदलें",
      "tredecadiaDate": "Tredecadia तारीख",
      "tredecadiaHelp": "12025-07-14, 00000-EQ या 09998-ED जैसे मानक रूप उपयोग करें।",
      "widgetNote": "यह विजेट सहायक कार्यान्वयन है। विनिर्देश और मशीन-पठनीय रजिस्टर मानक बने रहते हैं। “आज” ब्राउज़र की स्थानीय नागरिक तारीख का उपयोग करता है।",
      "invalidGregorian": "अमान्य ग्रेगोरियन तारीख",
      "invalidTredecadia": "अमान्य Tredecadia तारीख",
      "enterIntegerYear": "पूर्णांक Tredecadia वर्ष दर्ज करें।",
      "loading": "लोड हो रहा है…"
    }
  },
  "bn": {
    "name": "বাংলা",
    "dir": "ltr",
    "readme": "README.bn.md",
    "s": {
      "tagline": "১৩ × ২৮ চিরস্থায়ী ক্যালেন্ডার মান।",
      "displayLanguage": "প্রদর্শনের ভাষা",
      "autoSystem": "স্বয়ংক্রিয় (সিস্টেম)",
      "documentation": "নথি",
      "footerSource": "GitHub রিপোজিটরি হলো মানক উৎস।",
      "interactiveCalendar": "ইন্টারঅ্যাকটিভ ক্যালেন্ডার",
      "todayInTredecadia": "আজ Tredecadia-তে",
      "selectedDate": "নির্বাচিত তারিখ",
      "gregorian": "গ্রেগরিয়ান",
      "previous": "← আগের",
      "today": "আজ",
      "month": "মাস",
      "teYear": "TE বছর",
      "next": "পরের →",
      "tredecadiaMonth": "Tredecadia মাস",
      "eqName": "বিষুব / নববর্ষ",
      "edName": "পৃথিবী দিবস",
      "noEarthDay": "পৃথিবী দিবস নেই",
      "ordinaryYear": "সাধারণ Tredecadia বছর",
      "outsideWeekdayCycle": "সাপ্তাহিক চক্রের বাইরে",
      "dayOf": "দিন {day} / 28",
      "gregorianToTredecadia": "গ্রেগরিয়ান → Tredecadia",
      "convertCivilDate": "নাগরিক তারিখ রূপান্তর",
      "gregorianDate": "গ্রেগরিয়ান তারিখ",
      "gregorianHelp": "বছর ০ এবং ঋণাত্মক বছরসহ জ্যোতির্বৈজ্ঞানিক বছর গণনা সমর্থিত।",
      "convert": "রূপান্তর",
      "tredecadiaToGregorian": "Tredecadia → গ্রেগরিয়ান",
      "convertTeDate": "মানক TE তারিখ রূপান্তর",
      "tredecadiaDate": "Tredecadia তারিখ",
      "tredecadiaHelp": "12025-07-14, 00000-EQ বা 09998-ED-এর মতো মানক রূপ ব্যবহার করুন।",
      "widgetNote": "উইজেটটি সহায়ক বাস্তবায়ন। স্পেসিফিকেশন ও মেশিন-পাঠযোগ্য রেজিস্ট্রিগুলোই মানক। “আজ” ব্রাউজারের স্থানীয় নাগরিক তারিখ ব্যবহার করে।",
      "invalidGregorian": "অবৈধ গ্রেগরিয়ান তারিখ",
      "invalidTredecadia": "অবৈধ Tredecadia তারিখ",
      "enterIntegerYear": "একটি পূর্ণসংখ্যা Tredecadia বছর লিখুন।",
      "loading": "লোড হচ্ছে…"
    }
  },
  "id": {
    "name": "Bahasa Indonesia",
    "dir": "ltr",
    "readme": "README.id.md",
    "s": {
      "tagline": "Standar kalender abadi 13 × 28.",
      "displayLanguage": "Bahasa tampilan",
      "autoSystem": "Otomatis (sistem)",
      "documentation": "Dokumentasi",
      "footerSource": "Repositori GitHub adalah sumber kanonik.",
      "interactiveCalendar": "Kalender interaktif",
      "todayInTredecadia": "Hari ini di Tredecadia",
      "selectedDate": "Tanggal terpilih",
      "gregorian": "Gregorian",
      "previous": "← Sebelumnya",
      "today": "Hari ini",
      "month": "Bulan",
      "teYear": "Tahun TE",
      "next": "Berikutnya →",
      "tredecadiaMonth": "Bulan Tredecadia",
      "eqName": "Ekuinoks / Tahun Baru",
      "edName": "Hari Bumi",
      "noEarthDay": "Tanpa Hari Bumi",
      "ordinaryYear": "tahun Tredecadia biasa",
      "outsideWeekdayCycle": "Di luar siklus minggu",
      "dayOf": "hari {day} / 28",
      "gregorianToTredecadia": "Gregorian → Tredecadia",
      "convertCivilDate": "Konversi tanggal sipil",
      "gregorianDate": "Tanggal Gregorian",
      "gregorianHelp": "Penomoran tahun astronomis didukung, termasuk tahun 0 dan tahun negatif.",
      "convert": "Konversi",
      "tredecadiaToGregorian": "Tredecadia → Gregorian",
      "convertTeDate": "Konversi tanggal TE kanonik",
      "tredecadiaDate": "Tanggal Tredecadia",
      "tredecadiaHelp": "Gunakan bentuk kanonik seperti 12025-07-14, 00000-EQ, atau 09998-ED.",
      "widgetNote": "Widget ini adalah implementasi bantu. Spesifikasi dan registri yang dapat dibaca mesin tetap normatif. “Hari ini” memakai tanggal sipil lokal browser.",
      "invalidGregorian": "Tanggal Gregorian tidak valid",
      "invalidTredecadia": "Tanggal Tredecadia tidak valid",
      "enterIntegerYear": "Masukkan tahun Tredecadia bilangan bulat.",
      "loading": "Memuat…"
    }
  },
  "vi": {
    "name": "Tiếng Việt",
    "dir": "ltr",
    "readme": "README.vi.md",
    "s": {
      "tagline": "Tiêu chuẩn lịch vĩnh cửu 13 × 28.",
      "displayLanguage": "Ngôn ngữ hiển thị",
      "autoSystem": "Tự động (hệ thống)",
      "documentation": "Tài liệu",
      "footerSource": "Kho GitHub là nguồn chuẩn.",
      "interactiveCalendar": "Lịch tương tác",
      "todayInTredecadia": "Hôm nay trong Tredecadia",
      "selectedDate": "Ngày đã chọn",
      "gregorian": "Gregorian",
      "previous": "← Trước",
      "today": "Hôm nay",
      "month": "Tháng",
      "teYear": "Năm TE",
      "next": "Sau →",
      "tredecadiaMonth": "Tháng Tredecadia",
      "eqName": "Xuân phân / Năm mới",
      "edName": "Ngày Trái Đất",
      "noEarthDay": "Không có Ngày Trái Đất",
      "ordinaryYear": "năm Tredecadia thường",
      "outsideWeekdayCycle": "Ngoài chu kỳ tuần",
      "dayOf": "ngày {day} / 28",
      "gregorianToTredecadia": "Gregorian → Tredecadia",
      "convertCivilDate": "Chuyển đổi ngày dân sự",
      "gregorianDate": "Ngày Gregorian",
      "gregorianHelp": "Hỗ trợ đánh số năm thiên văn, gồm năm 0 và năm âm.",
      "convert": "Chuyển đổi",
      "tredecadiaToGregorian": "Tredecadia → Gregorian",
      "convertTeDate": "Chuyển đổi ngày TE chuẩn",
      "tredecadiaDate": "Ngày Tredecadia",
      "tredecadiaHelp": "Dùng dạng chuẩn như 12025-07-14, 00000-EQ hoặc 09998-ED.",
      "widgetNote": "Tiện ích là một triển khai hỗ trợ. Đặc tả và sổ đăng ký máy đọc được vẫn là chuẩn. “Hôm nay” dùng ngày dân sự cục bộ của trình duyệt.",
      "invalidGregorian": "Ngày Gregorian không hợp lệ",
      "invalidTredecadia": "Ngày Tredecadia không hợp lệ",
      "enterIntegerYear": "Nhập một năm Tredecadia nguyên.",
      "loading": "Đang tải…"
    }
  }
});
  const MONTH_PROFILES = Object.freeze({
  "ru": [
    {
      "month": 1,
      "full": "Масанумика",
      "short6": "Масану",
      "short4": "Маса"
    },
    {
      "month": 2,
      "full": "Тасузунуму",
      "short6": "Тасузу",
      "short4": "Тасу"
    },
    {
      "month": 3,
      "full": "Назумасану",
      "short6": "Назума",
      "short4": "Назу"
    },
    {
      "month": 4,
      "full": "Микасумани",
      "short6": "Микасу",
      "short4": "Мика"
    },
    {
      "month": 5,
      "full": "Янимузуну",
      "short6": "Яниму",
      "short4": "Яни"
    },
    {
      "month": 6,
      "full": "Зумитанасу",
      "short6": "Зумита",
      "short4": "Зуми"
    },
    {
      "month": 7,
      "full": "Муясануми",
      "short6": "Муяса",
      "short4": "Муя"
    },
    {
      "month": 8,
      "full": "Сунизусака",
      "short6": "Сунизу",
      "short4": "Суни"
    },
    {
      "month": 9,
      "full": "Нуманамута",
      "short6": "Нумана",
      "short4": "Нума"
    },
    {
      "month": 10,
      "full": "Казунусуя",
      "short6": "Казуну",
      "short4": "Казу"
    },
    {
      "month": 11,
      "full": "Яназумаса",
      "short6": "Яназу",
      "short4": "Яна"
    },
    {
      "month": 12,
      "full": "Санумиказу",
      "short6": "Сануми",
      "short4": "Сану"
    },
    {
      "month": 13,
      "full": "Нимутазуна",
      "short6": "Нимута",
      "short4": "Ниму"
    }
  ],
  "ja": [
    {
      "month": 1,
      "full": "マサヌミカ",
      "short6": "マサヌ",
      "short4": "マサ"
    },
    {
      "month": 2,
      "full": "タスズヌム",
      "short6": "タスズ",
      "short4": "タス"
    },
    {
      "month": 3,
      "full": "ナズマサヌ",
      "short6": "ナズマ",
      "short4": "ナズ"
    },
    {
      "month": 4,
      "full": "ミカスマニ",
      "short6": "ミカス",
      "short4": "ミカ"
    },
    {
      "month": 5,
      "full": "ヤニムズヌ",
      "short6": "ヤニム",
      "short4": "ヤニ"
    },
    {
      "month": 6,
      "full": "ズミタナス",
      "short6": "ズミタ",
      "short4": "ズミ"
    },
    {
      "month": 7,
      "full": "ムヤサヌミ",
      "short6": "ムヤサ",
      "short4": "ムヤ"
    },
    {
      "month": 8,
      "full": "スニズサカ",
      "short6": "スニズ",
      "short4": "スニ"
    },
    {
      "month": 9,
      "full": "ヌマナムタ",
      "short6": "ヌマナ",
      "short4": "ヌマ"
    },
    {
      "month": 10,
      "full": "カズヌスヤ",
      "short6": "カズヌ",
      "short4": "カズ"
    },
    {
      "month": 11,
      "full": "ヤナズマサ",
      "short6": "ヤナズ",
      "short4": "ヤナ"
    },
    {
      "month": 12,
      "full": "サヌミカズ",
      "short6": "サヌミ",
      "short4": "サヌ"
    },
    {
      "month": 13,
      "full": "ニムタズナ",
      "short6": "ニムタ",
      "short4": "ニム"
    }
  ],
  "ko": [
    {
      "month": 1,
      "full": "마사누미카",
      "short6": "마사누",
      "short4": "마사"
    },
    {
      "month": 2,
      "full": "타수주누무",
      "short6": "타수주",
      "short4": "타수"
    },
    {
      "month": 3,
      "full": "나주마사누",
      "short6": "나주마",
      "short4": "나주"
    },
    {
      "month": 4,
      "full": "미카수마니",
      "short6": "미카수",
      "short4": "미카"
    },
    {
      "month": 5,
      "full": "야니무주누",
      "short6": "야니무",
      "short4": "야니"
    },
    {
      "month": 6,
      "full": "주미타나수",
      "short6": "주미타",
      "short4": "주미"
    },
    {
      "month": 7,
      "full": "무야사누미",
      "short6": "무야사",
      "short4": "무야"
    },
    {
      "month": 8,
      "full": "수니주사카",
      "short6": "수니주",
      "short4": "수니"
    },
    {
      "month": 9,
      "full": "누마나무타",
      "short6": "누마나",
      "short4": "누마"
    },
    {
      "month": 10,
      "full": "카주누수야",
      "short6": "카주누",
      "short4": "카주"
    },
    {
      "month": 11,
      "full": "야나주마사",
      "short6": "야나주",
      "short4": "야나"
    },
    {
      "month": 12,
      "full": "사누미카주",
      "short6": "사누미",
      "short4": "사누"
    },
    {
      "month": 13,
      "full": "니무타주나",
      "short6": "니무타",
      "short4": "니무"
    }
  ],
  "ka": [
    {
      "month": 1,
      "full": "მასანუმიკა",
      "short6": "მასანუ",
      "short4": "მასა"
    },
    {
      "month": 2,
      "full": "ტასუზუნუმუ",
      "short6": "ტასუზუ",
      "short4": "ტასუ"
    },
    {
      "month": 3,
      "full": "ნაზუმასანუ",
      "short6": "ნაზუმა",
      "short4": "ნაზუ"
    },
    {
      "month": 4,
      "full": "მიკასუმანი",
      "short6": "მიკასუ",
      "short4": "მიკა"
    },
    {
      "month": 5,
      "full": "იანიმუზუნუ",
      "short6": "იანიმუ",
      "short4": "იანი"
    },
    {
      "month": 6,
      "full": "ზუმიტანასუ",
      "short6": "ზუმიტა",
      "short4": "ზუმი"
    },
    {
      "month": 7,
      "full": "მუიასანუმი",
      "short6": "მუიასა",
      "short4": "მუია"
    },
    {
      "month": 8,
      "full": "სუნიზუსაკა",
      "short6": "სუნიზუ",
      "short4": "სუნი"
    },
    {
      "month": 9,
      "full": "ნუმანამუტა",
      "short6": "ნუმანა",
      "short4": "ნუმა"
    },
    {
      "month": 10,
      "full": "კაზუნუსუია",
      "short6": "კაზუნუ",
      "short4": "კაზუ"
    },
    {
      "month": 11,
      "full": "იანაზუმასა",
      "short6": "იანაზუ",
      "short4": "იანა"
    },
    {
      "month": 12,
      "full": "სანუმიკაზუ",
      "short6": "სანუმი",
      "short4": "სანუ"
    },
    {
      "month": 13,
      "full": "ნიმუტაზუნა",
      "short6": "ნიმუტა",
      "short4": "ნიმუ"
    }
  ],
  "hy": [
    {
      "month": 1,
      "full": "մասանումիկա",
      "short6": "մասանու",
      "short4": "մասա"
    },
    {
      "month": 2,
      "full": "տասուզունումու",
      "short6": "տասուզու",
      "short4": "տասու"
    },
    {
      "month": 3,
      "full": "նազումասանու",
      "short6": "նազումա",
      "short4": "նազու"
    },
    {
      "month": 4,
      "full": "միկասումանի",
      "short6": "միկասու",
      "short4": "միկա"
    },
    {
      "month": 5,
      "full": "յանիմուզունու",
      "short6": "յանիմու",
      "short4": "յանի"
    },
    {
      "month": 6,
      "full": "զումիտանասու",
      "short6": "զումիտա",
      "short4": "զումի"
    },
    {
      "month": 7,
      "full": "մույասանումի",
      "short6": "մույասա",
      "short4": "մույա"
    },
    {
      "month": 8,
      "full": "սունիզուսակա",
      "short6": "սունիզու",
      "short4": "սունի"
    },
    {
      "month": 9,
      "full": "նումանամուտա",
      "short6": "նումանա",
      "short4": "նումա"
    },
    {
      "month": 10,
      "full": "կազունուսույա",
      "short6": "կազունու",
      "short4": "կազու"
    },
    {
      "month": 11,
      "full": "յանազումասա",
      "short6": "յանազու",
      "short4": "յանա"
    },
    {
      "month": 12,
      "full": "սանումիկազու",
      "short6": "սանումի",
      "short4": "սանու"
    },
    {
      "month": 13,
      "full": "նիմուտազունա",
      "short6": "նիմուտա",
      "short4": "նիմու"
    }
  ],
  "ar": [
    {
      "month": 1,
      "full": "مَسَنُمِكَ",
      "short6": "مَسَنُ",
      "short4": "مَسَ"
    },
    {
      "month": 2,
      "full": "تَسُزُنُمُ",
      "short6": "تَسُزُ",
      "short4": "تَسُ"
    },
    {
      "month": 3,
      "full": "نَزُمَسَنُ",
      "short6": "نَزُمَ",
      "short4": "نَزُ"
    },
    {
      "month": 4,
      "full": "مِكَسُمَنِ",
      "short6": "مِكَسُ",
      "short4": "مِكَ"
    },
    {
      "month": 5,
      "full": "يَنِمُزُنُ",
      "short6": "يَنِمُ",
      "short4": "يَنِ"
    },
    {
      "month": 6,
      "full": "زُمِتَنَسُ",
      "short6": "زُمِتَ",
      "short4": "زُمِ"
    },
    {
      "month": 7,
      "full": "مُيَسَنُمِ",
      "short6": "مُيَسَ",
      "short4": "مُيَ"
    },
    {
      "month": 8,
      "full": "سُنِزُسَكَ",
      "short6": "سُنِزُ",
      "short4": "سُنِ"
    },
    {
      "month": 9,
      "full": "نُمَنَمُتَ",
      "short6": "نُمَنَ",
      "short4": "نُمَ"
    },
    {
      "month": 10,
      "full": "كَزُنُسُيَ",
      "short6": "كَزُنُ",
      "short4": "كَزُ"
    },
    {
      "month": 11,
      "full": "يَنَزُمَسَ",
      "short6": "يَنَزُ",
      "short4": "يَنَ"
    },
    {
      "month": 12,
      "full": "سَنُمِكَزُ",
      "short6": "سَنُمِ",
      "short4": "سَنُ"
    },
    {
      "month": 13,
      "full": "نِمُتَزُنَ",
      "short6": "نِمُتَ",
      "short4": "نِمُ"
    }
  ],
  "hi": [
    {
      "month": 1,
      "full": "मासानुमिका",
      "short6": "मासानु",
      "short4": "मासा"
    },
    {
      "month": 2,
      "full": "तासुज़ुनुमु",
      "short6": "तासुज़ु",
      "short4": "तासु"
    },
    {
      "month": 3,
      "full": "नाज़ुमासानु",
      "short6": "नाज़ुमा",
      "short4": "नाज़ु"
    },
    {
      "month": 4,
      "full": "मिकासुमानि",
      "short6": "मिकासु",
      "short4": "मिका"
    },
    {
      "month": 5,
      "full": "यानिमुज़ुनु",
      "short6": "यानिमु",
      "short4": "यानि"
    },
    {
      "month": 6,
      "full": "ज़ुमितानासु",
      "short6": "ज़ुमिता",
      "short4": "ज़ुमि"
    },
    {
      "month": 7,
      "full": "मुयासानुमि",
      "short6": "मुयासा",
      "short4": "मुया"
    },
    {
      "month": 8,
      "full": "सुनिज़ुसाका",
      "short6": "सुनिज़ु",
      "short4": "सुनि"
    },
    {
      "month": 9,
      "full": "नुमानामुता",
      "short6": "नुमाना",
      "short4": "नुमा"
    },
    {
      "month": 10,
      "full": "काज़ुनुसुया",
      "short6": "काज़ुनु",
      "short4": "काज़ु"
    },
    {
      "month": 11,
      "full": "यानाज़ुमासा",
      "short6": "यानाज़ु",
      "short4": "याना"
    },
    {
      "month": 12,
      "full": "सानुमिकाज़ु",
      "short6": "सानुमि",
      "short4": "सानु"
    },
    {
      "month": 13,
      "full": "निमुताज़ुना",
      "short6": "निमुता",
      "short4": "निमु"
    }
  ],
  "bn": [
    {
      "month": 1,
      "full": "মাসানুমিকা",
      "short6": "মাসানু",
      "short4": "মাসা"
    },
    {
      "month": 2,
      "full": "তাসুজুনুমু",
      "short6": "তাসুজু",
      "short4": "তাসু"
    },
    {
      "month": 3,
      "full": "নাজুমাসানু",
      "short6": "নাজুমা",
      "short4": "নাজু"
    },
    {
      "month": 4,
      "full": "মিকাসুমানি",
      "short6": "মিকাসু",
      "short4": "মিকা"
    },
    {
      "month": 5,
      "full": "ইয়ানিমুজুনু",
      "short6": "ইয়ানিমু",
      "short4": "ইয়ানি"
    },
    {
      "month": 6,
      "full": "জুমিতানাসু",
      "short6": "জুমিতা",
      "short4": "জুমি"
    },
    {
      "month": 7,
      "full": "মুইয়াসানুমি",
      "short6": "মুইয়াসা",
      "short4": "মুইয়া"
    },
    {
      "month": 8,
      "full": "সুনিজুসাকা",
      "short6": "সুনিজু",
      "short4": "সুনি"
    },
    {
      "month": 9,
      "full": "নুমানামুতা",
      "short6": "নুমানা",
      "short4": "নুমা"
    },
    {
      "month": 10,
      "full": "কাজুনুসুইয়া",
      "short6": "কাজুনু",
      "short4": "কাজু"
    },
    {
      "month": 11,
      "full": "ইয়ানাজুমাসা",
      "short6": "ইয়ানাজু",
      "short4": "ইয়ানা"
    },
    {
      "month": 12,
      "full": "সানুমিকাজু",
      "short6": "সানুমি",
      "short4": "সানু"
    },
    {
      "month": 13,
      "full": "নিমুতাজুনা",
      "short6": "নিমুতা",
      "short4": "নিমু"
    }
  ],
  "fa": [
    {
      "month": 1,
      "full": "مَسَنومیکَ",
      "short6": "مَسَنو",
      "short4": "مَسَ"
    },
    {
      "month": 2,
      "full": "تَسوزونومو",
      "short6": "تَسوزو",
      "short4": "تَسو"
    },
    {
      "month": 3,
      "full": "نَزومَسَنو",
      "short6": "نَزومَ",
      "short4": "نَزو"
    },
    {
      "month": 4,
      "full": "میکَسومَنی",
      "short6": "میکَسو",
      "short4": "میکَ"
    },
    {
      "month": 5,
      "full": "یَنیموزونو",
      "short6": "یَنیمو",
      "short4": "یَنی"
    },
    {
      "month": 6,
      "full": "زومیتَنَسو",
      "short6": "زومیتَ",
      "short4": "زومی"
    },
    {
      "month": 7,
      "full": "مویَسَنومی",
      "short6": "مویَسَ",
      "short4": "مویَ"
    },
    {
      "month": 8,
      "full": "سونیزوسَکَ",
      "short6": "سونیزو",
      "short4": "سونی"
    },
    {
      "month": 9,
      "full": "نومَنَموتَ",
      "short6": "نومَنَ",
      "short4": "نومَ"
    },
    {
      "month": 10,
      "full": "کَزونوسویَ",
      "short6": "کَزونو",
      "short4": "کَزو"
    },
    {
      "month": 11,
      "full": "یَنَزومَسَ",
      "short6": "یَنَزو",
      "short4": "یَنَ"
    },
    {
      "month": 12,
      "full": "سَنومیکَزو",
      "short6": "سَنومی",
      "short4": "سَنو"
    },
    {
      "month": 13,
      "full": "نیموتَزونَ",
      "short6": "نیموتَ",
      "short4": "نیمو"
    }
  ]
});

  function normalizeTag(tag) {
    return String(tag || "").trim().replace(/_/g, "-").toLowerCase();
  }

  function resolveLanguage(tag) {
    const normalized = normalizeTag(tag);
    if (!normalized) return null;

    if (normalized === "zh-hant" || normalized.startsWith("zh-tw") || normalized.startsWith("zh-hk") || normalized.startsWith("zh-mo")) return "zh-TW";
    if (normalized === "zh-hans" || normalized.startsWith("zh-cn") || normalized.startsWith("zh-sg") || normalized === "zh") return "zh-CN";
    if (normalized.startsWith("pt")) return "pt-BR";

    const primary = normalized.split("-")[0];
    const exact = Object.keys(LOCALES).find((key) => key.toLowerCase() === normalized);
    if (exact) return exact;
    const primaryMatch = Object.keys(LOCALES).find((key) => key.toLowerCase() === primary);
    return primaryMatch || null;
  }

  function detectLanguage(languageList) {
    const candidates = Array.isArray(languageList) ? languageList : [];
    for (const candidate of candidates) {
      const resolved = resolveLanguage(candidate);
      if (resolved) return resolved;
    }
    return "en";
  }

  function string(locale, key) {
    const current = LOCALES[locale] || LOCALES.en;
    return current.s[key] || LOCALES.en.s[key] || key;
  }

  function monthAlias(locale, monthNumber) {
    const profile = MONTH_PROFILES[locale];
    if (!profile) return null;
    return profile.find((item) => item.month === monthNumber) || null;
  }

  function readmePath(locale) {
    return (LOCALES[locale] || LOCALES.en).readme;
  }

  return Object.freeze({
    STORAGE_KEY,
    LOCALES,
    MONTH_PROFILES,
    resolveLanguage,
    detectLanguage,
    string,
    monthAlias,
    readmePath,
  });
});
