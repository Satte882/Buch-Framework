# M1 – Acceptance Criteria

## Zweck

M1 ist der erste Nachweis, dass das Framework im **realen Chat-Betriebsmodell** den vollständigen Weg von einer Buchidee bis zu einem Produktionsartefakt tragen kann – und dabei die in `ARBEITSWEISE.md` definierte Entwicklung **vom Großen ins Kleine** tatsächlich einhält.

M1 ist kein Beweis für die Qualität oder Skalierbarkeit eines vollständigen Romans.

Verbindliche Grundlagen:

- `ZIEL.md`
- `ARBEITSWEISE.md`
- `BETRIEBSMODELL.md`
- `SOURCE_OF_TRUTH.md`
- `KISS_LEITPLANKEN.md`
- `FRAMEWORK_PIPELINE.md`

## Fester Umfang des M1-Testfalls

Der M1-Testfall umfasst mindestens:

- 1 dokumentierte Buchidee,
- 1 Story Package,
- vollständige dramaturgische Bausteine für den Mini-Fall,
- vollständige Ereignisse/Sequenzen für den Mini-Fall,
- Figurenkern und mindestens 1 plotrelevanten Rechercheeintrag,
- vollständige Beats für den Mini-Fall,
- mindestens 3 daraus abgeleitete Szenenkarten,
- zugehörige Character States,
- mindestens 3 echte Prosa-Drafts,
- einen repräsentativen G3-Prosa-Review,
- ein kanonisches Mini-Manuskript,
- ein finales Test-Produktionsartefakt.

Der generative Teil wird bewusst in ChatGPT ausgeführt. CI erzeugt keine Inhalte.

# Erfolgskriterien

M1 gilt nur dann als bestanden, wenn **alle** folgenden Kriterien erfüllt sind.

## A. Arbeitsweise vom Großen ins Kleine

1. Der Testfall startet mit einem dokumentierten Konzept und durchläuft die Entwicklungsebenen `Bausteine → Ereignisse/Sequenzen → Beats → Szenenkarten → Prosa`.
2. Jede dieser Ebenen wird für den gesamten Mini-Fall ausreichend geschlossen, bevor die nächste Ebene systematisch erzeugt wird.
3. Es wird nicht eine frühe Szene bis zur Prosa entwickelt, während spätere Storyteile noch nur grob oder offen sind.
4. Kein notwendiges Zwischenergebnis existiert ausschließlich im Chat.

## B. Human Gates

5. Es werden die sechs fachlichen Freigabephasen aus `ARBEITSWEISE.md` real verwendet: G0 Konzept, G1 Story-Architektur, G2 Prose Ready, G3 Prosa-Stil, G4 Manuskript, G5 Produktion.
6. Eine interne Entwicklungsebene erzeugt nicht automatisch einen eigenen zusätzlichen Human Gate.
7. Jeder erforderliche Gate-Record bezieht sich auf konkrete Artefaktstände.
8. `APPROVE`, `REWORK` oder `STOP` wird ausschließlich als bewusste menschliche Entscheidung gesetzt.
9. ChatGPT oder ein deterministischer Checker darf keinen menschlichen Gate automatisch freigeben.

## C. Story- und Szenenarchitektur

10. G1 prüft als gebündelte Freigabe mindestens Story Package, alle Bausteine, alle Ereignisse/Sequenzen, Figurenkern und bekannte relevante Rechercheabhängigkeiten.
11. Zwischen Bausteinen und Ereignissen/Sequenzen ist für M1 kein separater Human Gate erforderlich.
12. G2 prüft als gebündelte Freigabe mindestens alle Beats, alle Szenenkarten, Character States und die für diese Planung blockierenden Rechercheentscheidungen.
13. Zwischen Beats und Szenenkarten ist für M1 kein separater Human Gate erforderlich.
14. Mindestens 3 Szenenkarten erreichen G2 = APPROVE.
15. Die Scene-Readiness-Frage ist für jede Prosa-Szene positiv beantwortbar: Beim Schreiben muss keine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung mehr erfunden werden.

## D. Figuren und Recherche als Querschnitt

16. Figurenkern und zentrale Beziehungen werden spätestens in der Story-Architektur festgelegt; szenenspezifische Wissens-/Beziehungszustände werden bis G2 konkretisiert.
17. Mindestens eine reale plotrelevante Recherchefrage wird erfasst und entsprechend ihrer Abhängigkeit behandelt.
18. Eine offene Recherchefrage blockiert nur dann, wenn ihre Antwort eine aktuell zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung verändern kann.
19. M1 führt für diese Blockierregel keinen zusätzlichen Score oder eigenen Human Gate ein.

## E. Arbeitskontrollen und Review-Grenze

20. Mechanische Selbstprüfungen dürfen Pflichtfelder, IDs, Referenzen, Abdeckung und Status prüfen.
21. Semantische Selbstprüfung durch dieselbe KI wird nicht als unabhängiger Review ausgegeben.
22. Inhaltliche Storyrisiken werden im Human Gate und – wo vorgesehen – durch einen bewusst entkoppelten Red-Team-Review bewertet.

## F. Prosa

23. Zu mindestens 3 G2-freigegebenen Szenen wird in bewusst angestoßenen Chat-Runden echte Prosa erzeugt und im Repository gespeichert.
24. Jeder Draft besitzt einen nachvollziehbaren Provenienzrecord nach `BETRIEBSMODELL.md`.
25. Jeder Draft verweist auf die relevanten freigegebenen Upstream-Artefakte bzw. deren feste Git-Referenzen.
26. G3 wird mit einem repräsentativen Prosa-Batch real durchlaufen, bevor der vollständige Prosaumfang als freigegeben gilt.
27. Ein G3-REWORK muss gezielt auf den Prosa-Befund reagieren und darf keine Storyänderung still im Draft einführen.

## G. Source of Truth und Invalidierung

28. Das kanonische Mini-Manuskript enthält ausschließlich freigegebene, nicht `stale`/`invalidated` Prosa-Artefakte.
29. Ein absichtlich veränderter relevanter Upstream-Stand führt dazu, dass das abhängige Downstream-Artefakt nicht still weiter als gültig verwendet werden darf.
30. Eine reine sprachliche Draft-Änderung aktualisiert keinen Story-/Character-State automatisch.
31. Eine beabsichtigte Storyänderung aus der Prosa wird zuerst upstream eingearbeitet und durch die betroffenen Gates zurückgeführt.

## H. Qualität

32. Der bestehende Prosa-Audit läuft auf dem M1-Manuskript.
33. Vor G4 gilt `FAIL = 0`.
34. Verbleibende `REVIEW`-Treffer sind entweder bearbeitet oder mit einer bewussten menschlichen Disposition dokumentiert.
35. M1 behauptet keine literarische Gesamtqualität, für die noch kein validierter Gate/Prüfmechanismus existiert.

## I. Produktion

36. Aus dem G4-freigegebenen Mini-Manuskript wird mindestens ein reproduzierbares finales Test-Produktionsartefakt erzeugt.
37. G5 bezieht sich auf genau diesen finalen Artefaktstand.
38. Das Produktionsformat darf für M1 bewusst minimal sein; es muss aber ein echter abgeleiteter Output sein und darf nicht nur eine Kopie des Manuskripttexts unter anderem Namen sein.

## J. Fehler- und Abbruchfälle

39. Ein absichtlich fehlendes oder inkonsistentes Upstream-Artefakt blockiert einen passenden deterministischen Check.
40. Eine ungelöste **blockierende** Rechercheabhängigkeit verhindert die betroffene Downstream-Entscheidung.
41. Ein fehlender Human Gate blockiert den Übergang in die nächste geschützte Freigabephase.
42. Wird ein Chat-Schritt abgebrochen oder kein gültiges Zielartefakt committed, gilt die Stufe nicht als abgeschlossen.
43. Ein `stale` oder `invalidated` Draft darf nicht in das kanonische Mini-Manuskript gelangen.

## K. Gate-Batching / Skalierungsgrenze

44. M1 darf kleine Gate-Pakete in einer einzigen Review-Vorlage bündeln.
45. Das Framework dokumentiert ausdrücklich, dass große Romane innerhalb derselben fachlichen Freigabephase mehrere Review-Batches benötigen können.
46. M1 behauptet noch keine optimale Batch-Größe für einen 40+-Szenen-Roman.

## L. CI-Grenze

47. CI prüft ausschließlich deterministische Bestandteile: Contracts, Referenzen, Gate-Status, Tests, Audits, Invalidierungslogik und Builds.
48. Kein M1-Erfolgskriterium setzt einen programmatischen LLM-Aufruf, Provider-Adapter, API-Key, Mock-Provider, Tokenzähler oder Kostenbudget voraus.

# Messbarer M1-Abschlussbericht

Der Abschlussbericht muss mindestens enthalten:

```text
Makro→Mikro-Arbeitsfolge eingehalten: PASS / FAIL
Bausteine vollständig: PASS / FAIL
Ereignisse/Sequenzen vollständig: PASS / FAIL
Beats vollständig: PASS / FAIL
G2-freigegebene Szenenkarten: <n> (Minimum 3)
Human Gates G0–G5 vollständig: PASS / FAIL
committete Prosa-Drafts: <n> (Minimum 3)
Drafts mit Provenienz: <n>/<n>
G3 Prosa-Stil real durchlaufen: PASS / FAIL
Invalidierungstest: PASS / FAIL
Prosa-Audit FAIL: <n> (erwartet 0)
Prosa-Audit REVIEW offen ohne Disposition: <n> (erwartet 0 vor G4)
Produktionsartefakt erzeugt: PASS / FAIL
Deterministische CI: PASS / FAIL
bekannte Skalierungsfragen dokumentiert: PASS / FAIL
M1 Gesamt: PASS / FAIL
```

# Bewusste Nicht-Kriterien

Für M1 werden **nicht** verlangt:

- 70.000+ Wörter,
- vollständige Romanqualität,
- optimale Batch-Größe für lange Bücher,
- autonome Storyentwicklung,
- autonome Rewrite-Loops,
- wortgleiche Reproduktion eines Chat-Outputs,
- LLM-Kostenmessung,
- API-/Provider-Infrastruktur,
- generative CI.

# M1-Abnahme

M1 ist nur abgeschlossen, wenn der reale Chat-/GitHub-Prozess einmal vollständig in der neuen Arbeitsweise durchlaufen und die obige Acceptance-Liste gegen die tatsächlich entstandenen Artefakte geprüft wurde.

> **M1 beweist die Arbeitskette und ihre notwendige Entwicklungstiefe im Kleinen – nicht die Skalierbarkeit oder Gesamtqualität eines vollständigen Romans.**
