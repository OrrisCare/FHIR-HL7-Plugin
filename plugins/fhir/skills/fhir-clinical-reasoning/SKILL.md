---
name: fhir-clinical-reasoning
description: "Implement or review FHIR knowledge artifacts, CDS integration, CQL/FHIRPath use, quality measures, evidence and research interoperability."
---

# FHIR Clinical Reasoning

Establish the [release and IG contract](../fhir-standards/references/releases.md). Read the [clinical reasoning module](https://hl7.org/fhir/R5/clinicalreasoning-module.html), then the route that matches the task.

- **Expressions:** distinguish FHIRPath navigation/invariants from CQL clinical logic. Pin language version, FHIR model/modelinfo and libraries. Resolve `canonical|version` dependencies and evaluation context; empty/null, collection, date precision and timezone semantics affect results. Do not assume identical behavior between expression engines.
- **Knowledge artifacts:** Library, PlanDefinition and ActivityDefinition package logic and reusable plans/actions. Resolve parameters, relatedArtifact dependencies, data requirements and terminology versions. Applying a plan and fulfilling its proposed actions are separate events. Preserve subject/context and output resource semantics.
- **CDS:** use the selected [CDS Hooks specification](https://cds-hooks.org/) and published FHIR/SMART guidance. Read hook context, prefetch, discovery, response cards/suggestions, authorization and failure behavior. CDS Hooks is not itself a FHIR REST operation. A suggestion is not permission to execute a clinical action.
- **Quality measurement:** distinguish Measure definition from MeasureReport results and use the declared `$evaluate-measure` OperationDefinition. Pin measurement period, population basis, initial populations, denominators, exclusions/exceptions, stratifiers and supplemental data. Check individual versus summary/data-collection report semantics and subject references.
- **Evidence and research:** use Evidence, EvidenceVariable, Citation and ArtifactAssessment for their stated purposes; ResearchStudy and ResearchSubject describe studies and participation. Check specialized IGs before translating statistical results or research data. Do not treat EvidenceReport as interchangeable with DiagnosticReport.

For evaluation software, use known synthetic fixtures with explicit expected populations/actions and verify missing-data, terminology, dependency-version and temporal boundary behavior. Distinguish conformance of the artifact from accuracy or suitability of its clinical recommendations.

Read [knowledge distribution](https://hl7.org/fhir/R5/clinicalreasoning-knowledge-artifact-distribution.html), [CDS on FHIR](https://hl7.org/fhir/R5/clinicalreasoning-cds-on-fhir.html), [FHIRPath](https://hl7.org/fhir/R5/fhirpath.html), [CQL](https://cql.hl7.org/), and the [resource catalog](../fhir-standards/references/resources.md). Use the [IG discovery workflow](../fhir-implementation-guides/SKILL.md) for CQF, quality reporting and evidence guides.
