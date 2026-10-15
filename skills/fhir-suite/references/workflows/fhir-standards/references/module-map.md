# All R5 modules and how to reach them

This maps every module linked from the official [R5 module overview](https://hl7.org/fhir/R5/modules.html). Cross-cutting workflows deliberately span modules. Read only the rows relevant to the task, then follow the module's own resource, operation and detailed-topic links.

| Official module | Primary skill | Scope and deeper routes |
| --- | --- | --- |
| [Foundation](https://hl7.org/fhir/R5/foundation-module.html) | [Modeling](../../fhir-modeling/GUIDE.md) | Resource/DomainResource, primitives/complex/metadata datatypes, references, extensions, narrative, JSON/XML/NDJSON/RDF, Bundle, Binary, Parameters, Questionnaire/Response, List |
| [Implementation Support](https://hl7.org/fhir/R5/implsupport-module.html) | [Validation](../../fhir-validation/GUIDE.md), [Migration](../../fhir-migration/GUIDE.md) | Downloads, tooling, FHIRPath, mapping language, safety, identity, interaction patterns, TestPlan/Script/Report, ExampleScenario, Requirements, ActorDefinition, v2/v3/CDA comparisons |
| [Security and Privacy](https://hl7.org/fhir/R5/secpriv-module.html) | [Security](../../fhir-security/GUIDE.md) | Authentication/authorization, labels, consent, Permission, AuditEvent, Provenance, signatures, de-identification and test data |
| [Conformance](https://hl7.org/fhir/R5/conformance-module.html) | [Conformance](../../fhir-conformance/GUIDE.md) | Profiles, StructureDefinition, ElementDefinition, CapabilityStatement, OperationDefinition, SearchParameter, CompartmentDefinition, ImplementationGuide |
| [Terminology](https://hl7.org/fhir/R5/terminology-module.html) | [Terminology](../../fhir-terminology/GUIDE.md) | Code systems, value sets, mappings, NamingSystem, TerminologyCapabilities, bindings, service operations, terminology registries |
| [Exchange](https://hl7.org/fhir/R5/exchange-module.html) | [API](../../fhir-api/GUIDE.md), [Exchange](../../fhir-exchange/GUIDE.md) | REST, search, operations, transactions, documents, messaging, services, persistence, subscriptions and external exchange standards |
| [Administration](https://hl7.org/fhir/R5/administration-module.html) | [Administration](../../fhir-administration/GUIDE.md) | People, providers, organizations, care context, encounters, locations, endpoints, groups, administrative inventories |
| [Clinical](https://hl7.org/fhir/R5/clinicalsummary-module.html) | [Clinical](../../fhir-clinical/GUIDE.md) | Conditions, allergy, procedures, family history, care plans/teams/goals, risks, adverse events, nutrition |
| [Diagnostics](https://hl7.org/fhir/R5/diagnostics-module.html) | [Clinical domain routes](../../fhir-clinical/references/domains.md) | Observations, laboratory/reporting, specimens, body structures, imaging, genomics |
| [Medications](https://hl7.org/fhir/R5/medications-module.html) | [Clinical domain routes](../../fhir-clinical/references/domains.md) | Medication order/dispense/admin/use, medication knowledge, formulary and immunization |
| [Workflow](https://hl7.org/fhir/R5/workflow-module.html) | [Workflow](../../fhir-workflow/GUIDE.md) | Definition/Request/Event patterns, Task, scheduling, orders, coordination, supply/device/transport workflows |
| [Financial](https://hl7.org/fhir/R5/financial-module.html) | [Financial](../../fhir-financial/GUIDE.md) | Coverage, eligibility, enrollment, claims, adjudication, billing, payments and contracts |
| [Clinical Reasoning](https://hl7.org/fhir/R5/clinicalreasoning-module.html) | [Clinical Reasoning](../../fhir-clinical-reasoning/GUIDE.md) | Expressions/CQL, knowledge artifacts, CDS, quality measures, evidence, citations, research |
| [Medication Definition](https://hl7.org/fhir/R5/medication-definition-module.html) | [Clinical domain routes](../../fhir-clinical/references/domains.md) | Medicinal products, packaging, ingredients, substances, regulated authorization and manufacturing |

## Completeness routes beyond modules

- [Table of contents](https://hl7.org/fhir/R5/toc.html): every indexed core documentation topic, resource subpage and schema page.
- [Resource list](https://hl7.org/fhir/R5/resourcelist.html): scope, examples, definitions, mappings, profiles, search, operations and version maps for resources.
- [Datatypes](https://hl7.org/fhir/R5/datatypes.html), [metadata types](https://hl7.org/fhir/R5/metadatatypes.html), [patterns](https://hl7.org/fhir/R5/patterns.html): non-resource models and shared abstractions.
- [Operations](https://hl7.org/fhir/R5/operationslist.html), [search parameters](https://hl7.org/fhir/R5/searchparameter-registry.html), [profiles](https://hl7.org/fhir/R5/profilelist.html), [terminology systems](https://hl7.org/fhir/R5/terminologies-systems.html): specialized artifact registries.
- [Extensions](https://hl7.org/fhir/extensions/extension-registry.html) and [IG registry](https://fhir.org/guides/registry/): separately released ecosystem content. See [IG selection](../../fhir-implementation-guides/GUIDE.md).
- [Downloads](https://hl7.org/fhir/R5/downloads.html): authoritative packages, definitions and schemas. The offline artifact index includes every core-package entry, including logical models and datatypes, not just concrete resources.

Use `scripts/lookup.py` from the parent standards skill for exact resource, artifact and page discovery. If a topic is not in the curated prose, search the complete indexes and follow the corresponding primary source instead of assuming FHIR does not cover it.
