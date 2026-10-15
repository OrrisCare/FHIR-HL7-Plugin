---
name: fhir-validation
description: "Validate, test, debug, audit, or review FHIR instances, profiles, APIs, implementation guides, and behavior-preserving refactors."
---

# FHIR Validation and Review

Establish the [version and IG contract](../fhir-standards/references/releases.md). Match review breadth to the request. For a small bug fix, test the affected requirements; for an audit, use the full [review matrix](references/review-matrix.md).

## Validate with evidence

1. Identify inputs, applicable base/IG/profile packages, terminology versions, declared actor capabilities and expected behavior. Resolve profile inheritance and dependency packages before interpreting validation errors.
2. Select a FHIR-aware validator and pin its version. The HL7 Java validator is a common option; follow [official validator documentation](https://hl7.org/fhir/validator/) for current distribution and arguments. Run its help before assuming flags. Supply explicit FHIR version, IG package versions and required profiles; use locally authorized terminology services/data.
3. Validate syntax, cardinality, datatypes, invariants, slicing, bindings, reference rules and applicable profiles. JSON Schema, a generated type checker, or simply parsing JSON does not prove FHIR conformance. `meta.profile` alone does not select every profile required by context.
4. Separate invalid artifacts from missing dependencies, unsupported terminology, unavailable services, tool defects and narrative requirements that machines cannot check. Report skipped checks and warnings; do not suppress issues merely to obtain a green run.
5. Check runtime behavior separately: capabilities, search semantics, HTTP/OperationOutcome, conditional writes, transaction atomicity and authorization. Include negative cases that exercise the changed contract.
6. For refactoring, compare pre/post serialized output, references, extension preservation, precision, code semantics and externally observable API behavior. Use real project regression fixtures or synthetic examples; avoid transmitting patient data to public validators.

A command shape, after confirming the installed validator's help, is:

```sh
java -jar validator_cli.jar example.json -version 5.0.0 -ig 'package.id#version' -profile 'canonical-profile-url'
```

Replace the illustrative package/profile with the actual contract; omit them only when base-only validation is intended. This is a template, not a validation result or automatic permission to download/run software.

Return tool/package versions, commands actually run, issue paths and severities, evidence-backed findings, and residual uncertainty. Validation success is neither a guarantee of clinical correctness nor legal certification.

## Read

[Validation](https://hl7.org/fhir/R5/validation.html) · [Conformance testing](https://hl7.org/fhir/R5/testing.html) · [Safety](https://hl7.org/fhir/R5/safety.html) · [OperationOutcome](https://hl7.org/fhir/R5/operationoutcome.html) · [TestScript](https://hl7.org/fhir/R5/testscript.html) · [TestReport](https://hl7.org/fhir/R5/testreport.html) · [TestPlan](https://hl7.org/fhir/R5/testplan.html).
