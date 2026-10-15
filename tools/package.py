#!/usr/bin/env python3
"""Validate and produce a deterministic plugin-only ZIP for distribution."""
import argparse
from pathlib import Path
import sys
import zipfile
from validate import PLUGIN, validate

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output", type=Path)
args = parser.parse_args()
errors = validate()
if errors:
    sys.exit("\n".join(errors))
if args.output.resolve().is_relative_to(PLUGIN.resolve()):
    sys.exit("ZIP output must be outside the plugin directory")
args.output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(PLUGIN.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
            continue
        info = zipfile.ZipInfo(path.relative_to(PLUGIN).as_posix(), date_time=(2026, 10, 15, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes())
print(args.output)
