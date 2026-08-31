# PROSA-Regelmatrix v0.1

Diese Datei ist die fachliche Source of Truth für die in Aufgabe 2 implementierten Prosa-Prüfungen.

Sie zahlt direkt auf `ZIEL.md` ein: wiederholbare, mechanisch prüfbare Qualitätsarbeit wird automatisiert; kontextabhängige Stilentscheidungen bleiben REVIEW- bzw. menschliche Freigabeentscheidungen. Der Scanner verändert niemals Manuskripttext.

## Ebenen und Zuständigkeit

Jede Regel besitzt einen eindeutigen **Scope Owner**:

1. **Core** – nur Scanner-Mechanik: Konfiguration laden, Text segmentieren, Treffer lokalisieren, `FAIL`/`REVIEW`/`INFO` ausgeben, Ausnahmen anwenden. Der Core enthält keine literarischen Stilpräferenzen.
2. **Prosa-Profil** – wiederverwendbare sprachliche Regeln und Warnmuster. v0.1 aktiviert `de_anti_ki_prosa_v1`.
3. **Serienprofil** – optionale Regeln, die nur für eine konkrete Buchreihe gelten. In v0.1 keine aktive Prosa-Regel.
4. **Buch** – optionale Buchdaten und begründete Ausnahmen. Figurennamen und Einzelfall-Overrides gehören ausschließlich hierhin.

**Override-Prinzip:** Core-Mechanik kann nicht durch eine Buchregel umdefiniert werden. Prosa-Regeln können durch Serie/Buch nur enger konfiguriert oder über einen expliziten, begründeten Ausnahme-Eintrag behandelt werden. Es gibt keine stillen Overrides.

## Evidenzklassen

Der NORMALFALL-Korpus ist klein und stammt aus einem einzigen Buch. Deshalb werden keine statistisch starken Aussagen vorgetäuscht.

- `established_project_rule` – bewusste Projektregel, historisch bereits produktiv als harter Guard eingesetzt; nicht aus einer kleinen Stichprobe „gelernt“.
- `provisional` – ausreichend Material für einen ersten reproduzierbaren REVIEW-Detektor, aber noch keine allgemeine Stilregel.
- `provisional_small_sample` – sinnvoller Kandidat, aber zu wenige Fälle für belastbare Performanceaussagen.
- `insufficient_for_review_threshold` – nur deskriptive INFO-Ausgabe; kein Qualitätsgrenzwert.
- `semantic_only` – mit v0.1 nicht deterministisch/heuristisch entschieden.

### Dev/Hold-out-Regel

Die feste Zuordnung steht in `tests/corpus/normalfall_split.json`.

Ein pauschaler 75/25-Split wird **nicht erzwungen**, wenn die Musterfamilie zu klein ist. Insbesondere gilt:

> Eine Kategorie mit weniger als 8 relevanten Fällen erhält aus diesem Korpus allein niemals den Evidenzstatus `strong`.

Wenn im Hold-out weniger als zwei positive **oder** zwei Kontrollfälle vorhanden sind, werden Trefferquoten nur deskriptiv berichtet und nicht als belastbare Precision-/Recall-Aussage interpretiert. Hold-out-Fälle werden nach Ergebnissen nicht umsortiert.

## Vollmanuskript-Rauschtest

Vor produktivem Einsatz wurde `scripts/prosa_audit.py` am 29.08.2026 in GitHub Actions gegen das vollständige kanonische `Satte882/Buch/AUSNAHMEZUSTAND_FINAL.md` ausgeführt. Der erste Lauf auf Scanner-Stand `577547cee42fb1d9b9a7e9930336dc56f8ef9456` ergab:

- `FAIL`: 0
- `REVIEW`: 708
- `INFO`: 43
- davon `staccato_sequence`: 403
- davon `dialogue_pingpong`: 268
- davon `negation_sequence`: 37
- `softener_density`: 12
- `filter_terms`: 31

Dieser Lauf war methodisch entscheidend: Die synthetischen Tests waren korrekt, aber die beiden breiten Strukturdetektoren erzeugten auf einem bereits stark überarbeiteten finalen Roman zu viel Rauschen für einen REVIEW-Status.

**Entscheidung:** Die Schwellen werden nicht nachträglich auf NORMALFALL hochoptimiert. Stattdessen werden `staccato_sequence` und `dialogue_pingpong` in v0.1 auf **INFO** zurückgestuft. Ihre Detektoren bleiben als Messinstrument erhalten, bis mehr passendes positives und negatives Material oder ein präziserer Detektor vorliegt. `negation_sequence` bleibt wegen des deutlich kleineren Kandidatenvolumens vorläufig REVIEW.

## Whole-Manuscript-Aggregation

Der Real-Pilot `Satte882/ABWEICHUNG` hat eine wichtige Grenze lokaler Scanner-Severity bestätigt:

> Ein einzelner `dialogue_pingpong`-Treffer kann lokal nur INFO sein. Wenn dieselbe Rhythmusmechanik jedoch über viele Szenen und ähnliche Szenentypen verteilt dominiert, kann daraus **semantisch** ein manuskriptweites Major-Risiko entstehen.

Daraus folgt **keine** automatische Severity-Promotion im Scanner.

Stattdessen gilt für G3/G4:

1. lokale Scanner-Treffer bleiben in ihrer technischen Severity unverändert;
2. zusätzlich werden Treffer **pro Szene und über Sequenzen** aggregiert;
3. der unabhängige Whole-Manuscript-Review bewertet Verteilung, Vorhersagbarkeit und Ermüdungswirkung;
4. nur ein semantisch bestätigter Befund darf daraus einen Major machen.

Zu tracken sind insbesondere:

- `dialogue_pingpong`-Dichte pro Szene und über zusammenhängende Szenenfolgen,
- `staccato_sequence`-Häufung über Szenengrenzen,
- wiederkehrende Blick-/Übergangsformeln,
- gleiche Eröffnungs-/Schlussmechaniken,
- semantische `explanation_echo`-/Kontrast-/Symmetrie-Muster,
- Verhältnis von körperlicher/handlungsgetragener Präsenz zu Analyse-/Policy-Szenen.

**KISS:** v0.1 verlangt dafür keine neue automatisierte literarische Score-Engine. Vorhandene Zählungen dienen als Orientierung; die Entscheidung bleibt semantisch und wird anschließend adjudiziert.

---

## Regelmatrix

| Rule ID | Scope Owner | Muster | Korpus-Evidenz | Detektor v0.1 | Severity | Schwelle / Entscheidung | Evidenzstatus | Auto-Rewrite |
|---|---|---|---|---|---|---|---|---|
| `forbidden_sondern` | **Prosa-Profil** | Wort `sondern` | Positiv 01–10; historischer CI-Guard in NORMALFALL | Regex/Wortgrenze | **FAIL** | jedes nicht ausgenommene `\bsondern\b` | `established_project_rule` | nein |
| `forbidden_em_dash` | **Prosa-Profil** | Geviertstrich `—` im deutschsprachigen Romantext | historischer Typografie- und CI-Guard in NORMALFALL | Literalzeichen | **FAIL** | jedes nicht ausgenommene `—`; notwendiger Gedankenstrich ist `–` | `established_project_rule` | nein |
| `softener_density` | **Prosa-Profil** | Häufung von `vielleicht`, `möglicherweise`, `vermutlich`, `offenbar`, `schien`, `wirkte`, `könnte`, `soweit`, `zumindest` | Positiv 49; zahlreiche akzeptierte Einzel-/Doppelfälle K01–K20 | Rolling word window | **INFO** | 120-Wort-Fenster; `reporting_floor=2` dient nur der Reportbegrenzung, **nicht** als Qualitätsgrenze | `insufficient_for_review_threshold` | nein |
| `negation_sequence` | **Prosa-Profil** | kurze aufeinanderfolgende `Nicht`/`Kein`-Absätze | positive Negations-/Erklärfälle; Kontrollen K27–K31 | Absatzstruktur | **REVIEW** | ab 2 direkt aufeinanderfolgenden kurzen Negationsabsätzen, max. 12 Wörter je Absatz | `provisional_small_sample` | nein |
| `staccato_sequence` | **Prosa-Profil** | Kette sehr kurzer narrativer Absätze | mehrere gekürzte Stakkato-Fälle; mehrere akzeptierte kurze Formen; Vollmanuskript-Test: 403 Treffer | Absatzstruktur | **INFO** | ab 3 narrativen Absätzen mit max. 7 Wörtern; Dialog ausgeschlossen; rein deskriptiv | `insufficient_for_review_threshold` | nein |
| `dialogue_pingpong` | **Prosa-Profil** | schnelle kleinteilige Frage-/Antwort-/Bestätigungskette | Positiv 28–35; Kontrollmaterial K21–K26; Vollmanuskript-Test: 268 Treffer | Dialogabsatzstruktur | **INFO** | ab 4 direkt aufeinanderfolgenden Dialogabsätzen mit max. 10 Wörtern; rein deskriptiv | `insufficient_for_review_threshold` | nein |
| `filter_terms` | **Prosa-Profil** | Dichte von `merkte`, `bemerkte`, `wusste`, `dachte` | Positiv 43–45; wenig exakt passendes Kontrollmaterial | Kapitelzählung | **INFO** | ab 2 Treffern pro Kapitel wird gezählt/berichtet; kein Qualitätsgrenzwert | `insufficient_for_review_threshold` | nein |
| `binary_contrast_without_sondern` | **Prosa-Profil** | semantische Ausweichform `Nicht X. Y.` u. ä. | mehrere positive Kontrastfälle; gemischte legitime Negationen | – in v0.1 | später REVIEW | kein mechanischer Grenzwert | `semantic_only` | nein |
| `explanation_echo` | **Prosa-Profil** | bereits verständliche Handlung/Dialog wird nachträglich erklärt | Positiv u. a. 22, 23, 25, 36, 39, 40 | – in v0.1 | später REVIEW | kontextuell | `semantic_only` | nein |
| `method_or_proof_prose` | **Prosa-Profil** | sichtbare Methodik-/Beweisführung in Romanprosa | Positiv u. a. 38, 41 | – in v0.1 | später REVIEW | kontextuell | `semantic_only` | nein |
| `over_symmetry` | **Prosa-Profil** | zu saubere rhetorische Spiegelung/Dreierstruktur | Positiv 11–15, Kontrollen mit legitimer kurzer Parallelität | – in v0.1 | später REVIEW | kein mechanischer Grenzwert | `semantic_only` | nein |

### Warum `sondern` kein Core-Rule ist

Der Core muss jedes Buch analysieren können, ohne selbst zu behaupten, dass ein bestimmtes deutsches Wort „schlecht“ sei. `sondern = 0` ist deshalb Eigentum des **Prosa-Profils `de_anti_ki_prosa_v1`**. Das Framework kann später andere Prosa-Profile laden.

Die Regel bleibt in diesem Profil absichtlich hart, weil NORMALFALL sie bereits produktiv als Zero-Tolerance-Guard verwendet hat. Ausnahmen sind möglich, aber ausschließlich explizit in `config/prosa_rules.yml` mit `match` und `reason`. Es gibt keinen Inline-`noqa`-Marker im Romantext.

### Warum `—` im deutschen Prosa-Profil ein Hard Guard ist

Der Geviertstrich ist nicht grundsätzlich ein sprachlicher Fehler. Für das deutschsprachige Romanprofil wurde jedoch bereits bei `NORMALFALL` bewusst der **Halbgeviertstrich `–`** als Gedankenstrich festgelegt und `—` per CI ausgeschlossen.

Deshalb gilt profilbezogen:

> `— = 0` im finalen Romantext.

Das ist eine deterministische Typografie-Regel, keine semantische Stilbewertung. Sie verhindert zugleich, dass ein im deutschsprachigen Buchsatz ungewolltes und bei LLM-Prosa auffällig häufiges Zeichen unbemerkt in die finale Ausgabe gelangt.

## Ausnahmen

Ein legitimer Sonderfall wird nicht durch Änderung des Scanners versteckt, sondern konfiguriert:

```json
{
  "match": "exakte unveränderbare Passage",
  "reason": "Originalzitat; darf nicht redaktionell verändert werden"
}
```

Default ist eine leere Ausnahmeliste.

## Figurennamen

NORMALFALL-Namen dürfen in den Korpusdateien vorkommen, aber **nicht in produktiven Regeln**. Der Scanner arbeitet in v0.1 bei Filterwörtern ausschließlich mit Verben. Falls spätere Regeln Figurenbezug benötigen, kommen Namen aus der Buchkonfiguration (`characters`) und nicht aus dem Prosa-Profil.

## Semantischer LLM-Kontextreview

Der LLM-Kontextreview ist in v0.1 **spezifiziert, aber nicht implementiert**.

Er läuft später ausschließlich:

1. manuell, wenn ein Prosa-Batch zur menschlichen Freigabe vorgelegt wird;
2. manuell, beim finalen Prosa-Gate des Gesamtmanuskripts.

Bei längeren Romanen umfasst G3 neben repräsentativen Einzelszenen zusätzlich einen **zusammenhängenden Mittelteil-Run von mindestens 6 Szenen**, damit globale Muster früher sichtbar werden.

Er läuft **nicht**:

- bei jedem Commit,
- als CI-API-Aufruf,
- als automatische Umschreibepipeline.

Input soll später sein: Treffer/Kandidat + lokaler Kontext + passende positive Korpusfälle + passende Kontrollfälle; bei Whole-Manuscript-Prüfungen zusätzlich die Verteilung über Szenen/Sequenzen. Output: konkretes Finding oder `unklar`, mit kurzer Evidenz. Keine automatische Manuskriptänderung.

Raw-Findings werden anschließend gemäß `SEMANTIC_REVIEW_PROTOCOL.md` adjudiziert. Ein Reviewer darf seine eigene Severity nicht automatisch in einen Gate-Blocker verwandeln.

## Promotion einer Regel

Eine Musterfamilie darf nur in dieser Richtung aufsteigen:

`INFO → REVIEW → FAIL`

- **INFO → REVIEW:** erst wenn positives und negatives Material die Prüfung sinnvoll kalibrierbar macht **und** ein Vollmanuskript-Rauschtest ein praktisch nutzbares Kandidatenvolumen zeigt.
- **REVIEW → FAIL:** nur bei sehr hoher Eindeutigkeit **und** bewusster Projekt-/Profilentscheidung.
- Ein kleines Hold-out allein macht eine Regel niemals „stark“.
- False Positives bei REVIEW sind zulässig; REVIEW bedeutet bewusst „ansehen“, nicht „ändern“.
- Eine manuskriptweite semantische Häufung ändert nicht automatisch die technische Rule-Severity des Scanners.

## Definition of Done für v0.1

- jede implementierte Regel hat einen `scope`;
- keine NORMALFALL-Figur ist in produktiven Regeln hardcodiert;
- `FAIL` wird nur durch deterministische Regeln ausgelöst;
- REVIEW/INFO blockieren den Prozess nicht;
- Ausnahmen sind explizit und begründet;
- Scanner verändert keinen Text;
- Dev/Hold-out-Zuordnung ist festgeschrieben;
- Tests unterscheiden Softwarekorrektheit von literarischer Evidenz;
- ein Vollmanuskript-Rauschtest ist Teil der Validierung;
- Whole-Manuscript-Aggregation wird in G3/G4 semantisch mitgelesen;
- LLM-Review ist nicht Teil von CI und nicht automatisch aktiv;
- Finding-Adjudikation bleibt vom Raw-Review getrennt.