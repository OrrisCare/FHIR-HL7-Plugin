# FHIR by Orris

16 version-aware skills for implementing, reviewing and maintaining HL7 FHIR software, with all R5 module routes and searchable primary-source indexes. R5 is the checked published baseline; existing R4/R4B contracts and explicit R6 preview work have separate guidance.

For the copy-and-paste installation prompt, supported hosts, commands, scope choices and verification steps, see the [repository README](https://github.com/OrrisCare/FHIR-HL7-Plugin) and [installation guide](https://github.com/OrrisCare/FHIR-HL7-Plugin/blob/main/INSTALL.md).

This folder is the native multi-skill plugin, with portable Agent Plugins, Codex, Claude Code and Cursor manifests. Install it as a complete plugin; its skills reference one another. Single-skill importers should use the separate self-contained fhir-suite distribution from the repository releases. No MCP server, credentials or service configuration is needed.

Start with the standards navigator or ask your agent about a FHIR implementation task. Invocation syntax depends on the host. See [coverage and provenance](skills/fhir-standards/references/coverage.md) and [attribution](NOTICE.md). Independent Orris project; no HL7 endorsement or clinical/regulatory certification.
