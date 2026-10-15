# Clinical domain routes

Select the release and IG first. The resources below are navigation starting points, not substitute definitions. Every resource has a direct link in the [complete catalog](../../fhir-standards/references/resources.md); inspect its boundaries, elements, constraints, terminology, search, operations and applicable profiles.

| Domain | Core resources to investigate | Primary route |
| --- | --- | --- |
| Clinical summary and longitudinal record | Condition, ConditionDefinition, AllergyIntolerance, Procedure, FamilyMemberHistory, ClinicalImpression, AdverseEvent, DetectedIssue, RiskAssessment, Flag, CarePlan, CareTeam, Goal | [Clinical module](https://hl7.org/fhir/R5/clinicalsummary-module.html) |
| Diagnostics and lab | Observation, ObservationDefinition, DiagnosticReport, ServiceRequest, Specimen, SpecimenDefinition, BodyStructure, DocumentReference | [Diagnostics](https://hl7.org/fhir/R5/diagnostics-module.html) |
| Imaging | ImagingStudy, ImagingSelection, DiagnosticReport, ServiceRequest | Diagnostics plus the selected imaging/DICOM IG |
| Genomics | GenomicStudy, MolecularSequence, Observation, DiagnosticReport, Specimen, ServiceRequest | Diagnostics plus the genomics guide linked by that module; representations vary across IG versions |
| Patient medication workflow | Medication, MedicationRequest, MedicationDispense, MedicationAdministration, MedicationStatement, MedicationKnowledge, FormularyItem | [Medications](https://hl7.org/fhir/R5/medications-module.html) and [workflow](../../fhir-workflow/GUIDE.md) |
| Vaccinations | Immunization, ImmunizationEvaluation, ImmunizationRecommendation | Medications module and the jurisdiction's immunization profiles |
| Nutrition | NutritionOrder, NutritionIntake, NutritionProduct | Clinical module, product definitions and workflow |
| Devices and supplies | Device, DeviceDefinition, DeviceMetric, DeviceAssociation, DeviceRequest, DeviceUsage, DeviceDispense, SupplyRequest, SupplyDelivery, InventoryItem, InventoryReport, Transport | [Administration](https://hl7.org/fhir/R5/administration-module.html) and [workflow](https://hl7.org/fhir/R5/workflow-module.html) |
| Biologically derived products | BiologicallyDerivedProduct, BiologicallyDerivedProductDispense | Administration and workflow; preserve donor/product identifiers and traceability requirements |
| Regulated medicinal products | MedicinalProductDefinition, AdministrableProductDefinition, ManufacturedItemDefinition, PackagedProductDefinition, Ingredient, ClinicalUseDefinition, RegulatedAuthorization | [Medication Definition](https://hl7.org/fhir/R5/medication-definition-module.html) |
| Substances and chemistry | Substance, SubstanceDefinition, SubstanceNucleicAcid, SubstancePolymer, SubstanceProtein, SubstanceReferenceInformation, SubstanceSourceMaterial | Medication Definition plus each resource's scope |
| Forms and clinical documents | Questionnaire, QuestionnaireResponse, Composition, DocumentReference, List | [Foundation](https://hl7.org/fhir/R5/foundation-module.html), SDC/IPS guides via [IG discovery](../../fhir-implementation-guides/GUIDE.md) |
| Studies and evidence | ResearchStudy, ResearchSubject, Evidence, EvidenceVariable, EvidenceReport, Citation, ArtifactAssessment | [Clinical Reasoning](../../fhir-clinical-reasoning/GUIDE.md) and the selected research IG |

For specialty use cases (oncology, public health, vital signs, pathology, genomics, dental, vision, research), search the live IG registry and that guide's artifacts instead of treating this routing table as the entire ecosystem. Check VisionPrescription and other specialized resources through the complete resource catalog. Avoid using Basic as a shortcut around an existing appropriate resource/profile without a documented modeling reason.
