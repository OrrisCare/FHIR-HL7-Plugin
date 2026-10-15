---
name: fhir-workflow
description: "Implement or review FHIR requests, events, Task orchestration, scheduling, care plans, fulfillment and workflow state transitions."
---

# FHIR Orders and Workflow

Resolve the [release and workflow IG](../fhir-standards/references/releases.md). Read the [workflow module](https://hl7.org/fhir/R5/workflow-module.html), [workflow overview](https://hl7.org/fhir/R5/workflow.html), and linked communication/management patterns before choosing a coordination mechanism.

## Implement the lifecycle

1. Distinguish a reusable Definition, an authorized/planned Request, and the Event that actually occurred. Resource patterns describe common semantics; they are not interchangeable concrete resource types.
2. Keep clinical request status/intent separate from Task execution status and businessStatus. Task can track fulfillment; it does not itself replace the clinical order. Map each state transition to the permitted actor and resource, with concurrency and cancellation handling.
3. Preserve `basedOn`, `partOf`, `replaces`, supporting information, focus and subject according to each resource's definition. Do not infer relationships merely because two entries share a patient or timestamp.
4. For PlanDefinition/ActivityDefinition and RequestOrchestration, distinguish reusable definitions from patient-specific requests and evaluated actions. R4 RequestGroup and R5 RequestOrchestration require explicit version-aware handling.
5. For appointments, keep Schedule availability, Slot availability and Appointment booking/participant responses distinct. Model rescheduling, cancellations, timezones and race conditions according to the actual service contract; a free slot read does not reserve it.
6. Select direct REST, Task, messaging or operations based on the documented workflow agreement and capabilities. Delivery success alone is not proof of clinical acceptance or completed fulfillment.

Test transitions, rejected transitions, duplicate requests, cancellation, stale updates and failed downstream fulfillment relevant to the change. Preserve existing lifecycle behavior in refactors.

## Read by resource

[Task](https://hl7.org/fhir/R5/task.html) · [ServiceRequest](https://hl7.org/fhir/R5/servicerequest.html) · [CarePlan](https://hl7.org/fhir/R5/careplan.html) · [RequestOrchestration](https://hl7.org/fhir/R5/requestorchestration.html) · [Appointment](https://hl7.org/fhir/R5/appointment.html) · [AppointmentResponse](https://hl7.org/fhir/R5/appointmentresponse.html) · [Schedule](https://hl7.org/fhir/R5/schedule.html) · [Slot](https://hl7.org/fhir/R5/slot.html). Use the [catalog](../fhir-standards/references/resources.md) for supply, transport, device and nutrition workflows.
