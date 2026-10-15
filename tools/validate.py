#!/usr/bin/env python3
"""Validate repository packaging and index invariants without network access."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/fhir"


def validate():
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    manifest = json.loads((PLUGIN / "plugin.json").read_text())
    compat = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    entry = marketplace["plugins"][0]
    check((ROOT / entry["source"]["path"]).resolve() == PLUGIN, "Marketplace source does not resolve to the plugin")
    check(entry["name"] == manifest["name"] == compat["name"], "Plugin identity mismatch")
    check(manifest["version"] == compat["version"], "Manifest version mismatch")
    check(compat["skills"] == "./skills", "Compatibility skill path is wrong")
    interface = manifest["extensions"]["com.openai"]["interface"]
    check(interface == compat["interface"], "Presentation metadata differs between manifests")
    for key, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000), ("developerName", 80)):
        check(0 < len(interface[key]) <= limit, f"Invalid listing field: {key}")
    for key in ("logo", "composerIcon"):
        check((PLUGIN / interface[key]).is_file(), f"Missing {key}")
    check(len(interface["defaultPrompt"]) <= 3 and all(len(p) <= 128 for p in interface["defaultPrompt"]), "Invalid listing prompts")
    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    check(len(skills) == 16, "Expected 16 routed skills")
    for path in skills:
        text = path.read_text()
        match = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n", text)
        check(bool(match), f"Invalid skill frontmatter: {path}")
        if match:
            check(match[1] == path.parent.name, f"Skill name mismatch: {path}")
            try:
                check(bool(json.loads(match[2])), f"Empty skill description: {path}")
            except json.JSONDecodeError:
                errors.append(f"Description must be a JSON-compatible YAML quoted string: {path}")
        check((path.parent / "agents/openai.yaml").is_file(), f"Missing UI metadata: {path}")
        check(not re.search(r"\b(?:TODO|TBD|FIXME)\b", text), f"Unfinished skill: {path}")
    for path in PLUGIN.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("https://", "http://", "#")):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            check(resolved.is_relative_to(PLUGIN.resolve()), f"Reference escapes plugin: {path}: {target}")
            check(resolved.exists(), f"Broken local reference: {path}: {target}")
    indexes = PLUGIN / "skills/fhir-standards/references/indexes"
    provenance = json.loads((indexes / "provenance.json").read_text())
    data = {name: json.loads((indexes / f"{name}.json").read_text()) for name in ("resources", "artifacts", "pages")}
    for name, records in data.items():
        check(len(records) == provenance["counts"][name], f"Provenance count mismatch: {name}")
    check(len({r["id"] for r in data["resources"]}) == len(data["resources"]), "Duplicate resource definitions")
    check(sum(not r["abstract"] for r in data["resources"]) == 158, "Concrete R5 resource coverage changed")
    check(len({r["filename"] for r in data["artifacts"]}) == len(data["artifacts"]), "Duplicate artifact filenames")
    check(all(r["package"] == "hl7.fhir.r5.core#5.0.0" for r in data["artifacts"]), "Mixed core package versions")
    check(all(r["url"].startswith("https://hl7.org/fhir/R5/") for r in data["pages"]), "Non-R5 documentation in R5 page index")
    pages = {r["url"] for r in data["pages"]}
    check(all(r["url"] in pages for r in data["resources"]), "Resource page missing from TOC index")
    for host in ("claude", "cursor"):
        native = json.loads((PLUGIN / f".{host}-plugin/plugin.json").read_text())
        catalog = json.loads((ROOT / f".{host}-plugin/marketplace.json").read_text())
        check(native["name"] == manifest["name"] and native["version"] == manifest["version"], f"{host} manifest mismatch")
        check((ROOT / catalog["plugins"][0]["source"]).resolve() == PLUGIN, f"{host} marketplace source mismatch")
        check(native["skills"] == "./skills", f"{host} skill path mismatch")
    suite = ROOT / "skills/fhir-suite"
    check(len(list(suite.rglob("SKILL.md"))) == 1, "Suite must expose exactly one skill")
    check(len(list(suite.rglob("GUIDE.md"))) == 16, "Suite must preserve all 16 workflows")
    check(json.loads((suite / "distribution.json").read_text())["version"] == manifest["version"], "Suite version mismatch")
    for path in suite.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("https://", "http://", "#")):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            check(resolved.is_relative_to(suite.resolve()) and resolved.is_file(), f"Broken or escaping suite reference: {path}: {target}")
    for path in PLUGIN.rglob("*"):
        check(not path.is_symlink(), f"Symlink in portable package: {path}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print("PASS: manifests, marketplace path, 16 skills, portable suite, local links, metadata and R5 index invariants")
