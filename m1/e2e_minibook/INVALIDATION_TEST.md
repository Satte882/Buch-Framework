# M1 Invalidierungstest – PASS

status: PASS
date: 2026-08-30
scope: isolierter deterministischer Fixture-Test; keine Änderung am freigegebenen FEHLALARM-Story-/Manuskriptstand

## Ziel

Nachweisen, dass ein Downstream-Artefakt mit festen Git-Blob-Referenzen nicht still weiter als gültig verwendet werden kann, wenn sich ein relevanter Upstream-Stand ändert.

Der Test wird bewusst isoliert ausgeführt. Ein künstlicher Wechsel eines echten G2-/G4-Upstream-Artefakts im kanonischen FEHLALARM-Pfad würde die realen Human Gates unnötig invalidieren und wäre kein sinnvoller M1-Testaufbau.

## Implementierung

- Guard: `scripts/provenance_check.py` — blob `2e71119d1c083fcf9b58f54ed342bd41fe8d4714`
- Test: `tests/test_provenance_check.py` — blob `7344b0bf71b0ec9b7f1d6ef5c1efa00ac91173db`

Der Guard berechnet für referenzierte lokale Dateien den echten Git-Blob-SHA (`sha1("blob <len>\0" + bytes)`) und vergleicht ihn mit dem im Provenienzrecord festgehaltenen SHA.

## Geprüfter Fehlerfall

Der Unit-Test führt real nacheinander aus:

1. Upstream-Datei `alpha`, Provenienz `status: accepted`, Referenz stimmt → `OK`.
2. Upstream-Datei wird absichtlich auf `beta` verändert, Provenienz bleibt unverändert `accepted` → `BLOCK` wegen Blob-Mismatch.
3. Downstream-Provenienz wird sichtbar auf `status: stale` gesetzt → derselbe Mismatch wird als `STALE_OK` akzeptiert.

Zusätzlich wird geprüft, dass ein bereits als `stale` deklarierter Record durch den Checker niemals automatisch wieder auf `accepted` hochgestuft wird.

## CI-Nachweis

- Framework Validation Run #30 / ID `33306761282`: **success**; enthält beide Invalidierungstests.
- Framework Validation Run #32 / ID `33306864034`: **success**; bestätigt den Invalidierungs-Guard gemeinsam mit dem finalen Produktions-Rebuild-Test und dem übrigen Framework-Testbestand.

## Ergebnis

`Invalidierungstest: PASS`

Die zentrale M1-Regel ist damit deterministisch nachgewiesen:

> Ändert sich ein referenzierter relevanter Upstream-Blob, blockiert ein weiterhin als `accepted` oder `draft` geführtes Downstream-Artefakt. Weiterverwendung ist erst nach sichtbarer Invalidierung (`stale`/`invalidated`) und anschließender erneuter Ableitung/Freigabe zulässig.

Der Guard erkennt Hash-Drift; er entscheidet ausdrücklich nicht selbst, ob eine Änderung semantisch relevant ist und verändert keine Human-Gates.