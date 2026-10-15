---
name: fhir-modeling
description: "Design, implement, edit, or refactor FHIR resource models, datatypes, serialization, references, extensions, and persistence mappings."
---

# FHIR Data Modeling

Establish the release and IG contract using [release selection](../fhir-standards/references/releases.md). Use the [resource index](../fhir-standards/references/resources.md) to choose resources by scope and boundaries, not just matching names.

## Model and implement

1. Read the selected resource page and its element definitions. Record cardinality, choice types, reference targets, bindings, invariants, modifier flags, and inherited elements. Use its StructureDefinition from the pinned core/IG package when generating models.
2. Distinguish logical resource `id`, business `Identifier`, canonical URL, and resource history version. Preserve identifier namespaces and reference context. Relative, absolute, contained (`#id`), version-specific and logical references require different resolution; canonical `url|version` is not an instance reference.
3. Serialize a choice element such as `value[x]` as its actual typed property (for example `valueQuantity`). Do not invent resource fields. Repeating elements remain arrays even with one item. Preserve primitive `_element` extensions, including aligned null placeholders in repeating primitive arrays. Other empty strings/objects and ordinary null properties are not interchangeable with absence.
4. Preserve decimal precision, date/time precision and timezone rules, case-sensitive codes, units, and absent/unknown distinctions. Use UCUM system/code when the contract calls for coded units; a display label is not a unit identity. Do not turn partial dates into invented full timestamps.
5. Reuse published extensions with the correct context and release. Understand modifier extensions before processing affected content. Preserve unknown extensions through round trips when the task requires fidelity; do not silently discard clinically meaningful fields during refactoring.
6. Check Bundle identity/reference resolution, contained-resource constraints and safe XHTML narrative. Treat attachments and external reference resolution as explicit I/O decisions.

Validate representative round trips and edge cases relevant to the changed fields. For persistence, document which FHIR information the storage model cannot preserve; avoid claiming a lossless mapping without evidence. For XML/RDF, use that format's rules rather than mechanically translating JSON conventions.

## Read from HL7

- [Resource framework](https://hl7.org/fhir/R5/resource.html), [DomainResource](https://hl7.org/fhir/R5/domainresource.html), [resource definitions](https://hl7.org/fhir/R5/resource-definitions.html).
- [Datatypes](https://hl7.org/fhir/R5/datatypes.html), [references](https://hl7.org/fhir/R5/references.html), [extensibility](https://hl7.org/fhir/R5/extensibility.html).
- [JSON](https://hl7.org/fhir/R5/json.html), [XML](https://hl7.org/fhir/R5/xml.html), [RDF](https://hl7.org/fhir/R5/rdf.html), [narrative](https://hl7.org/fhir/R5/narrative.html).
- [FHIRPath](https://hl7.org/fhir/R5/fhirpath.html), [Bundle](https://hl7.org/fhir/R5/bundle.html), [ElementDefinition](https://hl7.org/fhir/R5/elementdefinition.html).
