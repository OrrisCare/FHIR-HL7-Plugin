---
name: fhir-maintenance
description: "Update this FHIR skills plugin, verify new HL7 releases, refresh documentation indexes and check coverage or stale links."
---

# FHIR Standards Maintenance

Use this workflow when maintaining the plugin itself or assessing its coverage. For application version migration use [fhir-migration](../fhir-migration/SKILL.md).

## Refresh without mixing releases

1. Read [HL7 publication history](https://hl7.org/fhir/directory.html) and its [package-list.json](https://hl7.org/fhir/package-list.json). Confirm publication status using the release home page and package metadata. `current` can describe a CI build; a snapshot named “Stable” can still be a draft. Do not select the numerically highest version as a production default.
2. Compare [coverage/provenance](../fhir-standards/references/coverage.md) and the bundled `indexes/provenance.json` and `indexes/releases.json` with upstream. The repository's `tools/build_indexes.py` regenerates an R5 candidate from fixed official sources. It is a repository maintenance tool, not a runtime requirement of the installed plugin.
3. Generate candidates in an empty temporary directory, compare resource/artifact/page additions and removals, source hashes, package metadata and release status. Review semantic changes before replacing maintained indexes. For a new major version, extend the builder and create a separate versioned index rather than relabeling the R5 catalog.
4. Update the release policy, module routes, affected specialized skills and external IG routes. Verify all official modules and concrete/abstract resources remain reachable. Check newly introduced resources, operations, search parameters, datatypes and artifact maturity.
5. Run the repository validation and lookup tests, check selected authoritative links, and use the behavioral scenarios in `tests/scenarios.md` for an actual agent evaluation if one is available and authorized. Record executed versus unexecuted evaluations honestly.
6. Increment the plugin version, update source/coverage dates and release notes, package from the plugin root, and verify the marketplace path resolves. Publish or push only to destinations authorized by the maintainer.

Broken, redirected, access-restricted and unverified links are different states. Do not report every indexed link as checked merely because the TOC was fetched. Keep HL7 attribution and terminology licensing boundaries intact. When online access fails, use the pinned metadata for discovery and state that the latest status or detailed rule could not be verified.
