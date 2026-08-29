# AI Translation Disclosure Gate

Dieses Gate ist fuer jede englische Edition verbindlich, bevor der KDP-Submission-Pfad als freigegeben gelten darf.

## Grundlage

Amazon KDP unterscheidet zwischen `AI-generated` und `AI-assisted` Content. Eine Uebersetzung gilt als `AI-generated`, wenn ein KI-basiertes Werkzeug den eigentlichen Uebersetzungstext erzeugt hat. Das gilt auch dann, wenn der Text anschliessend umfangreich menschlich redigiert wurde.

Die jeweils aktuelle KDP-Regel ist vor Submission gegen die offizielle KDP-Dokumentation zu pruefen. Das Framework darf diese Klassifikation nicht stillschweigend annehmen oder offenlassen.

## Blocking Gate

Vor KDP-Submission muss die Frage explizit beantwortet sein:

> **Wurde der eigentliche Text dieser Uebersetzung durch ein KI-basiertes Werkzeug erzeugt?**

Zulaessige Entscheidungen:

- `YES` – AI-generated translation.
- `NO` – keine AI-generated translation; KI wurde hoechstens assistierend eingesetzt oder gar nicht eingesetzt.

`UNRESOLVED`, `null`, ein leeres Feld oder nur `checked=true` bestehen das Gate **nicht**.

## Entscheidungslogik

### Wenn `YES`

Dann gilt:

- `ai_generated_translation = true`
- `kdp_disclosure_required = true`
- der KDP-Submission-Pfad darf nur fortgesetzt werden, wenn die Offenlegung im KDP-Prozess korrekt vorgenommen wird,
- vor `Final Publish` muss `kdp_disclosure_completed = true` dokumentiert sein.

### Wenn `NO`

Dann gilt:

- `ai_generated_translation = false`
- `kdp_disclosure_required = false`
- die Entscheidung muss mit der realen Provenienz des Textes vereinbar sein.

`NO` darf nicht verwendet werden, nur weil ein AI-generated Ausgangstext spaeter stark menschlich ueberarbeitet wurde.

## Standard fuer den ChatGPT-Lokalisierungsweg

Wenn ChatGPT oder ein anderes KI-System die eigentliche englische Uebersetzung erzeugt und der Mensch/Editor diese anschliessend prueft und redigiert, ist nach der aktuellen KDP-Definition die Entscheidung:

`YES – AI-generated translation`

## Release-Regel

`READY_FOR_KDP_SUBMISSION` ist nur zulaessig, wenn:

1. `ai_generated_translation` explizit `true` oder `false` ist,
2. `kdp_disclosure_required` daraus konsistent abgeleitet ist,
3. bei `true` die notwendige Offenlegung als verbindlicher Submission-Schritt vorgesehen ist.

`FINAL_PUBLISH_APPROVED` ist bei `kdp_disclosure_required = true` erst zulaessig, wenn `kdp_disclosure_completed = true` dokumentiert ist.

## Verantwortungsregel

Dieses Gate ist ein **Compliance Gate**, kein kreativer Human Gate. Wenn die Provenienz eindeutig ist, darf die Klassifikation deterministisch gesetzt werden. Bei unklarer Provenienz wird blockiert und nicht geraten.

Keine Person, Rolle oder Disclosure-Antwort erfinden, um das Gate zu passieren.
