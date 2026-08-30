# FEHLALARM – M1-Testfall

status: frozen_regression_fixture
m1_result: PASS
frozen_on: 2026-08-30

## Zweck

`FEHLALARM` ist **kein Buchprojekt** und kein Entwurf für einen späteren Roman. Der Ordner existiert ausschließlich, um den vollständigen M1-Pfad des Frameworks einmal real im Chat-/GitHub-Betriebsmodell durchzuspielen.

## Lifecycle-Entscheidung

Der Testfall wird nach erfolgreichem M1 **nicht gelöscht und nicht in ein Buchprojekt überführt**.

Er bleibt an diesem Pfad als **eingefrorener Regression-/Referenzfall** erhalten:

`m1/e2e_minibook/`

Warum er erhalten bleibt:

- Der Fall enthält einmal real durchlaufene Artefakte und Human Gates von G0 bis G5.
- Künftige Änderungen an Contracts, Checkern, Invalidierungslogik, Prosa-Audit oder Produktionsschritten können gegen einen bekannten vollständigen Fall geprüft werden.
- Die Git-Historie und Provenienzreferenzen bleiben verständlich; ein späteres Verschieben würde unnötig Pfade und Referenzen brechen.

## Statusmodell

Während M1 lief:

`status: active_m1_fixture`

Nach `M1 Gesamt: PASS`:

`status: frozen_regression_fixture`

Der M1-Abschlussbericht dokumentiert den PASS gegen `M1_ACCEPTANCE.md`.

## Was Regression hier bedeutet

FEHLALARM ist vor allem ein **statischer Integrations-/Regression-Fall**. Er darf für deterministische Prüfungen wiederverwendet werden, beispielsweise:

- Pipeline-Contracts,
- Gate- und Referenzprüfungen,
- Scene Readiness,
- Upstream-Invalidierung,
- Prosa-Audit,
- Manuskriptzusammenbau,
- Produktionsbuilds.

Die generative Prosa wird nicht in CI neu erzeugt. Ein künftiger Test vergleicht deshalb nicht, ob ChatGPT denselben Text erneut schreibt.

## Änderungsregel nach dem Freeze

Nach M1 wird der Fall nicht beiläufig weiterentwickelt.

Eine Änderung ist nur zulässig, wenn:

1. sich ein Framework-Contract bewusst ändert und der Fixture angepasst werden muss,
2. ein echter Framework-Bug durch einen neuen Regressionstest abgedeckt wird,
3. eine fehlerhafte Referenz oder ein sachlicher Fehler im Fixture korrigiert werden muss.

Solche Änderungen müssen als **Fixture-/Framework-Anpassung** erkennbar committed werden. Sie sind keine Weiterentwicklung der Geschichte.

## Abgrenzung

- kein veröffentlichungsfähiger Roman,
- kein `NORMALFALL`-Ableger,
- kein `ABWEICHUNG`-Test,
- kein Buch 3,
- keine Stilreferenz für künftige Bücher,
- kein Trainingskorpus für Storyinhalte.

> **FEHLALARM bleibt als gefrorener Nachweis dafür erhalten, dass die Framework-Kette einmal vollständig funktioniert hat.**
