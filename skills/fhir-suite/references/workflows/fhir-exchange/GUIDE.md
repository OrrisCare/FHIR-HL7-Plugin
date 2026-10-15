---
name: fhir-exchange
description: "Build or debug FHIR documents, messaging, subscriptions, Bulk Data, asynchronous exchange and cross-system interoperability."
---

# FHIR Exchange Workflows

Select the [release and IG](../fhir-standards/references/releases.md), then the exchange pattern. Read only the relevant route below and the operation/resource definitions it links. For ordinary REST use [fhir-api](../fhir-api/GUIDE.md).

## Choose the pattern

- **Documents:** a document Bundle has Composition first and the required identifiers/timestamps and referenced content. Composition describes a coherent clinical document; DocumentReference indexes or points to a document and is not interchangeable with it. Preserve document immutability, attestation, signatures and reference closure required by the contract. Read [documents](https://hl7.org/fhir/R5/documents.html), [Composition](https://hl7.org/fhir/R5/composition.html), [DocumentReference](https://hl7.org/fhir/R5/documentreference.html), and [Bundle](https://hl7.org/fhir/R5/bundle.html).
- **Messaging:** use a message Bundle with MessageHeader first. Resolve event, destination, response and reliable-processing requirements from the MessageDefinition/IG. Do not treat a message Bundle as a transaction. Read [messaging](https://hl7.org/fhir/R5/messaging.html), [MessageHeader](https://hl7.org/fhir/R5/messageheader.html), and [MessageDefinition](https://hl7.org/fhir/R5/messagedefinition.html).
- **Subscriptions:** R5 topic-based subscriptions use SubscriptionTopic, Subscription and SubscriptionStatus; inspect advertised topics, allowed filters, notification bundle/content rules, handshake, heartbeat and recovery behavior. R4 criteria-based subscriptions differ. For compatible earlier releases use the published [Subscriptions Backport IG](https://hl7.org/fhir/uv/subscriptions-backport/) rather than copying R5 fields. Read [R5 subscriptions](https://hl7.org/fhir/R5/subscriptions.html) and its linked operations. Design deduplication and gap recovery against the chosen protocol; do not promise exactly-once delivery without supporting evidence.
- **Bulk Data:** select the published [Bulk Data Access IG](https://hl7.org/fhir/uv/bulkdata/), its FHIR dependencies and [SMART authorization](https://hl7.org/fhir/smart-app-launch/). Implement the supported system/patient/group export mode, async kickoff and status polling, NDJSON output, errors, cancellation, expiration and download authorization as specified. Limit memory use and preserve resumability without inventing guarantees about incremental export/deletions.
- **Other exchange:** use the [exchange module](https://hl7.org/fhir/R5/exchange-module.html) for services, persistence, SQL, GraphQL, CDS Hooks and related patterns. FHIRcast synchronizes application context and is a separate specification from subscriptions. Follow linked official specifications and pin them separately.

Validate envelope rules, reference identities, failures/retries, duplicates, partial results and access controls relevant to the chosen pattern. Use synthetic payloads for interoperability tests. Record capabilities and external IG versions with the result.
