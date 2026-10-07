"""Check the published artifact manifest with the same command locally and in CI."""
from pathlib import Path
import hashlib
import re


def main():
    root = Path(__file__).resolve().parents[1]
    seen = set()
    for line in (root / 'ARTIFACTS.sha256').read_text().splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        fields = line.split(None, 1)
        if len(fields) != 2 or re.fullmatch(r'[a-f0-9]{64}', fields[0]) is None:
            raise SystemExit('Invalid artifact manifest entry')
        expected, name = fields
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts or name in seen:
            raise SystemExit('Invalid or duplicate artifact path: ' + name)
        seen.add(name)
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise SystemExit('Missing or redirected artifact: ' + name)
        digest = hashlib.sha256()
        with path.open('rb') as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b''):
                digest.update(chunk)
        if digest.hexdigest() != expected:
            raise SystemExit('Artifact checksum mismatch: ' + name)
    if not seen:
        raise SystemExit('Artifact manifest is empty')
    print(f'PASS: {len(seen)} artifact checksums')


if __name__ == '__main__':
    main()
