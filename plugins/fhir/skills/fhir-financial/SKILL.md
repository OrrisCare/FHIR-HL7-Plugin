---
name: fhir-financial
description: "Model, build, debug, or review FHIR coverage, eligibility, claims, adjudication, explanations of benefit, billing and payments data."
---

# FHIR Financial Workflows

Resolve the [FHIR release, jurisdiction and payer IG](../fhir-standards/references/releases.md). Financial workflows depend on local rules and payer agreements; base FHIR does not define universal reimbursement or insurance-eligibility decisions.

Read the [financial module](https://hl7.org/fhir/R5/financial-module.html), then the selected resources' scope and definitions:

- Coverage and InsurancePlan describe different aspects of insurance; CoverageEligibilityRequest/Response support eligibility exchanges. An eligibility response is not a guarantee of payment.
- Claim describes a claim, preauthorization or predetermination according to its `use`; ClaimResponse represents adjudication. ExplanationOfBenefit combines claim/adjudication information for reporting and is not a universal replacement for either transactional resource.
- Account, ChargeItem, ChargeItemDefinition and Invoice serve accounting, charge and invoice purposes. Preserve currency, decimal values, quantity/unit-price semantics, timing and rounding policies without converting money into unitless numbers.
- PaymentNotice and PaymentReconciliation are distinct payment information artifacts. EnrollmentRequest/Response and Contract have their own boundaries and maturity.

Map actors, identifiers, coverage order, beneficiaries, providers, servicing context, line/item sequences and adjudication categories from the selected IG. Preserve references between requests and responses, and distinguish submitted, accepted, adjudicated and paid states. Do not infer a successful business outcome from a successful HTTP response.

For implementation or refactoring, test totals, line-level associations, currencies, negative/adjustment cases, duplicate processing, versioned codes and unauthorized access as applicable. Keep financial/health data out of public test endpoints. Cite the FHIR/IG requirement for findings and identify business rules that need payer confirmation.

Use the [resource index](../fhir-standards/references/resources.md), [terminology skill](../fhir-terminology/SKILL.md) and [validation skill](../fhir-validation/SKILL.md) for the actual artifacts. Discover Da Vinci, CARIN and national guides through [the IG registry](https://fhir.org/guides/registry/) and pin a published compatible version.
