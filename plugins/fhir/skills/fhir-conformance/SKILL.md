---
name: fhir-conformance
description: "Author, inspect, or refactor FHIR StructureDefinitions, profiles, extensions, slicing, FSH, CapabilityStatements, and conformance requirements."
---

# FHIR Profiles and Extensions

Pin the [base release and IG dependencies](../fhir-standards/references/releases.md). Read the base StructureDefinition and the entire relevant profile inheritance chain before changing constraints.

## Author or review a profile

1. State the actor/use case and what needs constraining. Prefer a compatible existing profile or extension. Assign a stable canonical under a namespace the project controls; keep its business version distinct from resource `meta.versionId`.
2. Apply legal derivation rules: constraints narrow the base and cannot relax its cardinality or type requirements. Distinguish fixed values from patterns. Ensure reference target profiles, choice types and binding constraints are valid for the base.
3. For slicing, inspect discriminators, slice names, rules (open/closed/openAtEnd), ordering, reslicing and each slice's cardinality. Validate positive and near-miss examples; a discriminator that cannot uniquely distinguish slices creates interoperability problems.
4. `MustSupport` is not minimum cardinality. Read the IG's actor-specific definition and obligations before deciding what clients or servers must store, display, populate, query, or return. Do not import an R6 obligations mechanism into R5 without its published compatible extension/IG.
5. Define extension context, value type, cardinality and invariants; distinguish simple and complex extensions and modifier semantics. Follow the extension registry's own package/release, since it is maintained separately from R5 core.
6. Keep differential authoring and generated snapshot consistent. Resolve dependencies and regenerate snapshots with the chosen toolchain; do not hand-edit generated snapshots to hide an invalid differential. Use stable element IDs, canonical references and explicit version dependencies.
7. With FSH/SUSHI, check the FSH grammar version and supported FHIR release. Pin package dependencies and tool versions. Validate the generated StructureDefinitions and examples, then run IG Publisher QA for an IG change.

Return the changed artifacts, the requirements they encode, and the actual validation results. A profile definition, CapabilityStatement declaration, example instance and implemented runtime behavior are different evidence.

## Authoritative reading

[Profiling](https://hl7.org/fhir/R5/profiling.html) · [Conformance rules](https://hl7.org/fhir/R5/conformance-rules.html) · [StructureDefinition](https://hl7.org/fhir/R5/structuredefinition.html) · [ElementDefinition](https://hl7.org/fhir/R5/elementdefinition.html) · [Extensibility](https://hl7.org/fhir/R5/extensibility.html) · [Extension registry](https://hl7.org/fhir/extensions/extension-registry.html) · [FHIR Shorthand](https://hl7.org/fhir/uv/shorthand/) · [IG tooling guidance](https://build.fhir.org/ig/FHIR/ig-guidance/).
