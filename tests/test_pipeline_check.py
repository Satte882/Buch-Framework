from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import pipeline_check  # noqa: E402
import scene_readiness  # noqa: E402

PIPELINE_CONFIG = pipeline_check.load_config(ROOT / "config" / "pipeline_contract.yml")
SCENE_CONFIG = scene_readiness.load_config(ROOT / "config" / "scene_readiness.yml")


BOOK_IDEA = """# BOOK_IDEA
working_title: Testroman
genre: Psychothriller
core_conflict: Sicherheit gegen legitime Selbstbestimmung
central_question: Wann wird Schutz selbst zum Kontrollproblem?
mechanism: Ein Schutzsystem verschiebt schrittweise Entscheidungsmacht.
promise_to_reader: Schneller Thriller mit moralischer Reibung.
non_goals: Kein allwissender Bösewicht und keine Technikmagie.
irreversible_decisions_open: no
"""

STORY_PACKAGE = """# STORY_PACKAGE
working_title: Testroman
version: v0.2
premise_summary: Ein wirksames Schutzsystem verändert nach Erfolgen die legitime Entscheidungsmacht.
core_conflict_summary: Sicherheit und Selbstbestimmung sind gleichzeitig legitim.
central_question: Wann wird Schutz selbst zum Kontrollproblem?
mechanism_summary: Jeder Erfolg senkt die Schwelle für den nächsten Eingriff.
protagonist_arc_summary: Vorsicht → Akzeptanz → Grenzverschiebung → Verantwortung.
plot_architecture_summary: Zwei Bausteine tragen Eskalation und Reversal.
reversal_summary: Die Erfolge bleiben real, ihre institutionelle Bedeutung kippt.
information_architecture_summary: Leser akzeptiert Nutzen zuerst und erkennt den Preis verzögert.
character_functions_summary: Protagonist und Gegenfigur besitzen eigene Ziele.
story_decisions_open: no
"""

STORY_BLOCKS = """# STORY_BLOCKS
version: v0.2
story_package_version: v0.2
blocks_status: ready

| block_id | Funktion im Gesamtbogen | Ausgangslage | zentrale Verschiebung / Druck | relevante Entscheidung | Konsequenz | Leserfunktion | Figurenkern | Rechercheabhängigkeiten |
|---|---|---|---|---|---|---|---|---|
| B01 | Setzt die Ausgangsgrenze | Verfahren gilt als tragfähig | Zeitdruck steigt | Alex bleibt beim regulären Weg | Spur bleibt offen | Grenze wird verständlich | Alex gegen Bea | R-001 |
| B02 | Kippt die Grenze | Der Druck ist höher | Ausnahme wird plausibel | Alex akzeptiert den Eingriff | Handlungsspielraum schrumpft | Preis wird sichtbar | Alex und Bea driften auseinander | none |
"""

EVENTS = """# EVENTS
version: v0.2
story_blocks_version: v0.2
events_status: ready

| event_id | block_id | sequence_id | Ereignis | Ursache | unmittelbare Folge | Informationsverschiebung | Figurenwirkung | relevante Entscheidung | research_refs |
|---|---|---|---|---|---|---|---|---|---|
| E001 | B01 | SQ01 | Ein Hinweis trifft ein | Externe Meldung | Prüfung startet | Hinweis ist plausibel | Alex wird unter Druck gesetzt | Regulären Weg nutzen | R-001 |
| E002 | B01 | SQ01 | Die Frist läuft aus | Prüfung dauert | Spur droht zu versanden | Zeit wird zum Risiko | Bea fordert Abkürzung | Alex lehnt ab | none |
| E003 | B02 | none | Neuer Schaden tritt ein | Verzögerung hatte Kosten | Ausnahme wird angeboten | Nutzen der Ausnahme wird sichtbar | Alex zweifelt | Alex akzeptiert begrenzten Eingriff | R-002 |
"""

BEATS = """# BEATS
version: v0.2
events_version: v0.2
beats_status: ready

| beat_id | event_id | planned_scene_id | POV | Auslöser / beobachtbarer Schritt | Reaktion / Entscheidung | Druckverschiebung | Informationsverschiebung | Konsequenz | character_state_impact | research_refs |
|---|---|---|---|---|---|---|---|---|---|---|
| BT001 | E001 | S1 | Alex | Meldung erscheint | Alex prüft zuerst regulär | Druck beginnt | Hinweis wird konkret | Zeit vergeht | Alex bleibt regelorientiert | R-001 |
| BT002 | E002 | S1 | Alex | Timer wird kritisch | Alex lehnt Abkürzung ab | Druck steigt | Risiko der Verzögerung wird sichtbar | Spur bleibt offen | Vertrauen zu Bea sinkt leicht | none |
| BT003 | E003 | S2 | Alex | Schaden wird bestätigt | Alex akzeptiert begrenzte Ausnahme | Druck kippt | Nutzen wird real | Zugriff wird erweitert | Alex verschiebt seine Grenze | R-002 |
| BT004 | E003 | S3 | Bea | Erweiterung zeigt Nebenfolge | Bea widerspricht | Druck richtet sich gegen Alex | Preis wird sichtbar | Beziehung wird belastet | Bea entzieht Vertrauen | none |
"""

CHARACTERS = """# CHARACTERS
version: v0.2
story_package_version: v0.2
roster_summary: Alex trägt die Entscheidung; Bea vertritt eine gleichwertige Gegenlogik.
relationship_baseline_summary: Fachliches Vertrauen bei unterschiedlicher Risikogewichtung.
open_character_decisions: yes
"""

RESEARCH = """# RESEARCH_REGISTER
register_status: ready

| ID | Frage | Betroffene Ebene / Artefakte | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung | blocking_now |
|---|---|---|---|---|---|---|---|
| R-001 | Wie funktioniert die reale Freigabekette? | B01; E001; S1 | high | resolved | Fachquelle A | Zweistufige Freigabe | no |
| R-002 | Welche Oberfläche zeigt das System? | E003; S2 | low | open |  |  | no |
"""

CHARACTER_STATE_TEMPLATE = """# CHARACTER_STATE
scene_id: {scene_id}
character: {character}
status: ready
knows_before: Ausgangswissen ist festgelegt.
believes_before: Ausgangshaltung ist festgelegt.
wants_now: Ein konkretes Ziel verfolgen.
fears_or_avoids: Eine konkrete Fehlentscheidung vermeiden.
relationship_state: Ausgangsbeziehung ist festgelegt.
must_not_know_yet: Späteres Wissen bleibt geschützt.
knows_after: Neues Wissen ist festgelegt.
believes_after: Neue Einschätzung ist festgelegt.
relationship_change: Veränderung ist festgelegt.
decision_or_commitment: Entscheidung ist festgelegt.
"""


def scene(scene_id: str, beat_refs: str, state_ref: str, research_refs: str) -> str:
    return f"""# SCENE_PLAN
scene_id: {scene_id}
title: Szene {scene_id}
story_function: Eine definierte Storyfunktion tragen.
pov: Alex
location_time: Lagebüro am Dienstagmorgen.
characters_present: Alex; Bea
goal: Einen konkreten nächsten Schritt entscheiden.
conflict: Eine plausible Gegenoption erzeugt Druck.
decision: Alex trifft eine festgelegte Entscheidung.
consequence: Der Handlungsraum verändert sich sichtbar.
reader_before: Der Leser kennt die Ausgangslage.
reader_after: Der Leser erkennt die Verschiebung.
must_not_reveal: none - keine zusätzliche Geheimnisgrenze in diesem Test.
character_state_status: ready
research_status: ready
story_decisions_open: no
narrative_weight: medium
experience_status: pending_human_review
pressure_progression: Druck steigt über konkrete Frist und Gegenoption.
observable_actions: Alex prüft, fragt nach und entscheidet.
alternatives_in_scene: Bea vertritt eine reale Gegenoption.
consequence_carrier: Eine protokollierte Folge macht die Entscheidung sichtbar.
space_or_procedure_anchors: Raum, Zugriffspfad und Ablauf sind festgelegt.
relationship_or_psychology_carrier: Der Widerspruch verändert das Vertrauen sichtbar.
beat_refs: {beat_refs}
character_state_refs: {state_ref}
research_refs: {research_refs}
"""


def gate(gate_id: str, artifacts: str, next_step: str) -> str:
    return f"""# GATE_RECORD
gate_id: {gate_id}
artifacts: {artifacts}
decision: APPROVE
decided_by: human
date: 2026-08-30
open_blockers: no
next_step: {next_step}
"""


def write_valid_project(root: Path) -> None:
    (root / "gates").mkdir(parents=True)
    (root / "scenes").mkdir(parents=True)
    (root / "character_states").mkdir(parents=True)
    for name, text in {
        "BOOK_IDEA.md": BOOK_IDEA,
        "STORY_PACKAGE.md": STORY_PACKAGE,
        "STORY_BLOCKS.md": STORY_BLOCKS,
        "EVENTS.md": EVENTS,
        "BEATS.md": BEATS,
        "CHARACTERS.md": CHARACTERS,
        "RESEARCH_REGISTER.md": RESEARCH,
    }.items():
        (root / name).write_text(text, encoding="utf-8")

    state_refs = {}
    for scene_id, character in [("S1", "Alex"), ("S2", "Alex"), ("S3", "Bea")]:
        rel = f"character_states/{scene_id}_{character}.md"
        state_refs[scene_id] = rel
        (root / rel).write_text(
            CHARACTER_STATE_TEMPLATE.format(scene_id=scene_id, character=character),
            encoding="utf-8",
        )

    (root / "scenes" / "legacy.md").write_text(
        "# SCENE_PLAN\nscene_id: OLD\nstory_decisions_open: yes\n",
        encoding="utf-8",
    )
    (root / "scenes" / "S1.md").write_text(
        scene("S1", "BT001; BT002", state_refs["S1"], "R-001"), encoding="utf-8"
    )
    (root / "scenes" / "S2.md").write_text(
        scene("S2", "BT003", state_refs["S2"], "R-002"), encoding="utf-8"
    )
    (root / "scenes" / "S3.md").write_text(
        scene("S3", "BT004", state_refs["S3"], "none - keine Recherche nötig"), encoding="utf-8"
    )

    (root / "gates" / "G0.md").write_text(
        gate("G0", "BOOK_IDEA.md", "Story-Architektur entwickeln"), encoding="utf-8"
    )
    (root / "gates" / "G1.md").write_text(
        gate(
            "G1",
            "STORY_PACKAGE.md; STORY_BLOCKS.md; EVENTS.md; CHARACTERS.md; RESEARCH_REGISTER.md",
            "Beats und Szenenkarten entwickeln",
        ),
        encoding="utf-8",
    )
    g2_artifacts = (
        "BEATS.md; RESEARCH_REGISTER.md; scenes/S1.md; scenes/S2.md; scenes/S3.md; "
        "character_states/S1_Alex.md; character_states/S2_Alex.md; character_states/S3_Bea.md"
    )
    (root / "gates" / "G2.md").write_text(
        gate("G2", g2_artifacts, "Repräsentativen Prosa-Batch erzeugen"), encoding="utf-8"
    )


class PipelineV02Tests(unittest.TestCase):
    def test_valid_macro_to_micro_project_is_ready_for_prose(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "READY_FOR_PROSE")
            self.assertEqual(result.issues, [])
            self.assertEqual(result.active_scenes, ["scenes/S1.md", "scenes/S2.md", "scenes/S3.md"])
            self.assertNotEqual(result.status, "APPROVE")

    def test_historical_scene_not_referenced_by_beats_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertFalse(any("OLD" in issue for issue in result.issues))

    def test_every_block_requires_event_coverage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            events = (root / "EVENTS.md").read_text(encoding="utf-8")
            events = events.replace(
                "| E003 | B02 | none | Neuer Schaden tritt ein | Verzögerung hatte Kosten | Ausnahme wird angeboten | Nutzen der Ausnahme wird sichtbar | Alex zweifelt | Alex akzeptiert begrenzten Eingriff | R-002 |\n",
                "",
            )
            (root / "EVENTS.md").write_text(events, encoding="utf-8")
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("B02 has no event coverage" in issue for issue in result.issues))

    def test_every_event_requires_beat_coverage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            beats = (root / "BEATS.md").read_text(encoding="utf-8")
            beats = "\n".join(
                line for line in beats.splitlines()
                if not line.startswith("| BT003 |") and not line.startswith("| BT004 |")
            ) + "\n"
            (root / "BEATS.md").write_text(beats, encoding="utf-8")
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("E003 has no beat coverage" in issue for issue in result.issues))

    def test_scene_beat_refs_must_exactly_cover_planned_beats(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            text = (root / "scenes" / "S1.md").read_text(encoding="utf-8")
            (root / "scenes" / "S1.md").write_text(
                text.replace("beat_refs: BT001; BT002", "beat_refs: BT001"),
                encoding="utf-8",
            )
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("beat_refs missing planned beats" in issue for issue in result.issues))

    def test_missing_planned_scene_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            (root / "scenes" / "S2.md").unlink()
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("planned scene S2 has no matching scene plan" in issue for issue in result.issues))

    def test_open_nonblocking_research_does_not_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "READY_FOR_PROSE")
            self.assertFalse(any("R-002 is still open" in issue for issue in result.issues))

    def test_open_blocking_research_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            text = (root / "RESEARCH_REGISTER.md").read_text(encoding="utf-8")
            (root / "RESEARCH_REGISTER.md").write_text(
                text.replace("| R-002 | Welche Oberfläche zeigt das System? | E003; S2 | low | open |  |  | no |",
                             "| R-002 | Welche Oberfläche zeigt das System? | E003; S2 | low | open |  |  | yes |"),
                encoding="utf-8",
            )
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("blocking research R-002 is still open" in issue for issue in result.issues))

    def test_missing_human_g1_blocks_even_if_g2_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            (root / "gates" / "G1.md").unlink()
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("G1: missing human gate record" in issue for issue in result.issues))

    def test_missing_g1_does_not_report_future_g2_noise(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            (root / "gates" / "G1.md").unlink()
            (root / "BEATS.md").unlink()
            (root / "gates" / "G2.md").unlink()
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("G1: missing human gate record" in item for item in result.issues))
            self.assertFalse(any("BEATS.md" in item or "G2:" in item for item in result.issues))

    def test_research_row_requires_blocking_now_column(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            text = (root / "RESEARCH_REGISTER.md").read_text(encoding="utf-8")
            text = text.replace(
                "| R-002 | Welche Oberfläche zeigt das System? | E003; S2 | low | open |  |  | no |",
                "| R-002 | Welche Oberfläche zeigt das System? | E003; S2 | low | open |  |  |",
            )
            (root / "RESEARCH_REGISTER.md").write_text(text, encoding="utf-8")
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("must include blocking_now column" in item for item in result.issues))

    def test_g1_record_must_cover_bundled_story_architecture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            path = root / "gates" / "G1.md"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("STORY_BLOCKS.md; ", ""), encoding="utf-8")
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("G1: artifacts must include STORY_BLOCKS.md" in issue for issue in result.issues))

    def test_g2_record_must_cover_active_scenes_and_character_states(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            path = root / "gates" / "G2.md"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("scenes/S3.md; ", ""), encoding="utf-8")
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("G2: artifacts must include scenes/S3.md" in issue for issue in result.issues))

    def test_character_state_ref_must_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            (root / "character_states" / "S2_Alex.md").unlink()
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("character state missing" in issue for issue in result.issues))


if __name__ == "__main__":
    unittest.main()
