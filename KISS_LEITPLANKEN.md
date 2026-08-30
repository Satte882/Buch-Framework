# KISS-Leitplanken für das Buch-Framework

## Zweck

Das Framework soll Buchproduktion vereinfachen. Es darf nicht selbst zum größeren Projekt als das Buch werden.

Diese Leitplanken operationalisieren das Entwicklungsprinzip aus `ZIEL.md`:

> **Nicht maximale Automatisierung ist das Ziel, sondern reproduzierbar hohe Buchqualität bei möglichst wenig unnötiger manueller Arbeit.**

Die verbindliche fachliche Arbeitsweise steht in `ARBEITSWEISE.md`.

## Standardarchitektur v0.x

Für v0.x gilt als Default:

1. **ChatGPT-Chat** für generative und semantische Arbeit.
2. **GitHub-Dateien** als Source of Truth und Arbeitsartefakte.
3. **Human Gates** nur an irreversiblen oder teuer rückholbaren Entscheidungen.
4. **Kleine deterministische Python-Checks** nur für wiederholbare, eindeutig prüfbare Regeln.
5. **GitHub Actions** nur für deterministische Tests, Checks und Builds.

## Kein Gate pro Artefakt

Eine neue Entwicklungsebene, Datei oder Template erzeugt **nicht automatisch einen neuen Human Gate**.

Verbindliche Prüffrage vor jedem zusätzlichen Gate:

> **Welche konkrete irreversible Entscheidung schützt dieser zusätzliche Stopp, die nicht sinnvoll im nächsten gebündelten Gate geprüft werden kann?**

Gibt es darauf keine klare Antwort, wird der Gate nicht eingeführt.

Für v0.x werden die internen Ebenen bewusst in sechs Freigabephasen gebündelt: Konzept, Story-Architektur, Prose Ready, Prosa-Stil, Manuskript, Produktion.

## Gate-Batching statt Gate-Vermehrung

Ein großer Human Gate darf aus mehreren Review-Batches bestehen. Das ist bei langen Romanen ausdrücklich erwünscht, wenn ein einziger Prüfblock zu groß wird.

Beispiel: Szenen 1–15, 16–30 und 31–45 können getrennt geprüft werden und trotzdem Teil derselben fachlichen `Prose Ready`-Freigabephase bleiben.

Es werden dafür nicht automatisch neue Gate-Typen wie `G2a`, `G2b`, `G2c` eingeführt.

## Selbstprüfung ist keine unabhängige Qualitätssicherung

ChatGPT darf eigene Artefakte mechanisch und semantisch vorprüfen. Dabei gilt:

- Pflichtfelder, IDs, Referenzen und Vollständigkeit dürfen deterministisch geprüft werden.
- Inhaltliche Selbstprüfung darf Hinweise liefern.
- Dieselbe KI ersetzt damit weder Human Gate noch einen bewusst entkoppelten Red-Team-Review.

Diese Grenze verhindert, dass eine interne Selbstprüfung als unabhängige Qualitätskontrolle missverstanden wird.

## Bedeutung von „Engine“

Begriffe wie Story Engine, Prose Engine oder Quality Engine bezeichnen zunächst **fachliche Verantwortungsbereiche bzw. Chat-Workflows**.

Sie bedeuten ausdrücklich nicht automatisch:

- eigener Service,
- eigene Runtime,
- eigene Datenbank,
- eigener Provider-Adapter,
- eigener Agent,
- eigene Queue,
- eigener CI-Workflow.

## Build-vs.-Chat-vs.-Template-Check

Vor jeder neuen technischen Komponente müssen diese Fragen beantwortet werden:

1. Welches wiederkehrende Problem wird konkret gelöst?
2. Wie häufig ist das Problem im realen Buchprozess bereits aufgetreten?
3. Welches Downstream-Rework oder welche Qualitätsgefahr wird dadurch reduziert?
4. Reicht bereits:
   - ein klareres Template,
   - eine dokumentierte Regel,
   - ein Chat-Auftrag,
   - ein bestehender Human Gate?
5. Muss die Aufgabe wirklich deterministisch automatisiert werden?
6. Welche Wartungs- und Komplexitätskosten entstehen?

Wenn der konkrete Zusatznutzen gegenüber `Artefakt + ChatGPT + Gate` nicht klar ist, wird die technische Komponente **nicht gebaut**.

## Wann Code sinnvoll ist

Code ist bevorzugt bei Aufgaben mit mindestens einer dieser Eigenschaften:

- eindeutige Pflichtfelder oder Referenzen,
- reproduzierbare Konsistenzprüfung,
- wiederkehrende Text-/Strukturmuster mit vertretbarer False-Positive-Rate,
- Build-/Formatierungsaufgaben,
- Invalidierungs-/Hash-Prüfungen,
- wiederkehrende mechanische Arbeit, die im Chat unnötig fehleranfällig wäre.

## Wann Chat bevorzugt wird

Chat ist bevorzugt bei:

- Prämissen- und Plotentwicklung,
- Figurenentwicklung,
- Bewertung von Alternativen,
- semantischem Red-Team,
- Prosaerzeugung,
- kontextabhängigem Lektorat,
- Interpretation von Qualitätsbefunden.

## Recherche: KISS-Blockierregel

Eine offene Recherchefrage blockiert die aktuelle Entwicklungsebene nur dann, wenn ihre Antwort eine **jetzt zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung** verändern kann.

Für v0.x wird dafür bewusst kein Score und keine zusätzliche Matrix gebaut. Erst reales wiederkehrendes Fehlverhalten rechtfertigt mehr Mechanik.

## Persistenz

Neue persistente Infrastruktur ist nicht erlaubt, solange Folgendes ausreicht:

- Markdown-/JSON-/YAML-Artefakte,
- Git-Historie,
- feste Git-Referenzen/Hashes,
- kleine Provenienzrecords.

Insbesondere wird für v0.x keine Datenbank eingeführt.

## CI-Grenze

CI darf niemals zur Voraussetzung für generative Chat-Arbeit werden.

CI darf prüfen:

- Contracts,
- Referenzen,
- Gate-Status,
- Tests,
- Prosa-Audit,
- Builds,
- deterministische Invalidierungsregeln.

CI erzeugt keine Story, keine Figuren, keine Prosa und keine semantischen Freigaben.

## Ausbaukriterium

Ein fachlicher Bereich erhält erst tiefere technische Automatisierung, wenn mindestens eines belegt ist:

1. wiederholtes reales Downstream-Rework,
2. häufige manuelle Fehler,
3. unnötig hoher wiederkehrender Zeitaufwand,
4. fehlende Reproduzierbarkeit einer mechanischen Aufgabe,
5. konkrete Lücke zu `ZIEL.md`, die nicht einfacher geschlossen werden kann.

## Leitregel

> **So viel Entwicklungstiefe wie für Qualität nötig, so wenige Prozessstopps und so wenig Infrastruktur wie möglich.**
