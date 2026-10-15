# FHIR by Orris

An independent, version-aware HL7 FHIR reference plugin for coding agents. It helps agents build, edit, validate, audit and refactor FHIR software by selecting the correct contract and reading authoritative documentation on demand.

**16 skills · all 14 R5 modules · 158 concrete resource types · 4 abstract resource definitions · 2,968 core artifacts · 3,173 documentation links.**

The baseline was checked on **October 15, 2026**: **R5 / 5.0.0** is HL7's current published release. **R6 / 6.0.0-snapshot1** is newer preview content, still marked draft in HL7's publication history. Existing R4/R4B projects retain their required contracts.

## Install with one prompt

Copy this into your agent:

```text
Install FHIR by Orris from https://github.com/OrrisCare/FHIR-HL7-Plugin.
Read https://raw.githubusercontent.com/OrrisCare/FHIR-HL7-Plugin/main/INSTALL.md
and follow the route for this agent and its actual capabilities. Use the
native plugin manager when supported; otherwise install the complete skill
set or the self-contained fhir-suite bundle into the appropriate skill
folder. Confirm the target if you cannot determine it. Preserve existing
skills and settings, inspect any installer before running it, and verify
the result. Report the installed version, scope, and any reload step.
If this chat cannot install persistent skills, give me the supported import
steps instead of claiming it is installed. This package has no MCP server.
```

Download version 1.1.0: [native plugin ZIP](https://github.com/OrrisCare/FHIR-HL7-Plugin/releases/download/v1.1.0/fhir-1.1.0.zip) · [self-contained skill ZIP](https://github.com/OrrisCare/FHIR-HL7-Plugin/releases/download/v1.1.0/fhir-suite-1.1.0.zip).

An agent with the required filesystem/plugin tools can carry out the installation. A plain web chat may need a supported skill/ZIP importer or a manual step. See [INSTALL.md](INSTALL.md) for the complete agent-readable procedure.

| Agent | Easiest supported route |
| --- | --- |
| Codex | Git marketplace; commands below |
| Claude Code | `/plugin marketplace add OrrisCare/FHIR-HL7-Plugin`, then `/plugin install fhir@orris-fhir` |
| Cursor | Copy all skills into `.cursor/skills`, or import the repository through a team marketplace |
| Hermes | `hermes skills install OrrisCare/FHIR-HL7-Plugin/skills/fhir-suite` |
| OpenClaw | Clone the repo, then `openclaw skills install ./skills/fhir-suite` from the checkout |
| Claude.ai / other custom-skill importers | Import the self-contained `fhir-suite` ZIP using the product's supported interface |
| Other Agent Skills hosts | Use the copy helper with a confirmed skills directory; see INSTALL.md |

The native plugin exposes **16 skills**. The self-contained distribution exposes **one skill with all 16 workflows and references inside it**, so single-skill installers do not lose dependencies. Choose one distribution per scope.

### Manual skill installation

From a clone of this repository, use Python 3.10+ and an explicit destination:

```sh
python3 tools/install_skills.py --dest /absolute/path/to/project/.cursor/skills --dry-run
python3 tools/install_skills.py --dest /absolute/path/to/project/.cursor/skills
```

Add `--bundle` for the single-skill form. The helper makes no network calls, checks every collision before copying, preserves unrelated files, and refuses to overwrite a differing installation. For updates, use the native manager or stage/compare/back up a manual installation as described in INSTALL.md.

**Marketplace availability:** this repository is usable as a Codex/Claude Code Git marketplace and a Cursor team marketplace, and as a Hermes GitHub skill source. Curated public listings require separate submission/approval; none is implied by these manifests. See [marketplace publication steps](docs/MARKETPLACES.md).

## Install in Codex

In **Plugins → Add → Add plugin marketplace**, enter:

```text
https://github.com/OrrisCare/FHIR-HL7-Plugin.git
```

Use Git ref `main` and leave sparse paths empty. Open **Orris FHIR Standards**, install **FHIR by Orris**, then start a new chat. This is a Git-backed marketplace; it does not require the OpenAI Platform submission portal.

Alternatively, register the marketplace from the CLI:

```sh
codex plugin marketplace add https://github.com/OrrisCare/FHIR-HL7-Plugin.git --ref main
codex plugin add fhir@orris-fhir
```

For a local checkout, use `codex plugin marketplace add /absolute/path/to/FHIR-HL7-Plugin`. Registration makes the source discoverable; install through the app or the `plugin add` command. If the source does not appear immediately, refresh the plugin list or restart the app.

## Use

Ask naturally about a FHIR task or explicitly invoke `$fhir-standards`. Focused skills can be selected directly.

| Skill | Use |
| --- | --- |
| `fhir-standards` | Release selection and complete documentation navigation |
| `fhir-modeling` | Resources, datatypes, serialization and references |
| `fhir-api` | REST, search, operations and transactions |
| `fhir-conformance` | Profiles, extensions, slicing and FSH |
| `fhir-terminology` | Codes, value sets, bindings and mappings |
| `fhir-validation` | Validation, tests, audits and refactor review |
| `fhir-security` | SMART, access control, consent and audit |
| `fhir-exchange` | Documents, messages, subscriptions and Bulk Data |
| `fhir-administration` | Identity, providers, organizations and encounters |
| `fhir-clinical` | Clinical records, diagnostics, medications and products |
| `fhir-workflow` | Orders, Task, scheduling and orchestration |
| `fhir-financial` | Coverage, claims, billing and payment data |
| `fhir-clinical-reasoning` | CDS, CQL, measures, evidence and research |
| `fhir-implementation-guides` | Discover and author compatible IGs |
| `fhir-migration` | Version conversion and source-data mappings |
| `fhir-maintenance` | Refresh and verify this plugin's coverage |

Examples: “Review our FHIR transaction handling”; “Create a profile for our published IG”; “Find the correct medicinal-product resources”; “Refactor this R4 serializer without changing wire behavior.”

## Design and scope

Each skill contains actionable workflow guidance and links to versioned primary sources. A shared module/resource map supplies full core navigation; larger machine-readable indexes load only when searched. A Python 3.10+ helper can search the indexes offline, but Python is optional for reading the skills and following documentation links. There are no MCP servers, hooks, credentials, telemetry or runtime service dependencies. Native skill invocation syntax varies by host; the `$fhir-standards` example above is for Codex. In the self-contained distribution, select `fhir-suite`.

The indexes cover the official R5 TOC document's HTML targets and every entry in the R5 core package index. This is not a copy or manual review of every specification page. External guides and terminology releases are discovered through their official registries and pinned per task. R4/R4B/R6 full catalogs are not bundled. See [coverage and provenance](plugins/fhir/skills/fhir-standards/references/coverage.md).

FHIR compliance is broader than schema validation. The skills distinguish computable constraints, narrative/actor obligations, actual server behavior and clinical meaning. They do not provide clinical or regulatory certification.

## Validate and maintain

From the repository root:

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/sync_distribution.py --check
python3 tools/package.py dist/fhir-1.1.0.zip
python3 tools/package_suite.py dist/fhir-suite-1.1.0.zip
python3 plugins/fhir/skills/fhir-standards/scripts/lookup.py Observation --kind resources
python3 tools/build_indexes.py --out /tmp/fhir-r5-candidate
```

Use an empty output directory for candidate indexes. Compare changes before replacing the checked snapshot. The index builder reads official sources, verifies `hl7.fhir.r5.core#5.0.0`, records source hashes and never extracts archive files onto disk. See [agent evaluation scenarios](tests/scenarios.md) for behavioral checks beyond static validation.

`plugins/fhir/plugin.json` is the portable Agent Plugins manifest. `.codex-plugin/plugin.json` is a matching compatibility manifest for Codex clients. `.agents/plugins/marketplace.json` exposes the plugin from this repository. The ZIP contains the plugin itself with its manifest at the archive root.

## License and attribution

Original instructions and code: MIT, © 2026 Orris Care, Inc. Core metadata/descriptions: HL7 FHIR R5 package, CC0-1.0 according to its package metadata. HL7 and FHIR are trademarks of HL7 International. This project is not affiliated with or endorsed by HL7. External code systems and guide content retain their own licensing terms. See [NOTICE](plugins/fhir/NOTICE.md).
