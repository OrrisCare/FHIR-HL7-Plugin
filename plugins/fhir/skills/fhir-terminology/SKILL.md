---
name: fhir-terminology
description: "Implement, debug, or audit FHIR CodeSystems, ValueSets, ConceptMaps, terminology bindings and terminology-service operations."
---

# FHIR Terminology

Resolve the [release/IG contract](../fhir-standards/references/releases.md), terminology edition/version, jurisdiction and terminology-service capabilities. Terminology packages and external code systems have lifecycles separate from FHIR core.

## Resolve the meaning

- Keep `CodeSystem` (concept identity/meaning), `ValueSet` (selection of allowed concepts), `ConceptMap` (relationships between concepts), and `NamingSystem` (identifier metadata) distinct. `Coding.system` identifies the code system, not the ValueSet URL. Display strings and free text are not stable codes.
- Read the element's binding, not merely a list shown in an example. Required and extensible bindings impose different rules. Extensible does not mean any local code is always acceptable: use an applicable concept from the bound set when it exists, and inspect the datatype-specific rules. Preferred and example bindings do not impose required membership. Respect additional bindings and context.
- For CodeableConcept, preserve multiple codings, source text and userSelected semantics. Do not assume all codings are interchangeable or that a display-only change changes identity. For quantities, verify UCUM syntax and compatible units before conversion.
- Inspect ValueSet.compose, imports, exclusions, filters, inactive/abstract handling and locked versions. A cached expansion is parameter- and version-dependent; expansions can be paged or incomplete. Record the expansion identifier/date and parameters when reproducibility matters.
- Read the selected operation definition for `$expand`, `$validate-code`, `$lookup`, `$subsumes`, `$translate` and supported closure behavior. Distinguish a service outage or unknown code-system version from an invalid code. An HTTP 200 alone does not mean a validation result is true.
- ConceptMap relationships are directional and version-specific; R4 `equivalence` and R5 `relationship` must not be mixed. Check context, dependencies, unmapped behavior and mapping relationship before transforming data. Do not invent mappings or normalize clinically distinct concepts as a formatting fix.
- Account for SNOMED CT, LOINC, RxNorm, ICD and other publisher licensing/distribution terms. FHIR's open license does not grant rights to every referenced terminology.

For code changes, test both allowed and disallowed concepts under pinned versions, plus service-unavailable behavior where relevant. Report terminology availability limits explicitly.

## Read from authoritative sources

[Terminology module](https://hl7.org/fhir/R5/terminology-module.html) · [Bindings](https://hl7.org/fhir/R5/terminologies.html) · [Terminology service](https://hl7.org/fhir/R5/terminology-service.html) · [CodeSystem](https://hl7.org/fhir/R5/codesystem.html) · [ValueSet](https://hl7.org/fhir/R5/valueset.html) · [ConceptMap](https://hl7.org/fhir/R5/conceptmap.html) · [NamingSystem](https://hl7.org/fhir/R5/namingsystem.html) · [HL7 Terminology](https://terminology.hl7.org/) · [UCUM](https://ucum.org/).
