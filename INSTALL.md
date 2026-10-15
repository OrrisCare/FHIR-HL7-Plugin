# Agent installation instructions

Use this file when the user asks to install FHIR by Orris from `https://github.com/OrrisCare/FHIR-HL7-Plugin`. The package contains skills, references and one optional offline Python lookup helper. It has **no MCP server**, API key, daemon or required service account.

## Establish the installation target

Identify the actual host/product, its installed version, its filesystem or plugin-management capabilities, and the requested scope. Do not infer the host just from the model name. Use the current project for a manual skill copy unless the user requests a user-wide install or a native plugin manager uses its documented default. Ask one short question if the host or destination cannot be determined.

Use an existing clean checkout or clone this repository to a user-approved project/cache location. Read `README.md`, the applicable host section below, and `tools/install_skills.py` before running the helper. Record the checked-out commit or release tag. Do not reset an existing checkout or overwrite unrelated files. Native managers may track `main`; state that when reporting the install.

Choose **one** distribution:

- **Native plugin:** all 16 skills, for Codex, Claude Code or Cursor plugin workflows.
- **Individual skills:** copy all 16 sibling directories intact into one skill root.
- **Self-contained skill:** `skills/fhir-suite`, one skill containing the 16 workflows as reference guides. Use this for Hermes Hub, ClawHub and single-skill upload/import surfaces.

The specialized skills reference each other. Do not install one directory from `plugins/fhir/skills` alone. Do not flatten folders or discard references/scripts/indexes. Prefer the self-contained form when a platform copies one skill at a time. Avoid installing both forms in the same scope.

## Codex

Use the native Git marketplace where these commands are supported:

```sh
codex plugin marketplace add https://github.com/OrrisCare/FHIR-HL7-Plugin.git --ref main
codex plugin add fhir@orris-fhir
codex plugin list --marketplace orris-fhir --json
```

If already registered/installed, inspect the existing state first; use the manager's supported update flow rather than adding duplicates. The app route is **Plugins → Add → Add plugin marketplace**, repository URL, ref `main`, no sparse paths. Install **FHIR by Orris** from **Orris FHIR Standards**. Start a new chat afterward.

## Claude Code

Inside Claude Code:

```text
/plugin marketplace add OrrisCare/FHIR-HL7-Plugin
/plugin install fhir@orris-fhir
```

Use `/plugin` to inspect the installed entry. The CLI equivalents are `claude plugin marketplace add OrrisCare/FHIR-HL7-Plugin` and `claude plugin install fhir@orris-fhir`; inspect `--help` for scope options in the installed version. Start a new session and ask for the FHIR standards navigator. Plugin skills may use the namespace `fhir:fhir-standards`.

## Cursor

For direct local skills, run the helper from this checkout after confirming the project root:

```sh
python3 tools/install_skills.py --dest /absolute/path/to/project/.cursor/skills --dry-run
python3 tools/install_skills.py --dest /absolute/path/to/project/.cursor/skills
```

For a requested user-wide install, the target is `~/.cursor/skills`. Inspect **Customize → Skills**, then test a new agent chat. Local personal skills do not automatically become available to cloud/remote agents; use Cursor's documented sync or project distribution workflow.

For a team plugin marketplace, use **Dashboard → Plugins & MCPs → Team Marketplaces → Add Marketplace → Import from Repo**, supply this GitHub repository, then review/access/install it through the dashboard. Team marketplace availability depends on the team's plan and permissions. `.cursor-plugin/marketplace.json` and the native plugin manifest are included. Public Cursor Marketplace listing is a separate reviewed submission.

## Hermes Agent

Install the complete self-contained skill through the existing Hub workflow:

```sh
hermes skills inspect OrrisCare/FHIR-HL7-Plugin/skills/fhir-suite
hermes skills install OrrisCare/FHIR-HL7-Plugin/skills/fhir-suite
hermes skills list
```

Retain the Hub's normal scan/confirmation behavior. The repository can also be subscribed to as a tap with `hermes skills tap add OrrisCare/FHIR-HL7-Plugin`; its root `skills/` exposes `fhir-suite` as one complete installation unit.

For a manual install, select the active profile's actual skill root (`~/.hermes/skills` by default), then use `python3 tools/install_skills.py --bundle --dest /confirmed/profile/skills`. Do not assume a custom Hermes profile uses the default directory. Reload skills or start a new conversation as supported by that version.

## OpenClaw

From this checkout, where supported by the installed CLI:

```sh
openclaw skills install ./skills/fhir-suite
openclaw skills info fhir-suite
```

This targets the active workspace; inspect `openclaw skills install --help` before choosing an agent/global scope. The Git installer expects `SKILL.md` at the source root, so do not pass the repository root as though it were a single skill.

For a manual install use `python3 tools/install_skills.py --bundle --dest /confirmed/openclaw-workspace/skills`. A requested shared installation uses the active state directory's `skills` folder (`~/.openclaw/skills` by default). ClawHub publishing is optional and separate; there is no claimed `@orris/...` registry listing until an actual owner-qualified listing has been published and verified.

## Claude.ai, ChatGPT and other hosts

If the product offers custom-skill ZIP import, use the self-contained `fhir-suite` archive and the product's supported import flow. For a plugin ZIP importer, use the plugin archive only if that host accepts its manifest format. Account/workspace permissions may apply.

If the agent has a supported skill directory but no plugin manager, confirm that directory and use the helper (full set or `--bundle`). It needs Python 3.10+ only for the copy helper; an agent may copy the same complete directories with native filesystem tools instead. On Windows, use the actual profile/project path and `py -3` when appropriate; POSIX paths in this guide are examples, not Windows paths.

A chat that has neither filesystem execution nor an import/plugin-management interface cannot persistently install this package just by reading a prompt. Explain that limitation and provide the exact supported import step. Loading documentation into one conversation is not installation. Do not invent install commands, claim a nonexistent marketplace listing, or create an MCP configuration for this skills-only package.

## Verify and report

Check that the manager reports the plugin installed/enabled, or that all 16 destination skill folders (or the one self-contained skill) and their references exist. The copy helper verifies file hashes; identical repeat installs are no-ops and conflicts are refused without overwriting files. If Python is available, test the installed lookup helper with `Observation --kind resources --limit 1`; it should return the R5 Observation definition. This verifies file access, not whether the host actually selected a skill.

Ask the host to list/select the installed skill or run one simple FHIR navigation request when possible. Report host, scope/path, distribution, commit/version, verification actually performed and any reload step. Do not claim runtime behavior you have not observed.

For manual updates, stage a fresh copy and compare it with the installed copy. Back up locally modified skills before replacing their directories, or install into a separate scope. The helper deliberately has no force-overwrite mode. Native marketplace/Hub installs should use their own supported update/uninstall commands and preserve their bookkeeping.
