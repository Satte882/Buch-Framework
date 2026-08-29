import copy
import json
import unittest
from pathlib import Path

from scripts.prosa_audit import audit_text, counts, load_config, parse_paragraphs


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "prosa_rules.yml"
SPLIT_PATH = ROOT / "tests" / "corpus" / "normalfall_split.json"


def findings_for(text, rule_id, config=None):
    cfg = config or load_config(CONFIG_PATH)
    return [finding for finding in audit_text(text, cfg) if finding.rule_id == rule_id]


class ScannerMechanicsTests(unittest.TestCase):
    def test_config_is_dependency_free_yaml_compatible_json(self):
        cfg = load_config(CONFIG_PATH)
        self.assertEqual(cfg["version"], "0.1")
        self.assertEqual(cfg["active"]["prose_profile"], "de_anti_ki_prosa_v1")

    def test_paragraph_parser_tracks_chapter_and_lines(self):
        text = "## 1\n\nErster Absatz.\n\nZweiter Absatz.\n"
        paras = parse_paragraphs(text)
        self.assertEqual(len(paras), 2)
        self.assertEqual(paras[0].chapter, "1")
        self.assertEqual(paras[0].start_line, 3)
        self.assertEqual(paras[1].start_line, 5)

    def test_all_rules_have_valid_scope_and_fail_is_deterministic(self):
        cfg = load_config(CONFIG_PATH)
        allowed = {"core", "prose_profile", "series_profile", "book"}
        for rule_id, rule in cfg["rules"].items():
            self.assertIn(rule["scope"], allowed, rule_id)
            if rule["severity"] == "FAIL":
                self.assertEqual(rule["type"], "deterministic", rule_id)

    def test_production_config_contains_no_normalfall_character_name(self):
        raw = CONFIG_PATH.read_text(encoding="utf-8")
        self.assertNotIn("Daniel", raw)
        self.assertNotIn("Jonas", raw)
        self.assertNotIn("Lena Vogt", raw)

    def test_unreasoned_exception_is_rejected(self):
        cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cfg["rules"]["forbidden_sondern"]["exceptions"] = [{"match": "sondern"}]
        from scripts.prosa_audit import validate_config
        with self.assertRaises(ValueError):
            validate_config(cfg)

    def test_sondern_is_fail_with_word_boundary(self):
        text = "## 1\n\nEr ging nicht links, sondern rechts.\n\nBesonders blieb alles ruhig.\n"
        hits = findings_for(text, "forbidden_sondern")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].severity, "FAIL")

    def test_sondern_exception_is_explicit_and_local(self):
        cfg = copy.deepcopy(load_config(CONFIG_PATH))
        cfg["rules"]["forbidden_sondern"]["exceptions"] = [
            {"match": "Zitat: nicht links, sondern rechts.", "reason": "unveränderbares Originalzitat"}
        ]
        text = (
            "## 1\n\n"
            "Zitat: nicht links, sondern rechts.\n\n"
            "Er ging nicht hoch, sondern runter.\n"
        )
        hits = findings_for(text, "forbidden_sondern", cfg)
        self.assertEqual(len(hits), 1)
        self.assertIn("runter", hits[0].excerpt)

    def test_review_does_not_create_fail(self):
        text = "## 1\n\nNicht ungefähr.\n\nNicht irgendwann.\n\n14.20 Uhr.\n"
        result = audit_text(text, load_config(CONFIG_PATH))
        totals = counts(result)
        self.assertGreaterEqual(totals["REVIEW"], 1)
        self.assertEqual(totals["FAIL"], 0)

    def test_info_does_not_create_fail(self):
        text = (
            "## 1\n\n"
            "Vielleicht war es möglich. Vielleicht war es nur Zufall. "
            "Möglicherweise wusste niemand mehr.\n"
        )
        result = audit_text(text, load_config(CONFIG_PATH))
        totals = counts(result)
        self.assertGreaterEqual(totals["INFO"], 1)
        self.assertEqual(totals["FAIL"], 0)

    def test_noisy_structural_detectors_are_info_after_full_manuscript_check(self):
        cfg = load_config(CONFIG_PATH)
        self.assertEqual(cfg["rules"]["staccato_sequence"]["severity"], "INFO")
        self.assertEqual(cfg["rules"]["dialogue_pingpong"]["severity"], "INFO")
        self.assertEqual(
            cfg["rules"]["staccato_sequence"]["evidence_status"],
            "insufficient_for_review_threshold",
        )
        self.assertEqual(
            cfg["rules"]["dialogue_pingpong"]["evidence_status"],
            "insufficient_for_review_threshold",
        )


class CorpusSplitTests(unittest.TestCase):
    def test_split_is_fixed_and_documents_small_sample_limit(self):
        data = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
        self.assertTrue(data["split_policy"]["no_rebalancing_after_results"])
        self.assertIn("fewer than 8", data["split_policy"]["small_sample_rule"])

    def test_each_family_has_disjoint_dev_and_holdout_ids(self):
        data = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
        for family, split in data["families"].items():
            dev = set(split["development"]["positive"] + split["development"]["control"])
            holdout = set(split["holdout"]["positive"] + split["holdout"]["control"])
            self.assertTrue(dev.isdisjoint(holdout), family)


class RealNormalfallDevelopmentFixtures(unittest.TestCase):
    """Real historical prose snippets on the development side.

    They verify detector mechanics; they do not claim literary precision/recall.
    """

    def test_dialogue_pingpong_positive_28_is_descriptive_info(self):
        text = (
            "## 1\n\n"
            "„Donnerstag, halb vier.“\n\n"
            "„Jeweils wie lange?“\n\n"
            "„Wissen wir nicht.“\n\n"
            "„Video?“\n\n"
            "„Nur vom Donnerstag.“\n"
        )
        hits = findings_for(text, "dialogue_pingpong")
        self.assertTrue(hits)
        self.assertEqual(hits[0].severity, "INFO")

    def test_negation_positive_12_is_reviewed(self):
        text = (
            "## 35\n\n"
            "Kein Kennzeichen.\n\n"
            "Kein Ort.\n\n"
            "Kein Hinweis auf das Fahrzeug.\n"
        )
        hits = findings_for(text, "negation_sequence")
        self.assertTrue(hits)
        self.assertEqual(hits[0].severity, "REVIEW")

    def test_softener_positive_49_is_info_not_review(self):
        text = (
            "## 1\n\n"
            "„Vielleicht. Vielleicht fragt jemand nach dem Grund. "
            "Vielleicht wird aus einer Kontrolle eine zweite. Vielleicht passiert gar nichts.“\n"
        )
        hits = findings_for(text, "softener_density")
        self.assertTrue(hits)
        self.assertTrue(all(hit.severity == "INFO" for hit in hits))

    def test_filter_positive_43_is_only_descriptive(self):
        text = (
            "## 6\n\n"
            "Daniel merkte den Fehler, bevor sie etwas sagte.\n\n"
            "Später merkte er, dass der Satz anders klang.\n"
        )
        hits = findings_for(text, "filter_terms")
        self.assertTrue(hits)
        self.assertEqual(hits[0].severity, "INFO")


class RealNormalfallHoldoutFixtures(unittest.TestCase):
    """Real hold-out snippets.

    Small families remain descriptive. Legitimate controls may be surfaced,
    because INFO/REVIEW mean inspect or observe, never auto-rewrite.
    """

    def test_dialogue_pingpong_holdout_positive_32_is_detected_as_info(self):
        text = (
            "## 7\n\n"
            "„Hat jemand heute einen offenen Zugang gemeldet?“\n\n"
            "„Nein.“\n\n"
            "„Gestern?“\n\n"
            "„Nein.“\n\n"
            "„Fehlermeldung vom Schloss?“\n\n"
            "„Nicht dass ich wüsste.“\n"
        )
        hits = findings_for(text, "dialogue_pingpong")
        self.assertTrue(hits)
        self.assertEqual(hits[0].severity, "INFO")

    def test_dialogue_pingpong_holdout_control_k22_is_info(self):
        text = (
            "## 4\n\n"
            "„Wer hat einen Schlüssel?“\n\n"
            "„Ich. Du. Der Makler für angekündigte Termine. Sonst keiner.“\n\n"
            "„Hausmeister?“\n\n"
            "„Nein.“\n"
        )
        hits = findings_for(text, "dialogue_pingpong")
        self.assertTrue(hits)
        self.assertEqual(hits[0].severity, "INFO")

    def test_negation_holdout_control_k30_is_review_not_fail(self):
        text = (
            "## 18\n\n"
            "Drei Treffer.\n\n"
            "Nicht zwei relevante Treffer.\n\n"
            "Nicht Verbindung bestätigt.\n\n"
            "Drei.\n"
        )
        result = audit_text(text, load_config(CONFIG_PATH))
        self.assertTrue(findings_for(text, "negation_sequence"))
        self.assertEqual(counts(result)["FAIL"], 0)

    def test_staccato_holdout_positive_50_is_descriptive_info(self):
        text = (
            "## Prolog\n\n"
            "Er blieb wieder stehen.\n\n"
            "Keine zweite Kugel.\n\n"
            "Keine Aufforderung.\n\n"
            "Keine Erklärung.\n"
        )
        hits = findings_for(text, "staccato_sequence")
        self.assertTrue(hits)
        self.assertEqual(hits[0].severity, "INFO")


if __name__ == "__main__":
    unittest.main()
