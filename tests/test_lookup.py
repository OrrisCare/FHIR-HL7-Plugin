import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins/fhir/skills/fhir-standards/scripts/lookup.py"
spec = importlib.util.spec_from_file_location("lookup", SCRIPT)
lookup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup)


class LookupTests(unittest.TestCase):
    def invoke(self, *args):
        # Run outside the repository to prove paths are script-relative.
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT.parent, capture_output=True, text=True)

    def test_exact_resource_ranked_before_mentions(self):
        result = json.loads(self.invoke("Observation", "--kind", "resources", "--limit", "1").stdout)
        self.assertEqual(result["results"][0]["id"], "Observation")
        self.assertEqual(result["results"][0]["canonical"], "http://hl7.org/fhir/StructureDefinition/Observation")

    def test_artifact_search_resolves_real_parameter(self):
        result = json.loads(self.invoke("Observation-subject", "--kind", "artifacts", "--limit", "50").stdout)
        self.assertTrue(any(r["id"] == "Observation-subject" and r["resourceType"] == "SearchParameter" for r in result["results"]))

    def test_no_results_and_empty_query(self):
        result = json.loads(self.invoke("no-such-resource-zxy123", "--kind", "resources").stdout)
        self.assertEqual(result["matches"], 0)
        self.assertEqual(lookup.search([{"id": "Patient"}], "---"), [])

    def test_invalid_limit_rejected(self):
        self.assertNotEqual(self.invoke("Patient", "--limit", "0").returncode, 0)

    def test_all_tokens_required_case_insensitive(self):
        records = [{"id": "A", "description": "Patient reference"}, {"id": "B", "description": "Patient token"}]
        self.assertEqual([r["id"] for r in lookup.search(records, "PATIENT reference")], ["A"])


if __name__ == "__main__":
    unittest.main()
