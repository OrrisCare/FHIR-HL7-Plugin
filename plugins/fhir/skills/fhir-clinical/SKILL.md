---
name: fhir-clinical
description: "Design, edit, audit, or refactor FHIR clinical records, diagnostics, medications, immunizations, nutrition, devices, genomics and medicinal-product models."
---

# FHIR Clinical Domains

Resolve the [release, jurisdiction and clinical IG](../fhir-standards/references/releases.md). Start from [domain routes](references/domains.md), then read each chosen resource's scope, definitions, constraints and profile. The [complete resource catalog](../fhir-standards/references/resources.md) covers specialized resources too.

## Preserve clinical meaning

- Separate diagnoses/problems (Condition), measurements/assertions (Observation), procedures (Procedure), reports (DiagnosticReport), orders (ServiceRequest and other request resources), and documents. Similar text does not imply interchangeable clinical semantics.
- Preserve status, intent, effective/performed/authored time, subject, encounter, performer, specimen, body site, method, interpretation and reference range as applicable. Absent, unknown, negative and not-performed are different states; do not invent values to satisfy a validator.
- Model panels through the appropriate Observation.component/hasMember relationships; they are not interchangeable. Preserve DiagnosticReport results and report context. Use ImagingStudy/ImagingSelection and DICOM identifiers according to the diagnostic IG; avoid putting image bytes in arbitrary resource fields.
- Distinguish Medication, MedicationRequest, MedicationDispense, MedicationAdministration and MedicationStatement. Preserve dosage sequence, timing, route, site, dose/rate, product strength and actual versus planned use. Unit conversion or terminology substitution requires semantic evidence.
- Keep Immunization, ImmunizationEvaluation and ImmunizationRecommendation distinct. Use nutrition, device, substance and medicinal-product resources when their scope fits; regulated product definitions are not patient medication events.
- Follow domain-specific IGs for genomics, oncology, clinical summaries and questionnaires. A QuestionnaireResponse is not automatically a validated Observation extraction; follow the questionnaire's definitions and published extraction rules.

For changes, compare clinically significant fields and relationships before/after. Use the [terminology](../fhir-terminology/SKILL.md) and [validation](../fhir-validation/SKILL.md) workflows as needed. Report modeling uncertainty rather than deriving a diagnosis or prescribing treatment from missing information. This skill supports software and data interoperability, not autonomous clinical decision-making.
