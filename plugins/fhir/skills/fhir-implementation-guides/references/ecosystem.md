# Implementation-guide discovery

This is a set of discovery routes, not an exhaustive inventory of every independently published IG. The [FHIR guide registry](https://fhir.org/guides/registry/) and each guide's publication history, table of contents and artifact index provide the continuing coverage mechanism.

| Need | Official starting point | What to pin/check |
| --- | --- | --- |
| App launch, user-facing and backend authorization | [SMART App Launch](https://hl7.org/fhir/smart-app-launch/) | SMART release, flow, FHIR dependencies, discovery/scopes |
| Population export | [Bulk Data Access](https://hl7.org/fhir/uv/bulkdata/) | Published IG version, system/group/patient modes, auth, async/NDJSON contract |
| R4/R4B topic subscriptions | [Subscriptions Backport](https://hl7.org/fhir/uv/subscriptions-backport/) | Supported base releases, extensions and subscription notification format |
| Questionnaires, extraction and population | [Structured Data Capture](https://hl7.org/fhir/uv/sdc/) | Published canonical destination (follow redirects), questionnaire profile, expression/extraction rules |
| International patient summary | [IPS](https://hl7.org/fhir/uv/ips/) | Published version, Composition/Bundle profiles and section requirements |
| International patient access | [IPA](https://hl7.org/fhir/uv/ipa/) | Actor/API requirements and base dependencies |
| US clinical exchange | [US Core](https://hl7.org/fhir/us/core/) | Exact US Core version and FHIR dependency, MustSupport actor rules, required searches |
| US payer and patient access | [Registry](https://fhir.org/guides/registry/) → Da Vinci / CARIN guides | Use-case-specific IG, payer/regulatory agreement and adopted version |
| Genomics, oncology and public health | [Registry](https://fhir.org/guides/registry/) → relevant domain | Domain-specific profiles/terminology and publication maturity |
| India and other national programs | [Registry](https://fhir.org/guides/registry/) → jurisdiction/publisher | Official national authority, mandated release/profiles; do not assume US Core applies |
| CQL and quality/decision support | [CQL](https://cql.hl7.org/), [CDS Hooks](https://cds-hooks.org/), registry | Language/modelinfo/ELM and guide versions separate from FHIR |
| Shared terminology | [HL7 Terminology](https://terminology.hl7.org/) | Package release and external terminology editions/licensing |
| Extensions | [Extension registry](https://hl7.org/fhir/extensions/extension-registry.html) | Extension pack version, supported FHIR releases, context and canonical |
| FSH authoring | [FHIR Shorthand](https://hl7.org/fhir/uv/shorthand/) | Grammar/tool compatibility and generated artifact validation |
| Publisher/package maintenance | [IG tooling guidance](https://build.fhir.org/ig/FHIR/ig-guidance/) | This is tooling guidance on the build site; distinguish it from normative published clinical IGs |
| v2/CDA transformations, IHE, DICOM and other ecosystems | [Registry](https://fhir.org/guides/registry/), links from relevant core module | Source and destination standard versions, mappings and local agreements |

For a chosen guide, read: home/status → publication history → package metadata/dependencies → actor/conformance requirements → TOC → artifact index → affected profiles/operations/terminology → examples → QA/known issues. A functioning URL may be a redirect page or CI build; verify the final destination and publication status. Do not use the rolling home URL as a reproducible release pin.
