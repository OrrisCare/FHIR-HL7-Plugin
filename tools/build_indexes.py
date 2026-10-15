#!/usr/bin/env python3
"""Build an auditable R5 index from official downloads. Python 3.10+, stdlib only.

Accepts local source files or downloads only the three fixed official URLs.
Writes a candidate directory; never replaces the maintained index in place.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import tarfile
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen

BASE = "https://hl7.org/fhir/R5/"
URLS = {"toc": BASE + "toc.html", "package": BASE + "hl7.fhir.r5.core.tgz",
        "history": "https://hl7.org/fhir/package-list.json"}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.current = [attrs["href"], []]

    def handle_data(self, data):
        if self.current:
            self.current[1].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.current:
            self.links.append((self.current[0], " ".join(" ".join(self.current[1]).split())))
            self.current = None


def build(toc, package, history):
    parser = Links()
    parser.feed(toc.decode("utf-8-sig"))
    pages = {}
    for href, title in parser.links:
        url = urljoin(BASE, href)
        if not url.startswith(BASE) or not urlsplit(url).path.endswith(".html"):
            continue
        url = url.split("#")[0]
        if url not in pages or (title and len(title) > len(pages[url]["title"])):
            pages[url] = {"url": url, "title": title or url.rsplit("/", 1)[-1]}
    artifacts, resources = [], []
    with tarfile.open(fileobj=io.BytesIO(package), mode="r:gz") as archive:
        def read(name):
            # Read named members in memory, never extract untrusted archive paths.
            member = archive.getmember("package/" + name)
            if not member.isfile() or member.size > 30_000_000:
                raise ValueError("Unexpected package member")
            return json.load(archive.extractfile(member))
        metadata = read("package.json")
        if metadata["name"] != "hl7.fhir.r5.core" or metadata["version"] != "5.0.0":
            raise ValueError("Expected hl7.fhir.r5.core#5.0.0; review a new release separately")
        for item in read(".index.json")["files"]:
            resource = read(item["filename"])
            record = dict(item)
            record["name"] = resource.get("name", resource.get("title", resource.get("id", "")))
            record["description"] = resource.get("description", "")
            # A canonical identifies an artifact; it is not necessarily a fetch URL.
            record["canonical"] = record.pop("url", None)
            record["package"] = "hl7.fhir.r5.core#5.0.0"
            for key in ("base", "code", "expression", "target", "status", "abstract", "derivation"):
                if key in resource:
                    record[key] = resource[key]
            artifacts.append(record)
            if resource.get("resourceType") == "StructureDefinition" and resource.get("kind") == "resource" and resource.get("derivation") == "specialization":
                resource_id = resource["id"]
                url = BASE + resource_id.lower() + ".html"
                # Abstract pattern definitions have different page names: use TOC resolution.
                if url not in pages:
                    candidates = [u for u, p in pages.items() if p["title"].lower() == resource_id.lower()]
                    url = candidates[0] if candidates else None
                resources.append({"id": resource_id, "abstract": resource.get("abstract", False),
                                  "description": resource.get("description", ""), "url": url,
                                  "canonical": resource["url"], "package_file": item["filename"],
                                  "maturity": [e for e in resource.get("extension", []) if e.get("url", "").endswith(("structuredefinition-fmm", "structuredefinition-standards-status"))]})
    return {"pages": sorted(pages.values(), key=lambda r: r["url"]),
            "artifacts": sorted(artifacts, key=lambda r: (r["resourceType"], r["id"])),
            "resources": sorted(resources, key=lambda r: r["id"]),
            "releases": json.loads(history)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    for name in URLS:
        parser.add_argument("--" + name, type=Path)
    args = parser.parse_args()
    if args.out.exists() and any(args.out.iterdir()):
        parser.error("Output directory must be empty; compare candidates before promoting them")
    data, sources = {}, []
    for name, url in URLS.items():
        path = getattr(args, name)
        if path:
            content = path.read_bytes()
        else:
            with urlopen(url, timeout=60) as response:
                content = response.read(60_000_001)
            if len(content) > 60_000_000:
                raise ValueError("Source exceeds download size limit")
        data[name] = content
        sources.append({"url": url, "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)})
    result = build(**data)
    result["provenance"] = {"generated_at": datetime.now(timezone.utc).isoformat(), "release": "5.0.0",
                            "sources": sources, "counts": {k: len(result[k]) for k in ("pages", "resources", "artifacts")},
                            "artifact_types": dict(Counter(r["resourceType"] for r in result["artifacts"])),
                            "scope": "R5 TOC HTML targets and all entries in the official R5 core package index. Index inclusion is not a live-link or semantic-conformance check."}
    args.out.mkdir(parents=True, exist_ok=True)
    for name, value in result.items():
        (args.out / (name + ".json")).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result["provenance"]["counts"]))


if __name__ == "__main__":
    main()
