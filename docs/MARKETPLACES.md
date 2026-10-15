# Distribution and marketplace publication

Checked against the official sources below on **2026-10-15**. Supporting a package format, installing from Git, and being listed in a vendor's public catalog are separate outcomes.

| Host/channel | Included in this repository | What Orris must do for wider distribution |
| --- | --- | --- |
| Codex Git marketplace | `.agents/plugins/marketplace.json`, portable and Codex manifests; installed and verified locally | Share the repository URL. Public OpenAI directory submission remains a separate optional process, deferred here. |
| Claude Code Git marketplace | `.claude-plugin/marketplace.json` and plugin manifest | Share the two `/plugin` commands. For Anthropic's curated directory, submit the public repository through its [directory submission form](https://clau.de/plugin-directory-submission) and address review feedback. |
| Cursor local/team | `.cursor-plugin/marketplace.json`, Cursor manifest and portable manifest; direct skill copies supported | Use local skills immediately. A team admin can import the repo into its team marketplace on an eligible plan. For the public catalog submit at [Cursor Marketplace Publish](https://cursor.com/marketplace/publish); Cursor reviews listings. |
| Hermes GitHub/Hub tap | Root `skills/fhir-suite` contains a self-contained Agent Skill | Share the direct GitHub install command or tap URL. No registry account is needed for that GitHub route. Inclusion in other curated sources is separate. |
| OpenClaw local skill | Self-contained `skills/fhir-suite`, compatible with local installation | Share the local install route now. For public ClawHub discovery, publish the bundle under an actual Orris publisher account and verify its listing/scan state. |
| Claude.ai/custom-skill import | Buildable self-contained skill ZIP | Users import through their plan/workspace's supported Skills interface. Claude Code plugin registration is not the same as Claude.ai skill upload. |
| ChatGPT and other agents | Portable plugin, Agent Skill bundle, capability-aware installation prompt | Use the product's supported importer or filesystem workflow. A plain web chat cannot install persistent capabilities without an import/management interface. |

## Release preparation

The canonical content lives in `plugins/fhir/skills/`. `tools/sync_distribution.py` produces host manifests and the one-skill bundle, preserving every local reference. Nested workflows become `GUIDE.md` files so a recursive host scanner does not mistake them for separate installed skills. `--check` detects stale generated copies.

```sh
python3 tools/sync_distribution.py --check
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/package.py dist/fhir-1.1.0.zip
python3 tools/package_suite.py dist/fhir-suite-1.1.0.zip
```

The repository already uses MIT for Orris content and includes HL7 attribution, an original icon, publisher details and a public source URL. Before submitting to a curated catalog, test its native install in a clean environment, choose the publishing account/owner, and supply whatever description, support contact and demonstration the actual submission form requires. Keep names/versions consistent, resolve scan findings, and distinguish “submitted” from “approved/listed.” Do not claim an endorsement from HL7 or the host vendor.

## ClawHub publication

The bundle, rather than an isolated specialized workflow, is the publication unit. With the official ClawHub CLI and an authorized Orris publisher account:

```sh
clawhub login
clawhub skill publish ./skills/fhir-suite --dry-run
clawhub skill publish ./skills/fhir-suite --version 1.1.0
```

Check the installed CLI's help first. If publishing for an organization, select its real publisher handle with the supported `--owner` option; no handle has been reserved by this repository. Review the result and security-scan state, then document the actual owner-qualified installation reference. Do not run `sync --all`, which could publish unrelated local skills. This repository does not claim a ClawHub listing or provide an unverified install badge.

## Compatibility evidence and limits

Version 1.1.0 adds host-specific manifests and the generated portable skill. Local automated checks cover manifest paths, version consistency, generated-content parity, link integrity, installer conflict handling and installed file/lookup behavior. Claude Code's native manifest validator is available for additional checks. These are not a claim that every named application version or cloud surface has completed an end-to-end agent evaluation.

The original 16-skill form relies on sibling files inside the same plugin/skill root. Use the complete bundle for single-skill registries; publishing or importing only `fhir-standards` would omit referenced workflows. Install one form per scope to avoid duplicate skill selection.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) and [Agent Plugins](https://agent-plugins.org/).
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) and [public submission](https://developers.openai.com/plugins/deploy/submission).
- [Anthropic official marketplace README and submission link](https://github.com/anthropics/claude-plugins-official), [official skills installation guide](https://github.com/anthropics/skills), [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins). The official GitHub sources were used where direct documentation fetching returned 403.
- [Cursor skills](https://cursor.com/docs/skills), [plugin distribution](https://cursor.com/docs/plugins), [manifest/submission reference](https://cursor.com/docs/reference/plugins), [official marketplace examples](https://github.com/cursor/plugins).
- [Hermes skills, direct installs and custom taps](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).
- [OpenClaw skill loading and installation source](https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md), [ClawHub](https://github.com/openclaw/clawhub), [ClawHub CLI/publishing reference](https://github.com/openclaw/clawhub/blob/main/docs/cli.md).
