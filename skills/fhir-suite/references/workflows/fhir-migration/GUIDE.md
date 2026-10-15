---
name: fhir-migration
description: "Migrate FHIR versions or transform HL7 v2, CDA, source databases and other models into FHIR while preserving semantics and documenting loss."
---

# FHIR Migration and Mapping

Establish both source and target contracts: FHIR/other format version, profile/IG packages, terminology, actor behavior and intended use. Read [release guidance](../fhir-standards/references/releases.md). An existing R4 system is not implicitly authorized for an R5 upgrade.

## Map deliberately

1. Inventory resource types, extensions, references, datatypes, profiles, search parameters, operations, capabilities and persistence/API assumptions. Compare official version histories and each resource's version-conversion notes, not only property names.
2. Create a mapping table: source element and meaning, target element/type, transformation, terminology mapping, cardinality/null policy, reference handling and loss/ambiguity. Classify mappings as direct, transformed, deferred or unsupported with reasons.
3. Use version-specific StructureMaps/conversion libraries where applicable, but verify their maturity, coverage and handling of unknown extensions. R4↔R5 conversion can lose information. New resource types and changed workflow/status semantics may need application changes.
4. Preserve identifiers, canonical business versions, reference identities, provenance, precision and absent-data semantics. Use ConceptMap relationships only when their direction/context permits the transformation. Do not replace unknown codes with a plausible clinical value.
5. For HL7 v2/CDA, pin the message/document version and local conformance profile; source field positions alone do not establish clinical semantics. Use the relevant published mapping IG from the registry and record local customizations. StructureMap/FHIR Mapping Language maps structures; it does not automatically resolve clinical ambiguity.
6. Validate target data against its actual profiles, test representative round trips where meaningful, and measure intentional/non-recoverable loss. Verify API/search changes, migration ordering, reference rewrites and application compatibility. Plan rollback and parallel-version operation for a requested rollout before changing live data.

For an ordinary refactor with no version migration, preserve the existing external contract and compare observable behavior.

Read [version policy](https://hl7.org/fhir/R5/versions.html), [managing versions](https://hl7.org/fhir/R5/versioning.html), [version differences](https://hl7.org/fhir/R5/diff.html), [StructureMap](https://hl7.org/fhir/R5/structuremap.html), [mapping language](https://hl7.org/fhir/R5/mapping-language.html), [ConceptMap](https://hl7.org/fhir/R5/conceptmap.html), and each affected resource's version maps from the [TOC](https://hl7.org/fhir/R5/toc.html).
