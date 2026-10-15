#!/usr/bin/env python3
"""Build a self-contained Agent Skill ZIP with one top-level fhir-suite directory."""
import argparse
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', type=Path)
args = parser.parse_args()
subprocess.run([sys.executable, str(ROOT / 'tools/sync_distribution.py'), '--check'], check=True)
subprocess.run([sys.executable, str(ROOT / 'tools/validate.py')], check=True)
source = ROOT / 'skills/fhir-suite'
if args.output.resolve().is_relative_to(source.resolve()):
    parser.error('Output must be outside the skill directory')
args.output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.output, 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        info = zipfile.ZipInfo('fhir-suite/' + path.relative_to(source).as_posix(), date_time=(2026, 10, 15, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes())
print(args.output)
