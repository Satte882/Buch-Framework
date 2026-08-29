# Betriebsmodell – ChatGPT + GitHub

## Zweck

Dieses Dokument legt fest, **wie das Buch-Framework tatsächlich betrieben wird**. Es ersetzt die frühere Annahme einer separaten LLM-API-Runtime.

Das Betriebsmodell ist dem unveränderlichen Ziel aus `ZIEL.md` untergeordnet.

## Verbindliches Betriebsmodell

1. **ChatGPT-Chat ist die generative Arbeits- und Orchestrierungsebene.**
   - Storyentwicklung, Figurenarbeit, Rechercheauswertung, Prosa und semantische Reviews werden als bewusst angestoßene Chat-Runden ausgeführt.
   - Es gibt keine separate LLM-API, keinen Provider-Adapter und keine autonome generative Pipeline.
2. **GitHub ist die Source of Truth für Artefakte, Gates und Historie.**
   - Relevante Ergebnisse werden im Repository gespeichert.
   - Ein Ergebnis, das nur im Chat steht und nicht in das vorgesehene Repository-Artefakt übernommen wurde, gilt nicht als gültiger Pipeline-Fortschritt.
3. **Der Mensch entscheidet an den inhaltlich irreversiblen Gates.**
   - ChatGPT darf Gate-Unterlagen vorbereiten.
   - ChatGPT darf kein menschliches `APPROVE` simulieren oder selbst setzen.
4. **CI bleibt dauerhaft deterministisch.**
   - GitHub Actions darf Parser, Referenzen, Gate-Status, Invalidierung, Builds und Qualitätsregeln prüfen.
   - Generative Story-, Prosa- oder Review-Schritte sind kein CI-Ziel.

## Nicht benötigte Infrastruktur

Für dieses Betriebsmodell werden ausdrücklich nicht gebaut:

- API-Key-/Secret-Management für Modellprovider,
- Provider-Abstraktion,
- Token- oder Kostenbudget-Tracking,
- Retry-/Rate-Limit-/Timeout-Infrastruktur für Modellaufrufe,
- Mock-Provider,
- generative GitHub-Actions-Jobs,
- eigene Agenten-/Queue-/Service-Orchestrierung.

Sollte sich das reale Betriebsmodell später ändern, ist dafür eine bewusste Architekturentscheidung notwendig. Bis dahin sind solche Komponenten Scope Creep.

# Chat-Provenienzstandard

## Ziel

Ein chat-generiertes oder im Chat wesentlich überarbeitetes Artefakt muss nachvollziehbar auf die **freigegebenen Upstream-Artefakte** zurückgeführt werden können.

Reproduzierbarkeit bedeutet hier nicht wortgleiche Neuerzeugung. Nachvollziehbar sein müssen Herkunft, Inputs, Gate-Bezug und Zielartefakt.

## Minimaler Provenienzrecord

Für relevante generative Artefakte oder Batches wird ein Record mit mindestens folgenden Feldern gespeichert:

```yaml
artifact: <Pfad zum erzeugten/geänderten Artefakt>
generated_via: chatgpt_chat
action: generated | revised
date: YYYY-MM-DD
purpose: <kurzer Zweck>
upstream:
  - path: <Repository-Pfad oder externer kanonischer Pfad>
    ref: <Git-Commit, Blob-SHA oder andere feste Version>
gate_basis: <z. B. G3 APPROVE oder historisch freigegebener kanonischer Stand>
status: draft | accepted | stale | invalidated
notes: <bewusste Abweichungen/offene Punkte oder none>
```

## Was bewusst nicht gespeichert wird

Nicht verfügbare Chat-Metadaten werden nicht erfunden. Insbesondere sind nicht verpflichtend:

- Tokenverbrauch,
- Temperatur,
- Seed,
- interne Modelllauf-ID,
- Providerkosten,
- nicht sichtbare Systemparameter.

## Speicherform

Für v0.x gilt KISS:

- Bei einzelnen Drafts darf der Provenienzrecord als eigene Markdown-Datei unter `provenance/` liegen.
- Bei späteren größeren Batches darf ein gemeinsames Manifest verwendet werden.
- Es wird keine separate Datenbank eingeführt.

Die konkreten Upstream-Referenzen und Invalidierungsregeln richten sich nach `SOURCE_OF_TRUTH.md`.

## Gültigkeitsregel

Ein generatives Ergebnis gilt für die Framework-Pipeline erst dann als vorhanden, wenn:

1. das Zielartefakt im Repository gespeichert ist,
2. seine relevanten Upstream-Referenzen nachvollziehbar sind,
3. kein erforderlicher Human Gate fehlt,
4. das Artefakt nicht `stale` oder `invalidated` ist.

## Abgrenzung Chat vs. CI

| Aufgabe | ChatGPT-Chat | Deterministische Tools / CI |
|---|---:|---:|
| Plot entwickeln | ja | nein |
| Figuren entwickeln | ja | nein |
| Prosa erzeugen | ja | nein |
| semantisch lektorieren | ja | nein |
| Human Gate entscheiden | nein | nein |
| Pflichtfelder prüfen | optional | ja |
| Referenzen/Hashes prüfen | optional | ja |
| Prosa-Audit | optional | ja |
| Build/Format-QA | optional | ja |

## Leitregel

> **ChatGPT erzeugt und analysiert. GitHub hält den gültigen Stand. Der Mensch entscheidet. CI prüft nur das Deterministische.**
