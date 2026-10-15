# Coverage and provenance

Baseline checked on **2026-10-15**. The curated workflows cover all **14 R5 modules**, with **16 skills** for task-based routing.

## What is complete in the snapshot

- **162 resource definitions** from the official R5 core package: 158 concrete and 4 abstract.
- **2968 core-package indexed artifacts**, including all indexed StructureDefinitions (resource profiles, datatypes and logical models), SearchParameters, OperationDefinitions, ValueSets, CodeSystems, ConceptMaps and other conformance artifacts.
- **3173 unique R5 HTML page targets** extracted from links in the official table-of-contents document, including its navigation links. Includes resource subpages and schema pages.

The complete machine-readable files are [resources.json](indexes/resources.json), [artifacts.json](indexes/artifacts.json), [pages.json](indexes/pages.json), [publication history](indexes/releases.json) and [provenance/counts/hashes](indexes/provenance.json). Use the lookup helper rather than loading all JSON into context.

## Scope limits

This is an index and task guidance, not a mirror of all specification prose. Index generation reads the TOC and all indexed core-package definitions; it does not establish that every linked page is available or that every definition has been manually reviewed. The authoring process retrieved core narrative/module sources and selected ecosystem landing pages. Source retrieval is recorded separately in [research-sources.json](indexes/research-sources.json), including failures; retrieval is not semantic validation.

External IGs, extension packs, terminology editions and examples/expansions/search packages are independently released and are not exhaustively embedded. Follow the registries and each selected guide's TOC, artifact index and package dependencies. R4/R4B compatibility and R6 preview routes are provided, but their complete artifact catalogs are not bundled. Repository validation checks file integrity, routing, indexes and helper behavior; it does not certify every clinical/software use case.

## Reproducible maintenance

`tools/build_indexes.py` in the source repository regenerates candidate indexes from three fixed official sources, or accepts previously downloaded copies. It refuses nonempty output directories and verifies the R5 package identity/version. Compare candidates before replacing this snapshot. See [maintenance workflow](../../fhir-maintenance/GUIDE.md).

Source attribution: HL7 International, FHIR R5 core package (`CC0-1.0` package metadata). FHIR and HL7 are HL7 trademarks. The plugin is an independent Orris project, not an HL7 endorsement. Externally referenced terminologies may have separate licenses.
