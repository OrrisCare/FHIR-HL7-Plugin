# Validation record — 2026-10-15

Executed against plugin version 1.0.0:

- Official Agent Plugins 1.0.0 JSON schema validation: passed.
- Skill Creator `quick_validate.py`: all 16 skills passed.
- Repository validation: manifests, marketplace source resolution, matching compatibility metadata, UI fields/assets, all internal Markdown links and R5 index invariants passed.
- Seven unit tests: passed. Covers exact-result ranking, real SearchParameter lookup, no-match/empty queries, invalid limits, case-insensitive multi-term matching, TOC URL deduplication/scope, canonical preservation and rejection of a mismatched core release.
- Checked 111 distinct external URLs extracted from the authored skill/reference Markdown (excluding the generated resource catalog). One obsolete `artifacts.html` link returned 404; replaced it with the official downloads page and verified HTTP 200. These checks establish reachability, not correctness of every linked statement.
- Core snapshot: 162 resource definitions (158 concrete, 4 abstract), 2,968 package artifacts, 3,173 unique TOC-document HTML targets. Counts and source hashes are recorded in the packaged provenance file.

Not claimed: live validation of all 3,173 indexed pages, a manual reading of every page, a full mirror of all implementation guides, clinical/regulatory certification, or an independent agent execution of the scenarios in `tests/scenarios.md`.

The original GitHub repository's MIT license is preserved. No clinical records, credentials, research downloads, virtual environments or execution logs are included in the plugin ZIP.

## Version 1.1.0 — cross-agent distribution

Executed on 2026-10-15:

- Claude Code native validator: plugin and marketplace manifests passed without warnings.
- Repository checks: portable/Codex/Claude/Cursor identity, version and source paths, original local links and every generated bundle link passed.
- Distribution parity: generated host manifests and all self-contained workflow/reference files match the canonical source.
- Thirteen unit tests passed, including six installer tests: dry-run, all-skill installation/idempotency, preflight conflict handling, one-skill completeness and installed lookup execution, rollback on copy failure, and refusal to overwrite symlink targets.
- Both the native plugin ZIP and the self-contained skill ZIP were built and checked for integrity and required entrypoints.

Native installation/selection has not been tested end-to-end in Cursor, Hermes, OpenClaw, Claude.ai or a plain ChatGPT web chat. Their routes are based on official documentation and inspected CLI help. The Claude Code result above is manifest validation, not an agent behavioral evaluation. Public Anthropic/Cursor/ClawHub listings have not been submitted or claimed.
