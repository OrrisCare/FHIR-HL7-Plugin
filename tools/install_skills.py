#!/usr/bin/env python3
"""Copy FHIR skills to an explicitly selected host directory, without overwriting files.

Python 3.10+, standard library only. Performs no network calls or host configuration edits.
Re-running an identical install is a no-op; conflicting folders require manual resolution.
"""
import argparse
import hashlib
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(directory):
    result = {}
    for path in directory.rglob('*'):
        if path.is_symlink():
            raise ValueError(f'Symlink not accepted: {path}')
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
            result[path.relative_to(directory).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def install(destination, bundle=False, dry_run=False):
    destination = Path(destination).expanduser().absolute()
    if destination.is_symlink():
        raise ValueError(f'Choose a real directory, not a symlink: {destination}')
    # Resolve ordinary OS aliases such as macOS /var -> /private/var.
    destination = destination.resolve()
    if destination.exists() and not destination.is_dir():
        raise ValueError(f'Destination is not a directory: {destination}')
    sources = [ROOT / 'skills/fhir-suite'] if bundle else sorted((ROOT / 'plugins/fhir/skills').iterdir())
    sources = [p for p in sources if p.is_dir() and (p / 'SKILL.md').is_file()]
    expected = 1 if bundle else 16
    if len(sources) != expected:
        raise ValueError(f'Incomplete distribution: expected {expected} skills')
    to_copy = []
    # Preflight every skill before touching the destination.
    for source in sources:
        source_hashes = fingerprint(source)
        target = destination / source.name
        if target.exists() or target.is_symlink():
            if target.is_symlink() or not target.is_dir() or fingerprint(target) != source_hashes:
                raise ValueError(f'Existing skill differs; nothing copied: {target}. Back it up or use a separate scope.')
        else:
            to_copy.append((source, target))
    if not dry_run:
        created = []
        try:
            destination.mkdir(parents=True, exist_ok=True)
            for source, target in to_copy:
                # Reserve the directory without allowing an existing target to be merged.
                target.mkdir()
                created.append(target)
                shutil.copytree(source, target, dirs_exist_ok=True, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
                if fingerprint(source) != fingerprint(target):
                    raise ValueError(f'Copy verification failed: {target}')
        except Exception:
            for target in reversed(created):
                shutil.rmtree(target)
            raise
    return {'destination': str(destination), 'skills': expected, 'new': len(to_copy), 'unchanged': expected - len(to_copy), 'dry_run': dry_run}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, required=True, help='Confirmed host skill-root directory')
    parser.add_argument('--bundle', action='store_true', help='Install one self-contained fhir-suite skill instead of 16 sibling skills')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        import json
        print(json.dumps(install(args.dest, args.bundle, args.dry_run), indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
