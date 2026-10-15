#!/usr/bin/env python3
"""Generate host manifests and a self-contained skill from canonical plugin sources."""
import argparse
import json
from pathlib import Path
import re
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/fhir'
SUITE = 'skills/fhir-suite'


def generated(target):
    manifest = json.loads((PLUGIN / 'plugin.json').read_text())
    common = {k: manifest[k] for k in ('name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords')}
    def write(relative, content):
        p = target / relative
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    def js(relative, value):
        write(relative, json.dumps(value, indent=2) + '\n')
    js('plugins/fhir/.claude-plugin/plugin.json', dict(common, skills='./skills'))
    js('plugins/fhir/.cursor-plugin/plugin.json', dict(common, skills='./skills', logo='./assets/icon.svg'))
    js('.claude-plugin/marketplace.json', {
        'name': 'orris-fhir', 'owner': manifest['author'], 'description': 'FHIR standards skills by Orris',
        'plugins': [dict(name='fhir', source='./plugins/fhir', description=manifest['description'])]})
    js('.cursor-plugin/marketplace.json', {
        'name': 'orris-fhir', 'owner': manifest['author'],
        'metadata': {'description': 'FHIR standards skills by Orris'},
        'plugins': [dict(name='fhir', source='./plugins/fhir', description=manifest['description'])]})
    suite = target / SUITE
    for source in sorted((PLUGIN / 'skills').rglob('*')):
        if not source.is_file() or 'agents' in source.relative_to(PLUGIN / 'skills').parts or '__pycache__' in source.parts or source.suffix == '.pyc':
            continue
        relative = source.relative_to(PLUGIN / 'skills')
        if source.name == 'SKILL.md':
            relative = relative.with_name('GUIDE.md')
        dest = suite / 'references/workflows' / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == '.md':
            # Preserve the sibling layout; change only local Markdown link targets.
            def link(match):
                value = match[1]
                if not value.startswith(('http://', 'https://')):
                    value = value.replace('SKILL.md', 'GUIDE.md')
                return '](' + value + ')'
            dest.write_text(re.sub(r'\]\(([^)]+)\)', link, source.read_text()))
        else:
            shutil.copyfile(source, dest)
    write(SUITE + '/SKILL.md', '''---
name: fhir-suite
description: "Use HL7 FHIR standards to build, modify, validate, audit, or refactor healthcare software. Includes version selection, modeling, APIs, profiles, terminology, security, clinical domains, workflow, implementation guides and migrations."
license: MIT
---

# FHIR by Orris

This is the self-contained distribution of the 16-workflow FHIR plugin. It includes its own documentation indexes, references and optional Python lookup helper. No other skill, MCP server, network service account or host-specific command is required to load it.

For any FHIR task, first read [the standards navigator](references/workflows/fhir-standards/GUIDE.md). It selects the release and routes to the relevant workflow. Follow its local links to the bundled GUIDE.md files and primary documentation. Read only the relevant workflow and references, not all indexes at once. Each guide's relative paths are resolved from that guide's directory. The lookup helper can be invoked with its full path under `references/workflows/fhir-standards/scripts/lookup.py` when a Python-capable shell is available; otherwise use the linked resource table and official registries.

The checked baseline is FHIR R5 5.0.0; keep existing R4/R4B contracts and treat R6 as an explicit preview until publication status is reverified. Follow the user's authorized task and preserve the selected actor/IG requirements. Cite primary sources and distinguish validated facts from assumptions or unexecuted checks.

This package exposes one skill to the host; the 16 internal workflows are reference guides, not separately installed skills. Do not also install the full plugin/16-skill form in the same scope unless duplicate routing is intentional. See [attribution](NOTICE.md).
''')
    shutil.copyfile(PLUGIN / 'LICENSE', suite / 'LICENSE')
    write(SUITE + '/NOTICE.md', '''# Attribution

Original instructions and code: Copyright 2026 Orris Care, Inc., MIT. Generated from the canonical plugin in https://github.com/OrrisCare/FHIR-HL7-Plugin.

Core metadata/descriptions come from HL7's FHIR R5 core package (CC0-1.0). HL7 and FHIR are HL7 trademarks; this is an independent project with no HL7 endorsement. External terminology and guide licenses remain applicable.

See [coverage and source hashes](references/workflows/fhir-standards/references/coverage.md). Index inclusion is not proof that every document was read or every implementation is conformant. No clinical or regulatory certification is provided.
''')
    js(SUITE + '/distribution.json', {'name': 'fhir-suite', 'version': manifest['version'], 'source': manifest['repository'], 'workflows': 16})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='fhir-distribution-') as temp:
        candidate = Path(temp)
        generated(candidate)
        paths = [p.relative_to(candidate) for p in candidate.rglob('*') if p.is_file()]
        if args.check:
            mismatches = [str(p) for p in paths if not (ROOT / p).is_file() or (ROOT / p).read_bytes() != (candidate / p).read_bytes()]
            expected = {p for p in paths if p.is_relative_to(SUITE)}
            existing = {p.relative_to(ROOT) for p in (ROOT / SUITE).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
            mismatches += [str(p) for p in existing - expected]
            if mismatches:
                parser.exit(1, 'Generated distribution differs: ' + ', '.join(mismatches) + '\n')
            print('PASS: host manifests and self-contained bundle match canonical source')
        else:
            # This directory is generated; never point it at a user's installed skills.
            if (ROOT / SUITE).exists():
                shutil.rmtree(ROOT / SUITE)
            for relative in paths:
                dest = ROOT / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(candidate / relative, dest)
            print(f'Generated {len(paths)} distribution files')


if __name__ == '__main__':
    main()
