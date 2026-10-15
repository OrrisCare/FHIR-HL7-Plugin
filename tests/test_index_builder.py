import importlib.util
import io
import json
from pathlib import Path
import tarfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_indexes", ROOT / "tools/build_indexes.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def package(version="5.0.0"):
    files = {
        "package.json": {"name": "hl7.fhir.r5.core", "version": version},
        ".index.json": {"files": [{"filename": "StructureDefinition-Patient.json", "resourceType": "StructureDefinition", "id": "Patient", "url": "http://hl7.org/fhir/StructureDefinition/Patient"}]},
        "StructureDefinition-Patient.json": {"resourceType": "StructureDefinition", "id": "Patient", "url": "http://hl7.org/fhir/StructureDefinition/Patient", "kind": "resource", "derivation": "specialization", "abstract": False, "description": "Subject of care"},
    }
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode="w:gz") as archive:
        for name, data in files.items():
            content = json.dumps(data).encode()
            info = tarfile.TarInfo("package/" + name)
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))
    return output.getvalue()


class IndexTests(unittest.TestCase):
    def test_deduplicates_pages_preserves_canonical_and_rejects_external_targets(self):
        toc = b'<a href="patient.html#x">Patient</a><a href="patient.html">Patient</a><a href="https://example.org/x.html">Other</a><a href="../R4/patient.html">Older</a>'
        result = builder.build(toc, package(), b'{"list": []}')
        self.assertEqual(len(result["pages"]), 1)
        self.assertEqual(result["resources"][0]["url"], "https://hl7.org/fhir/R5/patient.html")
        self.assertEqual(result["artifacts"][0]["canonical"], "http://hl7.org/fhir/StructureDefinition/Patient")

    def test_refuses_different_release(self):
        with self.assertRaises(ValueError):
            builder.build(b"", package("6.0.0"), b"{}")


if __name__ == "__main__":
    unittest.main()
