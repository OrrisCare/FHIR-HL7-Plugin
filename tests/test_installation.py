import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('install_skills', ROOT / 'tools/install_skills.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dest = Path(self.temp.name) / 'skills'

    def test_dry_run_does_not_write(self):
        result = installer.install(self.dest, dry_run=True)
        self.assertEqual(result['new'], 16)
        self.assertFalse(self.dest.exists())

    def test_full_install_preserves_unrelated_files_and_is_idempotent(self):
        self.dest.mkdir()
        unrelated = self.dest / 'my-existing-skill.txt'
        unrelated.write_text('Keep me')
        self.assertEqual(installer.install(self.dest)['new'], 16)
        self.assertEqual(installer.install(self.dest)['unchanged'], 16)
        self.assertEqual(unrelated.read_text(), 'Keep me')
        self.assertTrue((self.dest / 'fhir-clinical/references/domains.md').is_file())
        self.assertTrue((self.dest / 'fhir-standards/references/indexes/artifacts.json').is_file())

    def test_conflict_is_detected_before_any_skill_is_copied(self):
        conflict = self.dest / 'fhir-workflow'
        conflict.mkdir(parents=True)
        (conflict / 'SKILL.md').write_text('Local work')
        with self.assertRaises(ValueError):
            installer.install(self.dest)
        self.assertEqual([p.name for p in self.dest.iterdir()], ['fhir-workflow'])
        self.assertEqual((conflict / 'SKILL.md').read_text(), 'Local work')

    def test_suite_is_self_contained_and_lookup_runs_after_copy(self):
        result = installer.install(self.dest, bundle=True)
        self.assertEqual(result['skills'], 1)
        self.assertEqual(len(list(self.dest.rglob('SKILL.md'))), 1)
        suite = self.dest / 'fhir-suite'
        self.assertEqual(len(list(suite.rglob('GUIDE.md'))), 16)
        script = suite / 'references/workflows/fhir-standards/scripts/lookup.py'
        output = subprocess.check_output([sys.executable, str(script), 'Observation', '--kind', 'resources', '--limit', '1'], cwd=self.temp.name, text=True)
        self.assertEqual(json.loads(output)['results'][0]['id'], 'Observation')

    def test_partial_io_failure_rolls_back_new_skill_directories(self):
        self.dest.mkdir()
        unrelated = self.dest / 'keep.txt'
        unrelated.write_text('Keep')
        with patch.object(installer.shutil, 'copytree', side_effect=OSError('Disk failure')):
            with self.assertRaises(OSError):
                installer.install(self.dest)
        self.assertEqual([p.name for p in self.dest.iterdir()], ['keep.txt'])

    def test_symlink_target_is_not_overwritten(self):
        actual = Path(self.temp.name) / 'existing'
        actual.mkdir()
        self.dest.mkdir()
        try:
            (self.dest / 'fhir-workflow').symlink_to(actual, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Host cannot create symlinks')
        with self.assertRaises(ValueError):
            installer.install(self.dest)
        self.assertEqual(list(actual.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
