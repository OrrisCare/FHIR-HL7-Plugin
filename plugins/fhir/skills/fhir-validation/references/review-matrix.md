# Evidence-oriented FHIR review matrix

Select rows appropriate to the requested audit or change. Record each as checked, not applicable, blocked or not checked. Attach exact release/IG citations and file/element/request evidence to findings.

| Area | Questions and meaningful evidence |
| --- | --- |
| Contract | Are FHIR, IG, terminology and tool versions pinned and compatible? Do runtime capabilities match declared actors/profiles? |
| Structure | Correct resource/type, cardinality, choice fields, primitive extensions, invariants, modifier handling and element inheritance? |
| Profiles | Correct canonical/version, inheritance, slices, target profiles, fixed/pattern values, binding constraints and actor-specific MustSupport? |
| Semantics | Preserved status/intent, identifiers, references, temporal/decimal precision, absent-data meaning, units and narrative? |
| Terminology | Correct systems/versions, binding strength, expansion completeness, mapping direction and handling of unavailable terminology? |
| REST/search | Correct status/headers, supported parameter semantics, escaping, paging, includes, error results, conditional match cases and concurrency? |
| Operations | Correct scope and parameters, state-changing behavior, declared support, authorization and OperationOutcome handling? |
| Bundles | Correct type/envelope, first entry where required, identities, reference closure, transaction atomicity and per-entry outcomes? |
| Workflow | Correct actors, transitions, request/event separation, cancellation, duplicate handling and fulfillment state? |
| Security/privacy | Correct enforcement on read/search/include/history/export/notifications, tenant isolation, consent/labels, safe narratives/attachments, no token/payload leakage? |
| Domain | Relevant clinical, diagnostic, medication, administrative or financial semantics preserved? Specialized IG requirements applied? |
| Migration/refactor | Observable compatibility, loss analysis, reference rewrites, extension/precision preservation and rollback where required? |
| Tools | Actual validator/terminology dependencies loaded? All required checks completed? Warnings/errors distinguished from infrastructure failures? |
| Documentation | Do narrative requirements, advertised capabilities, generated definitions and actual behavior agree? |

Finding format: severity → concrete issue → evidence → exact requirement/source → consequence → smallest appropriate repair → verification. Do not label a recommendation as a SHALL violation. Report “not verified” when a dependency or source is unavailable; do not turn uncertainty into a passing result.
