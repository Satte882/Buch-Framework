# RESEARCH_REGISTER

register_status: ready

Dieses Register enthält nur Recherchefragen, die für Plot, Figurenhandlung, Plausibilität oder konkrete spätere Szenenentscheidungen relevant sind. Recherche ist im v0.2-Workflow ein Querschnittsartefakt und besitzt keinen eigenen Human Gate.

| ID | Frage | Betroffene Ebene / Artefakte | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung | blocking_now |
|---|---|---|---|---|---|---|---|
| R-01 | Welche journalistisch/presserechtlich plausible Grenze gilt im deutschen Kontext für Sorgfalt, Verdachtsdarstellung, Stellungnahme und Quellenschutz? | STORY_PACKAGE.md; STORY_BLOCKS.md; EVENTS.md; später Beats/Szenen/Prosa | high | resolved | Deutscher Presserat, Pressekodex Ziffer 2 und Ziffer 5; BVerfG zur Verdachtsberichterstattung, u. a. Beschluss/Pressemitteilung 2020 zur Bedeutung von öffentlichem Interesse, Stellungnahmemöglichkeit und nicht-vorverurteilender Darstellung; § 53 StPO zum journalistischen Zeugnisverweigerungsrecht | Für SPERRFRIST wird keine vereinfachte Regel „unbewiesen = nicht publizierbar“ angenommen. Nora/Mira müssen belastbare Tatsachen von offenem Verdacht trennen, dem betroffenen Unternehmen vor Veröffentlichung Gelegenheit zur konkreten Stellungnahme geben und vereinbarte Quellenvertraulichkeit grundsätzlich wahren. Eine persönliche Wissens-/Verantwortungszuschreibung darf nicht nur aus dem technischen Befund abgeleitet werden. | no |
| R-02 | Welcher technische System-/Releasekontext ist für eine fiktive sicherheitsrelevante Kommunikationsplattform plausibel, ohne reale Bundeswarnsysteme falsch darzustellen? | STORY_PACKAGE.md; STORY_BLOCKS.md; EVENTS.md; später Beats/Szenen | high | resolved | BBK: MoWaS als hochverfügbares, mehrkanaliges Warn- und Kommunikationssystem; BBK: Weiterentwicklung über Software-Releases; BBK 25.11.2025: neue Cell-Broadcast-Funktion nach intensiver Testphase mit Mobilfunknetzbetreibern | Das fiktive Unternehmen liefert **nicht** MoWaS oder Cell Broadcast selbst. Es liefert eine vendorseitige, redundante Kommunikations-/Verteilplattform für kommunale Krisenorganisationen mit eigenen Release-Candidates, Failover-/Auslieferungstests und Rolloutfreigaben. Der Plot darf Testbefunde, Build-/Release-Versionen, Verteiler und geplante kommunale Rollouts verwenden, behauptet aber keine konkrete amtliche Bundeswarnprozedur. | no |

## Reale Anwendung der Blockierregel

### R-01

**Vor der Recherche:** `blocking_now: yes`.

Begründung: Die G1-Architektur musste entscheiden, ob Mira plausibel eine engere Veröffentlichung trotz verbleibender Unsicherheit zulassen kann und welche Rolle Stellungnahme/Quellenschutz spielen. Eine falsche Annahme hätte den gesamten Konflikt `Tempo vs. Belegbarkeit` verzerrt.

**Nach Rechercheentscheidung:** `blocking_now: no`.

Die Architektur bleibt bewusst allgemein und behauptet keine individuelle Rechtsberatung oder konkrete Prozessprognose. Für spätere Prosa dürfen keine detaillierten juristischen Aussagen erfunden werden, die über diese Leitplanken hinausgehen.

### R-02

**Vor der Recherche:** `blocking_now: yes`.

Begründung: Die Ausgangsidee „Notfall-Kommunikationssystem“ hätte leicht so konkretisiert werden können, dass ein privater Anbieter unrealistisch als Betreiber/Entscheider amtlicher Warninfrastruktur dargestellt wird. Das hätte Events und spätere Szenenlogik verändert.

**Nach Rechercheentscheidung:** `blocking_now: no`.

Durch die Abgrenzung auf eine fiktive vendorseitige Plattform kann die Story reale Konzepte wie Redundanz, Releases und Testphasen nutzen, ohne konkrete MoWaS-/Cell-Broadcast-Prozesse zu fiktionalisieren.

## Primär-/offizielle Quellen

### R-01

- Deutscher Presserat – Pressekodex: https://www.presserat.de/pressekodex.html
  - Ziffer 2: Recherche/Sorgfalt; unbestätigte Meldungen, Gerüchte und Vermutungen als solche kenntlich machen.
  - Ziffer 5 / Richtlinie 5.1: Berufsgeheimnis und grundsätzlich zu wahrende vereinbarte Vertraulichkeit von Informantinnen und Informanten.
- Bundesverfassungsgericht – Verdachtsberichterstattung / Online-Pressearchive, Pressemitteilung 65/2020: https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/DE/2020/bvg20-065.html
  - hohe Anforderungen bei Verdachtsberichterstattung; öffentliches Interesse, Stellungnahmemöglichkeit und nicht-vorverurteilende Darstellung als relevante Leitplanken.
- Strafprozessordnung § 53: https://www.gesetze-im-internet.de/stpo/__53.html
  - Zeugnisverweigerungsrecht für berufsmäßig an Presse/Informationsmedien Mitwirkende bezüglich Informanten und redaktioneller Informationen innerhalb der gesetzlichen Grenzen.

### R-02

- BBK – MoWaS: https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html
  - hochverfügbares, gehärtetes und mehrkanaliges Warn-/Kommunikationssystem.
- BBK – ISF: Modulares Warnsystem: https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/ISF-Projekt/ISF-MoWas/isf-mowas.html
  - Weiterentwicklung unter anderem über umfassende Software-Releases.
- BBK – Cell Broadcast: Entwarnung jetzt möglich, 25.11.2025: https://www.bbk.bund.de/SharedDocs/Pressemitteilungen/DE/2025/11/pm-25-cell-broadcast-entwarnung.html
  - neue Funktion nach intensiver Testphase mit Mobilfunknetzbetreibern; dient nur als Plausibilitätsbeleg für Test-/Release-Logik, nicht als Storysystem.

## Offene Recherchefragen

- none für G1.

Neue Detailfragen dürfen auf Beat-/Szenenebene entstehen, wenn eine konkrete Entscheidung davon abhängt. Sie werden dann neu im Register erfasst und nach derselben Blockierregel behandelt.

## Gate-Bezug

- G1 prüft, dass die Story-Architektur keine offene blockierende Rechercheabhängigkeit enthält.
- G2 prüft erneut, dass keine Beat-/Szenenentscheidung eine noch offene `blocking_now: yes`-Frage voraussetzt.
