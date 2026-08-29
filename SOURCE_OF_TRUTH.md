# Source of Truth, Ableitung und Invalidierung

## Zweck

Dieses Dokument verhindert, dass Story-, Figuren- oder Rechercheentscheidungen durch spätere Prosa stillschweigend verändert werden. Es definiert für v0.x die kanonischen Artefakte, die Richtung von Änderungen und den Umgang mit veralteten Downstream-Artefakten.

## Kanonische Ebenen

### 1. Buchidee / Prämisse

Kanonisch nach G0:

- `BOOK_IDEA.md`

### 2. Storyarchitektur

Kanonisch nach G1:

- `STORY_PACKAGE.md`

Hier liegen plotrelevante Entscheidungen wie zentraler Konflikt, Leitfrage, Mechanismus, Protagonistenbogen, Reversal und Informationsarchitektur.

### 3. Figuren- und Recherchebasis

Kanonisch nach G2:

- `CHARACTERS.md`
- `RESEARCH_REGISTER.md`

### 4. Szenenwahrheit

Kanonisch nach G3:

- freigegebener `SCENE_PLAN`
- referenzierte `CHARACTER_STATE`-Artefakte
- für die Szene relevante aufgelöste Rechercheentscheidungen

### 5. Prosa

Prosa ist **abgeleitet**.

Ein Draft darf die freigegebene Szenenwahrheit ausgestalten, rhythmisieren, konkretisieren und sprachlich verdichten. Er darf keine neue relevante Plot-, Figuren-, Wissens-, Recherche-, Informations- oder Konsequenzentscheidung heimlich zur kanonischen Wahrheit machen.

### 6. Kanonisches Manuskript

Ein Prosa-Draft wird erst nach dem vorgesehenen menschlichen Gate und den erforderlichen Checks Teil des kanonischen Manuskripts.

## Einbahnstraßenregel

Die normale Ableitungsrichtung lautet:

`BOOK_IDEA → STORY_PACKAGE → CHARACTERS/RESEARCH → SCENE_PLAN/CHARACTER_STATE → PROSA → MANUSKRIPT`

Prosa aktualisiert **niemals automatisch** einen Upstream-State.

Wenn beim Schreiben eine bessere Storyentscheidung entdeckt wird, gilt Backtracking statt Sync.

## Backtracking-Regel

Soll eine Prosaänderung eine relevante Storywahrheit verändern:

1. Änderung nicht nur im Draft vornehmen.
2. Betroffenes kanonisches Upstream-Artefakt identifizieren.
3. Änderung dort einarbeiten.
4. Erforderlichen Human Gate erneut durchlaufen.
5. Abhängige Downstream-Artefakte als `stale` oder `invalidated` markieren.
6. Betroffene Szenen/Drafts neu prüfen bzw. neu erzeugen.

> **Die Planung darf sich verbessern. Die Prosa darf sie nicht heimlich überschreiben.**

## Upstream-Referenzen

Ein abgeleitetes generatives Artefakt muss seine relevanten Inputs referenzieren. Für v0.x reichen Git-basierte Referenzen.

Beispiel:

```yaml
upstream:
  - path: scenes/S-001.md
    ref: <blob-sha-oder-commit>
  - path: character_states/S-001_Alex.md
    ref: <blob-sha-oder-commit>
  - path: RESEARCH_REGISTER.md
    ref: <blob-sha-oder-commit>
```

Wo ein externes Repository als kanonische Quelle dient, müssen Repository, Pfad und feste Git-Referenz eindeutig genannt werden.

## Statusmodell für abgeleitete Artefakte

Erlaubte Zustände:

- `draft` – erzeugt, noch nicht menschlich freigegeben,
- `accepted` – erforderlicher Gate wurde bestanden,
- `stale` – ein relevanter Upstream-Stand hat sich geändert; erneute Prüfung/Erzeugung erforderlich,
- `invalidated` – Artefakt darf nicht weiterverwendet werden.

`stale` und `invalidated` dürfen nicht in ein kanonisches Manuskript übernommen werden.

## Invalidierungsregel

Ein Downstream-Artefakt ist mindestens dann `stale`, wenn sich nach seiner Erzeugung ein referenzierter relevanter Upstream-Stand ändert.

Für v0.x muss nicht jede semantische Abhängigkeit automatisch erkannt werden. Entscheidend ist:

1. Referenzen sind explizit,
2. eine bekannte Änderung wird nicht ignoriert,
3. der betroffene Downstream-Status wird sichtbar aktualisiert,
4. vor weiterer Verwendung findet erneute Prüfung statt.

Deterministische Hash-/Referenzprüfungen dürfen später ergänzt werden, wenn sie real Rework sparen. Eine Datenbank ist dafür nicht erforderlich.

## Prosaänderungen ohne Upstream-Änderung

Reine sprachliche Überarbeitungen – Rhythmus, Wortwahl, Satzbau, Kürzung von Erklär-Echos – verändern den Story-/Character-State nicht automatisch.

Ein semantischer Review darf einen Widerspruch melden. Er darf keinen State selbst aktualisieren.

## Human Gates

Ein Human Gate bezieht sich immer auf einen konkreten Artefaktstand. Wird dieser Stand inhaltlich relevant geändert, gilt eine frühere Freigabe nicht automatisch für die neue Version.

## Leitregel

> **Upstream definiert die Storywahrheit. Downstream wird daraus abgeleitet. Relevante Änderungen wandern zuerst zurück zur Quelle und dann wieder vorwärts durch die betroffenen Gates.**
