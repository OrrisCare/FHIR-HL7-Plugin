---
name: fhir-suite
description: "Use HL7 FHIR standards to build, modify, validate, audit, or refactor healthcare software. Includes version selection, modeling, APIs, profiles, terminology, security, clinical domains, workflow, implementation guides and migrations."
license: MIT
---

# FHIR by Orris

This is the self-contained distribution of the 16-workflow FHIR plugin. It includes its own documentation indexes, references and optional Python lookup helper. No other skill, MCP server, network service account or host-specific command is required to load it.

For any FHIR task, first read [the standards navigator](references/workflows/fhir-standards/GUIDE.md). It selects the release and routes to the relevant workflow. Follow its local links to the bundled GUIDE.md files and primary documentation. Read only the relevant workflow and references, not all indexes at once. Each guide's relative paths are resolved from that guide's directory. The lookup helper can be invoked with its full path under `references/workflows/fhir-standards/scripts/lookup.py` when a Python-capable shell is available; otherwise use the linked resource table and official registries.

The checked baseline is FHIR R5 5.0.0; keep existing R4/R4B contracts and treat R6 as an explicit preview until publication status is reverified. Follow the user's authorized task and preserve the selected actor/IG requirements. Cite primary sources and distinguish validated facts from assumptions or unexecuted checks.

This package exposes one skill to the host; the 16 internal workflows are reference guides, not separately installed skills. Do not also install the full plugin/16-skill form in the same scope unless duplicate routing is intentional. See [attribution](NOTICE.md).
