---
name: fhir-security
description: "Implement or review security for FHIR systems, SMART authorization, consent enforcement, security labels, AuditEvent and Provenance."
---

# FHIR Security and SMART

Read the selected [release and implementation-guide contract](../fhir-standards/references/releases.md). FHIR specifies data/exchange models; deploying a FHIR endpoint alone does not supply authentication, authorization or regulatory compliance.

## Build or review the relevant controls

- For SMART, choose the published SMART App Launch version and the correct flow: EHR launch, standalone launch or backend services. Inspect discovery metadata, OAuth endpoints, scopes, PKCE requirements, launch context, redirect URI rules, token audience and lifecycle in that version. SMART versions are independent of FHIR versions.
- Enforce access per authenticated principal, tenant, patient and purpose across direct reads, search, includes, history, operations, bundles, export files and subscription notifications. OAuth scope is one input to policy, not proof of unrestricted access. A patient compartment is not an authorization boundary by itself.
- Consent is a representation of directives; an enforcement service must interpret its actors, scope, purpose, time and exceptions. Security labels carry handling requirements; labels do not enforce themselves. Use the jurisdiction's actual policy, not invented universal HIPAA/GDPR rules.
- Distinguish Provenance (origin and transformations of data) from AuditEvent (security/privacy-relevant activity). Capture useful actors and outcomes without leaking tokens or unnecessary clinical payloads into logs. Review integrity and retention requirements appropriate to the system.
- Protect transport and token storage. Treat external references, Attachment URLs, subscription endpoints and terminology URLs as network inputs: prevent SSRF and credential forwarding; authorize destinations and downloaded content. Sanitize XHTML narrative and render attachments safely.
- For signatures, verify the specified canonicalization, signed content, trust chain and intended use. An attached signature blob is not evidence that verification succeeded. Avoid changing signed content during an unrelated refactor.
- Use synthetic/redacted fixtures when contacting public test services. Read-only package/index helpers do not authorize sending clinical data externally.

For a review, report an exploitable path or concrete missing control with evidence, actor, impact and repair, rather than listing generic security advice. For implementation, verify denied as well as allowed access for the changed paths.

## Read

[Security module](https://hl7.org/fhir/R5/secpriv-module.html) · [Security](https://hl7.org/fhir/R5/security.html) · [Security labels](https://hl7.org/fhir/R5/security-labels.html) · [Consent](https://hl7.org/fhir/R5/consent.html) · [Permission](https://hl7.org/fhir/R5/permission.html) · [AuditEvent](https://hl7.org/fhir/R5/auditevent.html) · [Provenance](https://hl7.org/fhir/R5/provenance.html) · [SMART App Launch](https://hl7.org/fhir/smart-app-launch/).
