# Verbindliche Projektstruktur für Buch-Repositories

## Zweck

Dieses Dokument definiert, **wie ein echtes Buch-Repository mit dem Buch-Framework aufgebaut wird**.

Die Verzeichnisstruktur bildet die fachliche Ableitung vom Groben ins Feine ab. Entwicklungsebenen werden deshalb **nicht als parallele Top-Level-Ordner** nebeneinandergestellt.

> **Die Ordnerhierarchie folgt der Storyhierarchie. Prosa ist die unterste Ebene.**

## Verbindliche Grundstruktur

```text
BUCH-REPO/
├── README.md
├── BOOK_IDEA.md
├── STORY_PACKAGE.md
├── CHARACTERS.md
├── RESEARCH_REGISTER.md
├── gates/
│
└── BAUSTEINE/
    ├── README.md
    ├── B01/
    │   ├── BAUSTEIN.md
    │   ├── EVENTS.md
    │   └── SZENEN/
    │       ├── S001/
    │       │   ├── SZENE.md
    │       │   ├── BEATS.md
    │       │   ├── CHARACTER_STATES.md
    │       │   └── PROSA.md
    │       └── S002/
    │           └── ...
    ├── B02/
    │   └── ...
    └── Bxx/
        └── ...
```

Leere zukünftige Ordner müssen nicht künstlich mit `.gitkeep` angelegt werden. Eine Ebene entsteht erst, wenn sie fachlich bearbeitet wird.

## 1. Meta-Ebene – Root

Auf der obersten Ebene liegen nur Artefakte, die das **gesamte Buch** betreffen oder quer durch mehrere Storyebenen wirken:

- `BOOK_IDEA.md` – Thema, Prämisse, Leitfrage, Leser-Versprechen, Nicht-Ziele,
- `STORY_PACKAGE.md` – Gesamtmechanismus, Konflikt, große Wendungen, Informationsarchitektur,
- `CHARACTERS.md` – Figurenkern und große Beziehungsbögen,
- `RESEARCH_REGISTER.md` – bekannte Rechercheabhängigkeiten,
- `gates/` – Human-Gate-Records,
- Review-/Betriebsartefakte, sofern sie das Gesamtprojekt betreffen.

**Figuren und Research sind Querschnittsartefakte und dürfen auf dieser Meta-Ebene bleiben.**

## 2. Baustein-Ebene

Jeder dramaturgische Baustein erhält einen eigenen Ordner:

```text
BAUSTEINE/B07/
├── BAUSTEIN.md
└── EVENTS.md
```

### `BAUSTEIN.md`

Definiert die Makrofunktion dieses Abschnitts:

- Ausgangslage,
- dramaturgische Funktion,
- zentrale Verschiebung / Druck,
- relevante Entscheidung,
- Konsequenz,
- Informationsstrang,
- Figurenkern,
- Research-Abhängigkeiten.

### `EVENTS.md`

Enthält nur die Ereignisse/Sequenzen, die zu diesem Baustein gehören.

Events sind **noch keine Szenen**. Sie definieren, was kausal passieren muss, bevor entschieden wird, wie viele erzählte Szenen dafür benötigt werden.

## 3. Szenen-Ebene

Erst nachdem die Baustein-/Event-Architektur über das gesamte Buch ausreichend geschlossen und G1 freigegeben ist, werden daraus Szenen abgeleitet.

```text
BAUSTEINE/B07/SZENEN/
├── S019/
│   └── SZENE.md
└── S020/
    └── SZENE.md
```

`SZENE.md` definiert die erzählte Einheit, unter anderem:

- Storyfunktion,
- POV,
- Ort/Zeit,
- beteiligte Figuren,
- Event-Referenzen,
- Ziel und Konflikt,
- Entscheidung und Konsequenz,
- Informationsstand vorher/nachher,
- Reveal-Grenzen,
- Research-Abhängigkeiten.

**Zuerst wird die Szenenlandschaft über das gesamte Buch geschlossen.** Erst danach werden die einzelnen Szenen systematisch in Beats zerlegt.

## 4. Beat-Ebene

Beats gehören **zu genau einer Szene** und liegen deshalb in deren Ordner:

```text
BAUSTEINE/B07/SZENEN/S019/BEATS.md
```

Eine Datei pro Szene ist der Standard. Keine eigene Datei pro Beat, solange reale Skalierungserfahrung keinen Nutzen dafür zeigt.

`BEATS.md` beschreibt Schritt für Schritt, was innerhalb dieser Szene passiert. Spätestens hier muss klar sein:

- welche Handlung oder Information den Beat auslöst,
- was sich sichtbar verändert,
- welche Figur handelt/reagiert,
- welche Information neu ist,
- welche Entscheidung oder Konsequenz daraus folgt,
- was ausdrücklich noch nicht bekannt sein darf.

## 5. Character States auf Szenenebene

Szenenspezifische Wissens-, Glaubens-, Ziel- und Beziehungszustände gehören zur konkreten Szene:

```text
BAUSTEINE/B07/SZENEN/S019/CHARACTER_STATES.md
```

Die globale Figurenbaseline bleibt in `CHARACTERS.md`. `CHARACTER_STATES.md` konkretisiert nur den Zustand der in dieser Szene relevanten Figuren vor und nach der Szene.

Wenn eine Szene sehr viele Figuren enthält und eine einzelne Datei unpraktisch wird, darf innerhalb des Szenenordners ein Unterordner `CHARACTER_STATES/` mit einer Datei pro Figur verwendet werden. Das ist eine Skalierungsoption, keine zusätzliche Storyebene.

## 6. Prosa – unterste Ebene

Die Prosa einer Szene liegt direkt bei ihrer vollständig geplanten Szene:

```text
BAUSTEINE/B07/SZENEN/S019/PROSA.md
```

**Prosa ist kein paralleler Arbeitsstrang.** Sie ist das abgeleitete Endprodukt der vollständigen Kette:

`Buchidee → Story Package → Baustein → Events → Szene → Beats / Character States → Prosa`

Systematische Prosa darf erst nach G2 erzeugt werden.

Gate-Frage:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

Wenn nein, wird upstream weitergearbeitet; die fehlende Entscheidung wird nicht in `PROSA.md` improvisiert.

## 7. Horizontalregel bleibt verbindlich

Die Ordnerhierarchie ist vertikal, die Arbeitsweise bleibt horizontal:

1. alle Bausteine über das gesamte Buch schließen,
2. alle Events innerhalb dieser Bausteine schließen,
3. alle Szenen über das gesamte Buch ableiten,
4. alle Szenen in Beats und Character States präzisieren,
5. G2 – Prose Ready,
6. erst danach Prosa.

Damit wird nicht B01 bis zur fertigen Prosa geschrieben, während B18 noch nur als grobe Idee existiert.

## 8. Globale Index-/Checker-Sichten

Für Reviews, CI oder ältere Checker dürfen zusätzlich globale Dateien existieren, zum Beispiel:

- `STORY_BLOCKS.md`,
- `EVENTS.md`,
- `BEATS.md`,
- ein Szenenindex.

Diese Dateien sind in einem hierarchischen Buchprojekt **abgeleitete Gesamtansichten** und keine zweite fachliche Source of Truth.

Regeln:

1. Kanonische Detailänderung immer zuerst in der verschachtelten Storystruktur vornehmen.
2. Globale Sichten danach neu erzeugen/aktualisieren.
3. Nie Root-Index und verschachtelte Datei unabhängig voneinander fortschreiben.
4. Bei Widerspruch gilt die hierarchische kanonische Datei; der Index ist `stale` und muss regeneriert werden.

Historische M1/M2-Fixtures dürfen ihr flaches Layout behalten. Die neue Struktur gilt verbindlich für **neue echte Buchprojekte** und insbesondere für `Satte882/ABWEICHUNG`.

## 9. Human Gates in der Struktur

- **G0** – Root-Konzept (`BOOK_IDEA.md`)
- **G1** – `STORY_PACKAGE.md` + alle `BAUSTEINE/Bxx/BAUSTEIN.md` + alle `EVENTS.md` + Figurenkern + relevante Research-Entscheidungen
- **G2** – alle `SZENE.md` + `BEATS.md` + Character States + blockierende Research-Entscheidungen
- **G3** – repräsentative `PROSA.md`-Stichprobe aus G2-freigegebenen Szenen
- **G4** – vollständiges Manuskript aus allen freigegebenen Szenen-Prosa-Artefakten
- **G5** – konkretes Produktionsartefakt

Die Struktur erzeugt keine zusätzlichen Human Gates.

## 10. Backtracking

Wenn eine tiefere Ebene einen Fehler sichtbar macht, wird die Änderung auf der frühesten betroffenen kanonischen Ebene vorgenommen.

Beispiel:

`PROSA.md` zeigt, dass eine Entscheidung in S019 nicht vorbereitet ist → nicht nur Prosa umschreiben → `BEATS.md`, `SZENE.md`, `EVENTS.md` oder `BAUSTEIN.md` prüfen → betroffene Downstream-Artefakte `stale` markieren → erneut ableiten.

## Leitregel

> **Meta definiert das Buch. Bausteine strukturieren den Roman. Events definieren, was passieren muss. Szenen definieren, was erzählt wird. Beats definieren, wie die Szene abläuft. Prosa schreibt erst das bereits Entschiedene aus.**
