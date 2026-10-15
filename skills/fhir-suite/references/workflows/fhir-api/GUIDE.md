---
name: fhir-api
description: "Build, debug, audit, or refactor FHIR REST clients and servers, search behavior, operations, conditional requests, and transaction processing."
---

# FHIR APIs and Search

Resolve the [release contract](../fhir-standards/references/releases.md). Read the server's `GET [base]/metadata` CapabilityStatement and applicable IG before assuming support. Resource definitions alone do not mandate every REST interaction or search parameter.

## Implement the interaction

- Match read/vread, create, update, patch, delete, history, and search to the selected specification. Follow its MIME types, HTTP status codes, headers, OperationOutcome and return preferences. Handle resource contention with advertised versioning support and `ETag` / `If-Match`; do not overwrite concurrent updates during a refactor.
- Implement conditional create (`If-None-Exist`) and conditional update/delete using their zero/one/multiple-match rules and declared capabilities. Retrying a create is not automatically idempotent. PUT-as-create and conditional delete are server capabilities, not universal assumptions.
- Read the actual SearchParameter's type, bases, expression, targets, modifiers and comparators. Token `system|code`, date/number ranges, quantities, references, strings and composites have distinct semantics. Repeated parameters and comma-separated values have different AND/OR behavior; also inspect per-parameter multipleAnd/multipleOr support.
- Treat chains, reverse chains, `_include`, `_revinclude`, `_has`, `_filter`, sorting and total modes as capabilities to verify. A FHIRPath is not automatically a search parameter. Do not expose arbitrary internal database field names as standard search parameters.
- Follow returned paging links; do not construct or decode opaque page tokens. Distinguish match, include and outcome entries. Bound include expansion and enforce authorization on every result, history and included resource.
- A transaction is atomic; a batch contains independently processed entries. Respect `fullUrl`, intra-bundle references, request ordering rules, conditional references and per-entry responses. Test failure/rollback behavior for a transaction implementation.
- Resolve `$operation` from its OperationDefinition: system/type/instance scope, parameter types/cardinality, GET eligibility and whether it affects state. Use Parameters or the specified return resource; never infer the whole interface from an operation's name.

Test the behavior changed: empty/multiple matches, escaping, partial dates, stale versions, pagination, denied access, or transaction rollback as applicable. Report protocol errors separately from business validation errors. For Bulk Data or subscriptions use [fhir-exchange](../fhir-exchange/GUIDE.md).

## Authoritative reading

[REST API](https://hl7.org/fhir/R5/http.html) · [Search](https://hl7.org/fhir/R5/search.html) · [Search registry](https://hl7.org/fhir/R5/searchparameter-registry.html) · [Operations framework](https://hl7.org/fhir/R5/operations.html) · [Operation list](https://hl7.org/fhir/R5/operationslist.html) · [CapabilityStatement](https://hl7.org/fhir/R5/capabilitystatement.html) · [OperationOutcome](https://hl7.org/fhir/R5/operationoutcome.html) · [Bundle](https://hl7.org/fhir/R5/bundle.html) · [FHIR Patch](https://hl7.org/fhir/R5/fhirpatch.html).
