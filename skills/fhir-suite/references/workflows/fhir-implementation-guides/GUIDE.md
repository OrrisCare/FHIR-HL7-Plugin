---
name: fhir-implementation-guides
description: "Find applicable FHIR implementation guides or build, update, and publish an IG with pinned packages, FSH/SUSHI and IG Publisher."
---

# FHIR Implementation Guides

Resolve the user's jurisdiction, clinical domain, actors, exchange partners and existing contracts before choosing an IG. Use [ecosystem routes](references/ecosystem.md) and the [HL7/FHIR guide registry](https://fhir.org/guides/registry/); that registry remains the discovery source for guides beyond the examples listed here.

## Select an existing guide

Open its home page, directory/history, package metadata, dependencies, table of contents, artifacts index, actor requirements and downloads. Follow browser/meta redirects when necessary. Pin its published package ID/version and FHIR dependency. Do not equate the IG version with the FHIR version, pick a CI build by default, or assume that a guide supports R5 merely because R5 is newer. Report conflicts between overlapping guides instead of silently dropping constraints.

## Build or update an IG

1. Define canonical, package ID, business version, FHIR version, publisher, jurisdiction, license and dependencies in the project's existing configuration. Preserve namespaces already in use.
2. Author profiles/extensions, value sets, operations, capabilities, examples and narrative according to the actor contract. Use [fhir-conformance](../fhir-conformance/GUIDE.md) for constraints and FSH. Include testable requirements and examples of edge cases where they clarify interoperability.
3. Pin SUSHI/IG Publisher and dependency versions. Follow the [official IG tooling guidance](https://build.fhir.org/ig/FHIR/ig-guidance/) and [FHIR Shorthand](https://hl7.org/fhir/uv/shorthand/) documentation for current commands. Inspect existing build scripts rather than replacing a functioning toolchain.
4. Build and inspect QA results, generated snapshots, canonical resolution, broken links, example validation and terminology availability. Separate errors, warnings, unavailable dependencies and known narrative limitations.
5. For a requested release, verify publication metadata, package contents, version/history links and source/release reproducibility. Publishing an IG or modifying its registry entry is a separate external action and must be within the user's requested scope; creating this plugin does not authorize publishing an unrelated IG.

Return the selected guide and package versions, rationale, build/QA evidence, and remaining compatibility issues. Read a guide's normative actor requirements in addition to its computable artifacts.
