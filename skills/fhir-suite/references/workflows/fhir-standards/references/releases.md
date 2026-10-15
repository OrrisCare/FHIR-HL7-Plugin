# Select and pin the FHIR contract

Verified against [HL7 publication history](https://hl7.org/fhir/directory.html), [machine-readable history](https://hl7.org/fhir/package-list.json), the release home pages and R5 package metadata on **2026-10-15**.

| Track | Version | Use |
| --- | --- | --- |
| Current published release | [R5 / 5.0.0](https://hl7.org/fhir/R5/) | Default for new work without an existing version constraint, after checking history for updates |
| Newer preview | [R6 / 6.0.0-snapshot1](https://hl7.org/fhir/6.0.0-snapshot1/) | History describes “FHIR R6 Stable (Sept 2026)” but marks it **draft**; opt-in preview only |
| Existing ecosystem | [R4B / 4.3.0](https://hl7.org/fhir/R4B/) | Use when required by an existing implementation or IG |
| Existing ecosystem | [R4 / 4.0.1](https://hl7.org/fhir/R4/) | Use when required by an existing implementation or IG |
| Development | [Continuous build](https://build.fhir.org/) | Unstable development evidence, never silently substituted for a published release |

The R5 release is designated STU overall, while individual resources/pages can be Normative, Trial Use, Draft or Informative. Read each artifact's standards status and maturity. “Latest published release” does not mean every artifact is normative. The history also lists R6 ballots; neither their numbering nor a `current` marker on the CI entry establishes production status.

## Decision sequence

1. Inspect project package locks, `fhirVersion`, IG/SUSHI configuration, generated models and tests. Read the target server CapabilityStatement's `fhirVersion` and supported profiles/interactions.
2. Identify actor, jurisdiction and required IGs. Pin each package as `package.id#version`, plus its dependencies. For example, an IG whose own version is `9.0.0` may still depend on FHIR R4.
3. If these sources conflict, explain the conflict and resolve it before producing incompatible wire data. Do independent work while awaiting any essential choice.
4. For a genuinely new unconstrained project, recheck HL7 history. If unavailable, explicitly use this checked R5 baseline and disclose that “latest” could not be reverified.
5. Treat R6 implementation as a separately identified preview contract. Use that exact snapshot's definitions, packages and documentation. The bundled offline indexes are **R5 only**; they do not prove R6 resource or field availability.

## Keep these versions distinct

- FHIR specification version (`5.0.0`).
- IG/package business version and dependencies.
- Canonical artifact `url` plus its optional business `version` (`url|version` references).
- Resource instance `meta.versionId` and REST history version.
- Terminology system edition/version, expansion parameters and expression language version.

All R5 links in the skills are explicit baseline references. For R4/R4B/R6 work, navigate the selected release's own TOC and verify the page/field there; do not blindly replace URL path segments or reuse R5 code. Canonical `http://hl7.org/fhir/...` identifiers remain exactly as specified even when documentation is fetched over HTTPS.

If sources disagree, inspect the selected release's errata, normative narrative, definitions and IG actor requirements and disclose the discrepancy. Machine-readable schemas and examples are not automatically more authoritative than narrative constraints. See [version policy](https://hl7.org/fhir/R5/versions.html) and [version management](https://hl7.org/fhir/R5/versioning.html).
