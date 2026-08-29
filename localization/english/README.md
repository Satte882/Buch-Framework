# English Edition

Dieser Baustein konkretisiert `localization/` fuer hochwertige englische Editionen. Er basiert auf dem realen Durchlauf `NORMALFALL` → `REASONABLE MEASURES` und konserviert nur die Schritte, die beim naechsten Buch nachweisbar Rework sparen.

Er ist kein eigener Agenten-Stack. Betriebsmodell bleibt:

> **ChatGPT bearbeitet. GitHub haelt den gueltigen Stand. Der Mensch entscheidet nur an irreversiblen Punkten.**

## Ziel

Aus einem finalen deutschsprachigen Manuskript reproduzierbar eine:

- literarisch tragfaehige `en-US`-Edition,
- KDP-taugliche Paperback-Datei,
- reflowable EPUB-Edition,
- konsistente Publishing-/KDP-Metadatenbasis

erzeugen, ohne die bei `REASONABLE MEASURES` einmalig notwendigen technischen und redaktionellen Lernschleifen zu wiederholen.

## Der kuenftige Standardablauf

### 1. Source Freeze + English Profile

Vor der ersten Uebersetzung festlegen:

- exakte Source-Datei und Git-Commit,
- Zielvariante, standardmaessig `English (US)`,
- deutsche Institutionen/Orte bleiben deutsch, sofern keine explizite andere Entscheidung getroffen wird,
- keine Amerikanisierung deutscher Rechts-, Polizei- oder Verwaltungslogik,
- `LOCALIZATION_PROFILE.md`, `STYLE_GUIDE.md`, `GLOSSARY.md` anlegen.

### 2. Pilot – genau ein fruehes Human Gate

Pilotumfang:

- Prolog,
- 2–3 repraesentative Kapitel,
- mindestens eine Dialogszene,
- wenn moeglich eine institutionelle/fachliche Szene und eine Szene mit innerer Stimme unter Druck.

Der Mensch entscheidet einmal:

`VOICE APPROVED | REWORK`

Nach `VOICE APPROVED` wird die Stimme eingefroren.

**Nicht mehr tun:** nach jedem weiteren Kapitelblock erneut um Freigabe bitten. Danach nur anhalten, wenn eine echte semantische, kulturelle oder Source-Entscheidung notwendig wird.

### 3. Volluebertragung ohne kuenstliche Zwischenstopps

Fuer jedes Kapitel:

1. literarische Uebertragung,
2. direkter Source-Abgleich,
3. English Editorial Pass,
4. neue wiederkehrende Begriffe ins Glossary,
5. eindeutige idiomatische Fehler direkt korrigieren.

Keine langen Review-Berichte erzeugen, wenn keine Entscheidung offen ist.

### 4. Ein Global-QA-Pass am Ende

Nach dem letzten Kapitel genau einen buchweiten Konsistenzpass durchfuehren.

Pflichtfelder:

- Namen, Zahlen, Orte, Zeiten,
- Figurenstimmen,
- institutionelle Terminologie,
- US-/UK-Mischung,
- Translation Drift,
- wiederkehrende Germanismen/False Friends,
- Mehrdeutigkeiten, die erst im Englischen entstehen,
- Source-Kontinuitaetsfehler.

Typische Warnmuster aus dem ersten realen Durchlauf:

- deutsche Verwaltungsnominalisierung im Englischen,
- woertliche Konstruktionen fuer `Pruefung`, `Gegenlesart`, `Lagebild`, `Stand`, `Massnahme`,
- scheinbar korrekte, aber unidiomatische Komposita,
- englische Woerter mit neuer Mehrdeutigkeit, z. B. `case`,
- nach spaeteren Kapiteln driftende Fachbegriffe.

Regel:

> Nicht global glaetten. Nur belegte Inkonsistenzen und klare Uebersetzungsartefakte korrigieren.

## Titel-Gate vor Publishing Production

Der Markttitel ist eine eigenstaendige Lokalisierungsentscheidung, keine Uebersetzung des deutschen Titels.

Vor Front Matter, finalem DOCX und KDP-Metadaten muss ein zentraler Publishing-Status existieren:

- `working_title`,
- `market_title`,
- `market_title_status: open | approved`,
- `subtitle`.

Solange `market_title_status = open`, duerfen technische Builds mit Arbeitstitel entstehen, aber keine finalen KDP-Metadaten behauptet werden.

**Damit entfaellt beim naechsten Buch die spaete Titel-Umarbeitung von Front Matter, Config und Produktionsdateien.**

## English Paperback Production

Die deutsche Print-Geometrie darf wiederverwendet werden. Die deutsche Sprachlogik darf **nicht** ungeprueft wiederverwendet werden.

### Verbindliche English-Defaults

- Sprache/Run-Language: `en-US`,
- englische Anfuehrungszeichen,
- englische Trennlogik,
- kein deutscher Guillemets-/Hyphenation-Pass,
- Print und eBook getrennt behandeln.

### Bekannte technische Falle: TOC / LibreOffice

Beim TOC-Roundtrip kann LibreOffice Word-Styles umbenennen oder normalisieren.

Deshalb:

- Kapitel nicht nur ueber den sichtbaren Style-Namen erkennen,
- Kapitelueberschriften strukturell am kontrollierten Text-/Kapitelmuster erkennen,
- `Heading 1` nach dem TOC-Pass bei Bedarf explizit wiederherstellen,
- danach erneut Layout-Regression laufen lassen.

**Diese Schleife darf beim naechsten Buch nicht erst durch einen fehlgeschlagenen Build entdeckt werden.**

### Bekannte technische Falle: Hyphenation

Automatische englische Trennung ist im Fliesstext sinnvoll, aber nicht in:

- Front Matter,
- Inhaltsverzeichnis,
- Kapitelueberschriften.

Dort `suppressAutoHyphens` bzw. das funktionale Aequivalent von Anfang an setzen.

Damit werden Fehler wie getrennte Kapitelwoerter bereits im ersten Build verhindert.

## Print-QA: technisch + visuell

Ein gruener XML-/DOCX-Test reicht nicht.

Pflichtfolge:

1. DOCX bauen,
2. Layout-/Strukturtests,
3. in derselben CI-/Runner-Umgebung nach PDF rendern,
4. Seitenzahl als technischer Guard pruefen,
5. gesamtes PDF visuell ueber Kontaktboegen/Seitenuebersicht sichten,
6. auffaellige Seiten in voller Aufloesung pruefen,
7. nach einem Fix nur noch Delta-Seiten zwischen altem und neuem Render vergleichen.

Wichtig:

> Die CI-/LibreOffice-Seitenzahl ist **nicht** die finale KDP-Rueckenbreite. Fuer das Print-Cover zaehlt die nach Upload im KDP Previewer bestaetigte Seitenzahl.

Cover daher erst nach KDP-Preview finalisieren.

## Kindle / EPUB ist ein eigener Produktionspfad

Die Print-DOCX wird nicht als Kindle-Produktionsmodell wiederverwendet.

Standard:

- EPUB 3,
- reflowable,
- eigenes interaktives TOC,
- keine Print-Seitenzahlen,
- keine Print-Raender/Spiegelraster,
- Titel aus derselben zentralen Publishing-Config,
- Prolog + alle Kapitel strukturell validieren.

### EPUBCheck ist Pflicht

Der offizielle W3C-`EPUBCheck` wird **von Anfang an** als CI-Gate eingeplant, nicht erst nach einem erfolgreichen Eigenvalidator.

Zielzustand:

`0 fatal / 0 errors / 0 warnings`

Danach folgt nur noch die Kindle-/KDP-Preview-Darstellungskontrolle.

## KDP-Metadaten und Submission

Eine zentrale Publishing-Config ist Source of Truth fuer mindestens:

- Markttitel und Status,
- Subtitle,
- Sprache,
- Zielmarkt,
- Printformat,
- Papier-/Ink-/Bleed-Entscheidung,
- Paperback-/eBook-Artefakt,
- Keywords,
- Kategorien,
- Zielpreise,
- Release-Status.

KDP-spezifische Regeln nicht in die literarische Uebersetzung mischen.

### AI-Uebersetzung

Wenn der Zieltext durch KI erzeugt und anschliessend redigiert wurde, muss beim aktuellen KDP-Prozess die jeweils geltende AI-generated-content-Regel geprueft und korrekt angegeben werden.

Contributor-/Translator-Angaben bleiben ein Human/KDP-Submission-Gate, wenn die Plattform fuer den konkreten AI-Uebersetzungsfall keine eindeutige Eingabelogik vorgibt. Keine Person oder Rolle erfinden.

## Welche Schleifen beim naechsten Buch entfallen

| Erste reale Edition | Kuenftiger Standard |
|---|---|
| nach Voice-Freeze erneut nach Feedback stoppen | genau ein Voice-Gate, danach durchlaufen |
| Titel erst nach DOCX-Produktion finalisieren | Markttitel vor finalem Publishing-Build entscheiden |
| deutsche DOCX-Sprachlogik wiederverwenden und nachbessern | eigene `en-US`-Pipeline von Anfang an |
| TOC-Stylebruch erst im CI-Fehler entdecken | strukturelle Heading-Erkennung sofort |
| Trennung in Heading/TOC erst visuell entdecken | Hyphenation dort von Anfang an unterdruecken |
| technisches QA zuerst, visuelles QA spaet | Runner-PDF und Kontaktbogen im Standardprozess |
| Kindle aus Printproduktion mitdenken | separater EPUB-3-Pfad |
| EPUBCheck nachtraeglich ergaenzen | EPUBCheck als initiales hartes Gate |

## Minimaler Human-Gate-Satz

Fuer die naechste englische Edition reichen im Normalfall vier menschliche Entscheidungen:

1. **Voice Gate** nach Pilot,
2. **Market Title Gate** vor finalem Publishing-Build,
3. **KDP Preview/Cover Gate** nach echter KDP-Seitenzahl,
4. **Final Publish Gate** im KDP-UI.

Alles andere soll ChatGPT + GitHub + deterministische CI ohne weitere Freigabeschleifen abarbeiten.

## Leitprinzip

> **Die erste Edition lernt die Pipeline. Die naechste Edition soll sie nur noch ausfuehren.**
