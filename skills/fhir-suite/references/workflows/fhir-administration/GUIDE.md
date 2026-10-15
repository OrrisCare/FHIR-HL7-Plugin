---
name: fhir-administration
description: "Model or maintain FHIR patient identity, people, providers, organizations, locations, encounters and administrative relationships."
---

# FHIR Administration

Select the [release and applicable IG](../fhir-standards/references/releases.md). Use the [administration module](https://hl7.org/fhir/R5/administration-module.html) and [complete resource index](../fhir-standards/references/resources.md) to resolve scope and boundaries.

## Model the actors and context

- Distinguish Patient (subject in a care context), Person (identity linkage), RelatedPerson (relationship to a patient), Practitioner and PractitionerRole. A practitioner and their role/organization/location affiliations are not interchangeable references.
- Preserve Identifier.system/value/assigner/use/period semantics. Logical resource IDs need not be globally unique business identifiers. Do not merge people based only on similar names or date of birth. A matching score or duplicate candidate is not authorization to merge records.
- Model Organization, OrganizationAffiliation, HealthcareService, Location and Endpoint according to their distinct purposes. The existence of Endpoint does not prove supported capabilities or permission to connect.
- Distinguish Encounter, EncounterHistory and EpisodeOfCare and read their version-specific statuses, class and period definitions. Do not copy R4 Encounter field layouts into R5. Preserve participant, subject, location and service-provider relationships.
- Use Group's membership/characteristic semantics for populations and non-person subjects where appropriate. Inspect actual versus definitional membership and inclusion criteria, rather than assuming a patient list.
- For scheduling, use [fhir-workflow](../fhir-workflow/GUIDE.md). For merging, linking or identity operations, inspect the selected OperationDefinition and server support, preserve provenance and references, and require the user's intended scope before mutating records.

For a change, check identifier collisions, reference resolution, version-specific fields and actor/jurisdiction requirements. Use synthetic identities and explain unresolved matching ambiguities.

Read each applicable page through the resource index, including Patient, Person, RelatedPerson, Practitioner, PractitionerRole, Organization, OrganizationAffiliation, HealthcareService, Location, Endpoint, Encounter, EncounterHistory, EpisodeOfCare, Group, Linkage and VerificationResult. Their definitions and inherited constraints are the implementation authority.
