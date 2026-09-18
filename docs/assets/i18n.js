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
      "loading": "Loading…",
      "aboutTitle": "About Tredecadia",
      "aboutSummary": "This page is a navigational summary, not a second copy of the standard. Normative requirements remain in the repository specifications and machine-readable registries.",
      "factStructure": "13 equal months × 28 days = 364 regular days; every month contains four complete seven-day weeks.",
      "factIntercalary": "EQ — Equinox / New Year Day — opens each year outside the month/week cycle; leap years also contain ED — Earth Day.",
      "factEra": "Tredecadia Era (TE) is a single integer year axis with a real year 0.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo and Toze are canonical language-neutral weekday identities.",
      "resourcesTitle": "Standard and resources",
      "resourcesSummary": "Open the full project documentation in the selected language, or inspect the published releases.",
      "allLanguages": "All languages",
      "stableRelease": "Stable v1.0.0",
      "prerelease": "v1.1.0-rc.1 prerelease"
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
      "loading": "Загрузка…",
      "aboutTitle": "О Tredecadia",
      "aboutSummary": "Эта страница — краткая навигационная сводка, а не вторая копия стандарта. Нормативные требования находятся в спецификациях репозитория и машиночитаемых реестрах.",
      "factStructure": "13 равных месяцев × 28 дней = 364 обычных дня; каждый месяц содержит четыре полные семидневные недели.",
      "factIntercalary": "EQ — День равноденствия / Новый год — открывает каждый год вне месяца и недели; в високосном году также есть ED — День Земли.",
      "factEra": "Эра Tredecadia (TE) — единая целочисленная шкала лет с настоящим нулевым годом.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo и Toze — канонические нейтральные названия дней недели.",
      "resourcesTitle": "Стандарт и материалы",
      "resourcesSummary": "Откройте полную документацию проекта на выбранном языке или опубликованные релизы.",
      "allLanguages": "Все языки",
      "stableRelease": "Стабильная v1.0.0",
      "prerelease": "Предрелиз v1.1.0-rc.1"
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
      "loading": "Cargando…",
      "aboutTitle": "Acerca de Tredecadia",
      "aboutSummary": "Esta página es un resumen de navegación, no una segunda copia del estándar. Los requisitos normativos permanecen en las especificaciones y registros legibles por máquina del repositorio.",
      "factStructure": "13 meses iguales × 28 días = 364 días regulares; cada mes contiene cuatro semanas completas de siete días.",
      "factIntercalary": "EQ — Equinoccio / Año Nuevo — abre cada año fuera del ciclo de mes y semana; los años bisiestos también incluyen ED — Día de la Tierra.",
      "factEra": "La Era Tredecadia (TE) es un único eje entero de años con un año 0 real.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo y Toze son identidades canónicas y neutrales de los días de la semana.",
      "resourcesTitle": "Estándar y recursos",
      "resourcesSummary": "Abra la documentación completa del proyecto en el idioma seleccionado o consulte las versiones publicadas.",
      "allLanguages": "Todos los idiomas",
      "stableRelease": "Estable v1.0.0",
      "prerelease": "Prelanzamiento v1.1.0-rc.1"
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
      "loading": "Carregando…",
      "aboutTitle": "Sobre o Tredecadia",
      "aboutSummary": "Esta página é um resumo de navegação, não uma segunda cópia do padrão. Os requisitos normativos permanecem nas especificações e registros legíveis por máquina do repositório.",
      "factStructure": "13 meses iguais × 28 dias = 364 dias regulares; cada mês contém quatro semanas completas de sete dias.",
      "factIntercalary": "EQ — Equinócio / Ano-Novo — abre cada ano fora do ciclo de mês e semana; anos bissextos também incluem ED — Dia da Terra.",
      "factEra": "A Era Tredecadia (TE) é um único eixo inteiro de anos com um ano 0 real.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo e Toze são identidades canônicas e neutras dos dias da semana.",
      "resourcesTitle": "Padrão e recursos",
      "resourcesSummary": "Abra a documentação completa do projeto no idioma selecionado ou consulte as versões publicadas.",
      "allLanguages": "Todos os idiomas",
      "stableRelease": "Estável v1.0.0",
      "prerelease": "Pré-lançamento v1.1.0-rc.1"
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
      "loading": "Chargement…",
      "aboutTitle": "À propos de Tredecadia",
      "aboutSummary": "Cette page est un résumé de navigation, et non une seconde copie de la norme. Les exigences normatives restent dans les spécifications et registres lisibles par machine du dépôt.",
      "factStructure": "13 mois égaux × 28 jours = 364 jours ordinaires ; chaque mois contient quatre semaines complètes de sept jours.",
      "factIntercalary": "EQ — Équinoxe / Nouvel An — ouvre chaque année hors du cycle mois/semaine ; les années bissextiles contiennent aussi ED — Jour de la Terre.",
      "factEra": "L’ère Tredecadia (TE) est un axe entier unique des années avec une véritable année 0.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo et Toze sont les identités canoniques et neutres des jours de la semaine.",
      "resourcesTitle": "Norme et ressources",
      "resourcesSummary": "Ouvrez la documentation complète du projet dans la langue sélectionnée ou consultez les versions publiées.",
      "allLanguages": "Toutes les langues",
      "stableRelease": "Stable v1.0.0",
      "prerelease": "Préversion v1.1.0-rc.1"
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
      "loading": "Wird geladen…",
      "aboutTitle": "Über Tredecadia",
      "aboutSummary": "Diese Seite ist eine Navigationsübersicht und keine zweite Kopie des Standards. Normative Anforderungen bleiben in den Spezifikationen und maschinenlesbaren Registern des Repositorys.",
      "factStructure": "13 gleiche Monate × 28 Tage = 364 reguläre Tage; jeder Monat enthält vier vollständige Sieben-Tage-Wochen.",
      "factIntercalary": "EQ — Tagundnachtgleiche / Neujahr — eröffnet jedes Jahr außerhalb des Monats-/Wochenzyklus; Schaltjahre enthalten zusätzlich ED — Tag der Erde.",
      "factEra": "Die Tredecadia-Ära (TE) ist eine einzige ganzzahlige Jahresachse mit einem echten Jahr 0.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo und Toze sind kanonische, sprachneutrale Wochentagsidentitäten.",
      "resourcesTitle": "Standard und Ressourcen",
      "resourcesSummary": "Öffnen Sie die vollständige Projektdokumentation in der gewählten Sprache oder die veröffentlichten Versionen.",
      "allLanguages": "Alle Sprachen",
      "stableRelease": "Stabil v1.0.0",
      "prerelease": "Vorabversion v1.1.0-rc.1"
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
      "loading": "Caricamento…",
      "aboutTitle": "Informazioni su Tredecadia",
      "aboutSummary": "Questa pagina è un riepilogo di navigazione, non una seconda copia dello standard. I requisiti normativi rimangono nelle specifiche e nei registri leggibili dalla macchina del repository.",
      "factStructure": "13 mesi uguali × 28 giorni = 364 giorni regolari; ogni mese contiene quattro settimane complete di sette giorni.",
      "factIntercalary": "EQ — Equinozio / Capodanno — apre ogni anno fuori dal ciclo mese/settimana; gli anni bisestili includono anche ED — Giornata della Terra.",
      "factEra": "L’Era Tredecadia (TE) è un unico asse intero degli anni con un vero anno 0.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo e Toze sono identità canoniche e linguisticamente neutrali dei giorni della settimana.",
      "resourcesTitle": "Standard e risorse",
      "resourcesSummary": "Apri la documentazione completa del progetto nella lingua selezionata oppure consulta le versioni pubblicate.",
      "allLanguages": "Tutte le lingue",
      "stableRelease": "Stabile v1.0.0",
      "prerelease": "Pre-release v1.1.0-rc.1"
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
      "loading": "Yükleniyor…",
      "aboutTitle": "Tredecadia hakkında",
      "aboutSummary": "Bu sayfa standardın ikinci bir kopyası değil, gezinme amaçlı bir özettir. Normatif gereksinimler depo spesifikasyonlarında ve makinece okunabilir kayıtlarda kalır.",
      "factStructure": "13 eşit ay × 28 gün = 364 normal gün; her ay dört tam yedi günlük haftadan oluşur.",
      "factIntercalary": "EQ — Ekinoks / Yeni Yıl — her yılı ay/hafta döngüsünün dışında açar; artık yıllarda ayrıca ED — Dünya Günü bulunur.",
      "factEra": "Tredecadia Era (TE), gerçek bir 0 yılı olan tek bir tam sayı yıl eksenidir.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo ve Toze kanonik ve dilden bağımsız hafta günü kimlikleridir.",
      "resourcesTitle": "Standart ve kaynaklar",
      "resourcesSummary": "Tam proje belgelerini seçilen dilde açın veya yayımlanmış sürümleri inceleyin.",
      "allLanguages": "Tüm diller",
      "stableRelease": "Kararlı v1.0.0",
      "prerelease": "Ön sürüm v1.1.0-rc.1"
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
      "loading": "Ładowanie…",
      "aboutTitle": "O Tredecadii",
      "aboutSummary": "Ta strona jest skrótem nawigacyjnym, a nie drugą kopią standardu. Wymagania normatywne pozostają w specyfikacjach repozytorium i rejestrach maszynowych.",
      "factStructure": "13 równych miesięcy × 28 dni = 364 zwykłe dni; każdy miesiąc zawiera cztery pełne siedmiodniowe tygodnie.",
      "factIntercalary": "EQ — Równonoc / Nowy Rok — otwiera każdy rok poza cyklem miesiąca i tygodnia; lata przestępne zawierają także ED — Dzień Ziemi.",
      "factEra": "Era Tredecadii (TE) to jedna całkowitoliczbowa oś lat z rzeczywistym rokiem 0.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo i Toze są kanonicznymi, neutralnymi językowo nazwami dni tygodnia.",
      "resourcesTitle": "Standard i materiały",
      "resourcesSummary": "Otwórz pełną dokumentację projektu w wybranym języku lub opublikowane wydania.",
      "allLanguages": "Wszystkie języki",
      "stableRelease": "Stabilna v1.0.0",
      "prerelease": "Wersja wstępna v1.1.0-rc.1"
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
      "loading": "Завантаження…",
      "aboutTitle": "Про Tredecadia",
      "aboutSummary": "Ця сторінка — навігаційний огляд, а не друга копія стандарту. Нормативні вимоги залишаються у специфікаціях репозиторію та машинозчитуваних реєстрах.",
      "factStructure": "13 рівних місяців × 28 днів = 364 звичайні дні; кожен місяць містить чотири повні семиденні тижні.",
      "factIntercalary": "EQ — Рівнодення / Новий рік — відкриває кожен рік поза циклом місяця і тижня; у високосному році також є ED — День Землі.",
      "factEra": "Ера Tredecadia (TE) — єдина цілочисельна шкала років зі справжнім нульовим роком.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo і Toze — канонічні нейтральні назви днів тижня.",
      "resourcesTitle": "Стандарт і матеріали",
      "resourcesSummary": "Відкрийте повну документацію проєкту вибраною мовою або опубліковані релізи.",
      "allLanguages": "Усі мови",
      "stableRelease": "Стабільна v1.0.0",
      "prerelease": "Передреліз v1.1.0-rc.1"
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
      "loading": "იტვირთება…",
      "aboutTitle": "Tredecadia-ს შესახებ",
      "aboutSummary": "ეს გვერდი არის სანავიგაციო შეჯამება და არა სტანდარტის მეორე ასლი. ნორმატიული მოთხოვნები რჩება რეპოზიტორიის სპეციფიკაციებსა და მანქანურად წაკითხვად რეესტრებში.",
      "factStructure": "13 თანაბარი თვე × 28 დღე = 364 ჩვეულებრივი დღე; თითოეული თვე შეიცავს ოთხ სრულ შვიდდღიან კვირას.",
      "factIntercalary": "EQ — ბუნიობა / ახალი წელი — ყოველ წელს ხსნის თვე/კვირის ციკლის გარეთ; ნაკიან წლებში ასევე არის ED — დედამიწის დღე.",
      "factEra": "Tredecadia Era (TE) არის წლების ერთი მთელი რიცხვითი ღერძი რეალური 0 წლით.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo და Toze არის კვირის დღეების კანონიკური, ენობრივად ნეიტრალური იდენტობები.",
      "resourcesTitle": "სტანდარტი და რესურსები",
      "resourcesSummary": "გახსენით პროექტის სრული დოკუმენტაცია არჩეულ ენაზე ან გამოქვეყნებული რელიზები.",
      "allLanguages": "ყველა ენა",
      "stableRelease": "სტაბილური v1.0.0",
      "prerelease": "წინასწარი რელიზი v1.1.0-rc.1"
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
      "loading": "Բեռնվում է…",
      "aboutTitle": "Tredecadia-ի մասին",
      "aboutSummary": "Այս էջը նավիգացիոն ամփոփում է, ոչ թե ստանդարտի երկրորդ պատճենը։ Նորմատիվ պահանջները մնում են պահոցի բնութագրերում և մեքենայական ընթեռնելի ռեգիստրներում։",
      "factStructure": "13 հավասար ամիս × 28 օր = 364 սովորական օր. յուրաքանչյուր ամիս ունի չորս ամբողջական յոթօրյա շաբաթ։",
      "factIntercalary": "EQ — Գիշերահավասար / Նոր տարի — բացում է յուրաքանչյուր տարին ամսվա/շաբաթվա ցիկլից դուրս, իսկ նահանջ տարիներում կա նաև ED — Երկրի օր։",
      "factEra": "Tredecadia Era (TE)-ն տարիների մեկ ամբողջ թվային առանցք է՝ իրական 0 տարով։",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo և Toze-ը շաբաթվա օրերի կանոնական, լեզվապես չեզոք նույնականացուցիչներ են։",
      "resourcesTitle": "Ստանդարտ և նյութեր",
      "resourcesSummary": "Բացեք նախագծի ամբողջական փաստաթղթերը ընտրված լեզվով կամ հրապարակված թողարկումները։",
      "allLanguages": "Բոլոր լեզուները",
      "stableRelease": "Կայուն v1.0.0",
      "prerelease": "Նախաթողարկում v1.1.0-rc.1"
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
      "loading": "加载中…",
      "aboutTitle": "关于 Tredecadia",
      "aboutSummary": "本页是导航摘要，而不是标准的第二份副本。规范性要求仍以仓库中的规范文档和机器可读注册表为准。",
      "factStructure": "13 个等长月份 × 28 天 = 364 个常规日；每个月恰好包含四个完整的七日周。",
      "factIntercalary": "EQ — 春分 / 新年日 — 在月/周循环之外开启每一年；闰年还包含 ED — 地球日。",
      "factEra": "Tredecadia 纪元（TE）是一条整数年份轴，并具有真实的 0 年。",
      "factWeekdays": "Mene、Noko、Kese、Zoyo、Sote、Yemo 和 Toze 是规范的、与语言无关的星期日名称。",
      "resourcesTitle": "标准与资源",
      "resourcesSummary": "打开所选语言的完整项目文档，或查看已发布版本。",
      "allLanguages": "所有语言",
      "stableRelease": "稳定版 v1.0.0",
      "prerelease": "预发布版 v1.1.0-rc.1"
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
      "loading": "載入中…",
      "aboutTitle": "關於 Tredecadia",
      "aboutSummary": "本頁是導覽摘要，而不是標準的第二份副本。規範性要求仍以儲存庫中的規範文件與機器可讀登錄為準。",
      "factStructure": "13 個等長月份 × 28 天 = 364 個常規日；每個月恰好包含四個完整的七日週。",
      "factIntercalary": "EQ — 春分 / 新年日 — 在月/週循環之外開啟每一年；閏年還包含 ED — 地球日。",
      "factEra": "Tredecadia 紀元（TE）是一條整數年份軸，並具有真正的 0 年。",
      "factWeekdays": "Mene、Noko、Kese、Zoyo、Sote、Yemo 和 Toze 是規範且與語言無關的星期日名稱。",
      "resourcesTitle": "標準與資源",
      "resourcesSummary": "開啟所選語言的完整專案文件，或查看已發布版本。",
      "allLanguages": "所有語言",
      "stableRelease": "穩定版 v1.0.0",
      "prerelease": "預發布版 v1.1.0-rc.1"
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
      "loading": "読み込み中…",
      "aboutTitle": "Tredecadia について",
      "aboutSummary": "このページはナビゲーション用の概要であり、標準の第二のコピーではありません。規範要件はリポジトリの仕様書と機械可読レジストリにあります。",
      "factStructure": "13 個の同じ長さの月 × 28 日 = 364 通常日。各月は完全な 7 日週を 4 週含みます。",
      "factIntercalary": "EQ — 春分 / 元日 — は月・曜日サイクルの外で各年を開始し、閏年には ED — アースデイもあります。",
      "factEra": "Tredecadia Era（TE）は実在する 0 年を持つ単一の整数年軸です。",
      "factWeekdays": "Mene、Noko、Kese、Zoyo、Sote、Yemo、Toze は言語に依存しない正規の曜日識別子です。",
      "resourcesTitle": "標準とリソース",
      "resourcesSummary": "選択した言語で完全なプロジェクト文書を開くか、公開済みリリースを確認してください。",
      "allLanguages": "すべての言語",
      "stableRelease": "安定版 v1.0.0",
      "prerelease": "プレリリース v1.1.0-rc.1"
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
      "loading": "불러오는 중…",
      "aboutTitle": "Tredecadia 소개",
      "aboutSummary": "이 페이지는 탐색용 요약이며 표준의 두 번째 사본이 아닙니다. 규범 요구사항은 저장소의 사양 문서와 기계 판독 가능 레지스트리에 있습니다.",
      "factStructure": "13개의 동일한 달 × 28일 = 364개의 일반일이며, 각 달은 완전한 7일 주 4개로 구성됩니다.",
      "factIntercalary": "EQ — 춘분 / 새해 첫날 — 은 월/주기 밖에서 매년을 시작하고, 윤년에는 ED — 지구의 날도 포함됩니다.",
      "factEra": "Tredecadia Era(TE)는 실제 0년을 갖는 하나의 정수 연도 축입니다.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo, Toze는 언어에 독립적인 정규 요일 식별자입니다.",
      "resourcesTitle": "표준 및 자료",
      "resourcesSummary": "선택한 언어로 전체 프로젝트 문서를 열거나 게시된 릴리스를 확인하세요.",
      "allLanguages": "모든 언어",
      "stableRelease": "안정판 v1.0.0",
      "prerelease": "프리릴리스 v1.1.0-rc.1"
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
      "loading": "جارٍ التحميل…",
      "aboutTitle": "حول Tredecadia",
      "aboutSummary": "هذه الصفحة ملخص للتنقل وليست نسخة ثانية من المعيار. تبقى المتطلبات المعيارية في مواصفات المستودع والسجلات المقروءة آليًا.",
      "factStructure": "13 شهرًا متساويًا × 28 يومًا = 364 يومًا عاديًا؛ وكل شهر يحتوي أربع أسابيع كاملة من سبعة أيام.",
      "factIntercalary": "EQ — الاعتدال / رأس السنة — يفتح كل سنة خارج دورة الشهر/الأسبوع؛ وتحتوي السنوات الكبيسة أيضًا على ED — يوم الأرض.",
      "factEra": "حقبة Tredecadia ‏(TE) محور واحد صحيح للسنوات ويتضمن سنة 0 حقيقية.",
      "factWeekdays": "Mene وNoko وKese وZoyo وSote وYemo وToze هي هويات معيارية ومحايدة لغويًا لأيام الأسبوع.",
      "resourcesTitle": "المعيار والموارد",
      "resourcesSummary": "افتح وثائق المشروع الكاملة باللغة المختارة أو راجع الإصدارات المنشورة.",
      "allLanguages": "كل اللغات",
      "stableRelease": "الإصدار المستقر v1.0.0",
      "prerelease": "الإصدار التمهيدي v1.1.0-rc.1"
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
      "loading": "در حال بارگذاری…",
      "aboutTitle": "دربارهٔ Tredecadia",
      "aboutSummary": "این صفحه خلاصه‌ای برای راهبری است و نسخهٔ دوم استاندارد نیست. الزامات معیار در مشخصات مخزن و رجیسترهای ماشین‌خوان باقی می‌مانند.",
      "factStructure": "۱۳ ماه برابر × ۲۸ روز = ۳۶۴ روز عادی؛ هر ماه چهار هفتهٔ کامل هفت‌روزه دارد.",
      "factIntercalary": "EQ — اعتدال / سال نو — هر سال را خارج از چرخهٔ ماه/هفته آغاز می‌کند؛ سال‌های کبیسه همچنین ED — روز زمین را دارند.",
      "factEra": "دورهٔ Tredecadia ‏(TE) یک محور صحیح واحد برای سال‌ها با سال واقعی ۰ است.",
      "factWeekdays": "Mene، Noko، Kese، Zoyo، Sote، Yemo و Toze شناسه‌های معیار و بی‌طرف زبانی روزهای هفته هستند.",
      "resourcesTitle": "استاندارد و منابع",
      "resourcesSummary": "مستندات کامل پروژه را به زبان انتخاب‌شده باز کنید یا نسخه‌های منتشرشده را ببینید.",
      "allLanguages": "همهٔ زبان‌ها",
      "stableRelease": "نسخهٔ پایدار v1.0.0",
      "prerelease": "پیش‌انتشار v1.1.0-rc.1"
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
      "loading": "लोड हो रहा है…",
      "aboutTitle": "Tredecadia के बारे में",
      "aboutSummary": "यह पृष्ठ नेविगेशन सारांश है, मानक की दूसरी प्रति नहीं। मानक आवश्यकताएँ रिपॉज़िटरी की विशिष्टताओं और मशीन-पठनीय रजिस्टरों में रहती हैं।",
      "factStructure": "13 समान माह × 28 दिन = 364 सामान्य दिन; हर माह में सात दिनों के चार पूरे सप्ताह होते हैं।",
      "factIntercalary": "EQ — विषुव / नववर्ष दिवस — हर वर्ष को माह/सप्ताह चक्र के बाहर खोलता है; लीप वर्ष में ED — पृथ्वी दिवस भी होता है।",
      "factEra": "Tredecadia Era (TE) वास्तविक वर्ष 0 वाला एक पूर्णांक वर्ष-अक्ष है।",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo और Toze सप्ताह के दिनों की मानक, भाषा-तटस्थ पहचान हैं।",
      "resourcesTitle": "मानक और संसाधन",
      "resourcesSummary": "चुनी गई भाषा में पूर्ण परियोजना दस्तावेज़ खोलें या प्रकाशित रिलीज़ देखें।",
      "allLanguages": "सभी भाषाएँ",
      "stableRelease": "स्थिर v1.0.0",
      "prerelease": "प्रीरिलीज़ v1.1.0-rc.1"
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
      "loading": "লোড হচ্ছে…",
      "aboutTitle": "Tredecadia সম্পর্কে",
      "aboutSummary": "এই পৃষ্ঠাটি নেভিগেশনের সারাংশ, মানটির দ্বিতীয় অনুলিপি নয়। মানক প্রয়োজনীয়তা রিপোজিটরির স্পেসিফিকেশন ও মেশিন-পাঠযোগ্য রেজিস্ট্রিতে থাকে।",
      "factStructure": "১৩টি সমান মাস × ২৮ দিন = ৩৬৪টি সাধারণ দিন; প্রতিটি মাসে চারটি পূর্ণ সাত দিনের সপ্তাহ থাকে।",
      "factIntercalary": "EQ — বিষুব / নববর্ষ — মাস/সপ্তাহ চক্রের বাইরে প্রতি বছর শুরু করে; অধিবর্ষে ED — পৃথিবী দিবসও থাকে।",
      "factEra": "Tredecadia Era (TE) হলো বাস্তব ০ বছরসহ একটি একক পূর্ণসংখ্যা বছর অক্ষ।",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo ও Toze সপ্তাহের দিনের মানক, ভাষা-নিরপেক্ষ পরিচয়।",
      "resourcesTitle": "মান ও সম্পদ",
      "resourcesSummary": "নির্বাচিত ভাষায় সম্পূর্ণ প্রকল্প নথি খুলুন অথবা প্রকাশিত রিলিজ দেখুন।",
      "allLanguages": "সব ভাষা",
      "stableRelease": "স্থিতিশীল v1.0.0",
      "prerelease": "প্রিরিলিজ v1.1.0-rc.1"
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
      "loading": "Memuat…",
      "aboutTitle": "Tentang Tredecadia",
      "aboutSummary": "Halaman ini adalah ringkasan navigasi, bukan salinan kedua standar. Persyaratan normatif tetap berada di spesifikasi repositori dan registri yang dapat dibaca mesin.",
      "factStructure": "13 bulan sama panjang × 28 hari = 364 hari reguler; setiap bulan berisi empat minggu penuh tujuh hari.",
      "factIntercalary": "EQ — Ekuinoks / Tahun Baru — membuka setiap tahun di luar siklus bulan/minggu; tahun kabisat juga memiliki ED — Hari Bumi.",
      "factEra": "Era Tredecadia (TE) adalah satu sumbu tahun bilangan bulat dengan tahun 0 yang nyata.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo, dan Toze adalah identitas hari dalam minggu yang kanonik dan netral bahasa.",
      "resourcesTitle": "Standar dan sumber",
      "resourcesSummary": "Buka dokumentasi proyek lengkap dalam bahasa yang dipilih atau lihat rilis yang telah diterbitkan.",
      "allLanguages": "Semua bahasa",
      "stableRelease": "Stabil v1.0.0",
      "prerelease": "Prarilis v1.1.0-rc.1"
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
      "loading": "Đang tải…",
      "aboutTitle": "Về Tredecadia",
      "aboutSummary": "Trang này là bản tóm tắt điều hướng, không phải bản sao thứ hai của tiêu chuẩn. Các yêu cầu quy chuẩn vẫn nằm trong đặc tả kho mã và các sổ đăng ký máy đọc được.",
      "factStructure": "13 tháng bằng nhau × 28 ngày = 364 ngày thường; mỗi tháng có bốn tuần đầy đủ, mỗi tuần bảy ngày.",
      "factIntercalary": "EQ — Xuân phân / Năm mới — mở đầu mỗi năm ngoài chu kỳ tháng/tuần; năm nhuận còn có ED — Ngày Trái Đất.",
      "factEra": "Kỷ nguyên Tredecadia (TE) là một trục năm số nguyên duy nhất với năm 0 thực.",
      "factWeekdays": "Mene, Noko, Kese, Zoyo, Sote, Yemo và Toze là các định danh ngày trong tuần chuẩn, trung lập ngôn ngữ.",
      "resourcesTitle": "Tiêu chuẩn và tài nguyên",
      "resourcesSummary": "Mở tài liệu đầy đủ của dự án bằng ngôn ngữ đã chọn hoặc xem các bản phát hành đã công bố.",
      "allLanguages": "Tất cả ngôn ngữ",
      "stableRelease": "Ổn định v1.0.0",
      "prerelease": "Bản tiền phát hành v1.1.0-rc.1"
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

    if (normalized.startsWith("zh-hant") || normalized.startsWith("zh-tw") || normalized.startsWith("zh-hk") || normalized.startsWith("zh-mo")) return "zh-TW";
    if (normalized.startsWith("zh-hans") || normalized.startsWith("zh-cn") || normalized.startsWith("zh-sg") || normalized === "zh") return "zh-CN";
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
