#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP from the shared package.

The ZIP holds the portable manifest, its MCP config, the license, every skill
and the listing assets. Skills and assets live in the Claude plugin folder
(plugins/kauneonga/) and keep their skills/ and assets/ paths in the ZIP.
Claude-only files (.claude-plugin/, .mcp.json) are left out.

Usage: python3 scripts/build_chatgpt_package.py [output.zip]
"""
import pathlib
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "dist" / "kauneonga-chatgpt.zip"
TOP_LEVEL = ["plugin.json", "mcp.json", "LICENSE"]
PLUGIN_DIR = ROOT / "plugins" / "kauneonga"


def package_files():
    """(source path, name in the ZIP) pairs."""
    files = [(ROOT / name, name) for name in TOP_LEVEL]
    for folder in ("skills", "assets"):
        base = PLUGIN_DIR / folder
        if base.is_dir():
            files.extend(
                (p, p.relative_to(PLUGIN_DIR).as_posix())
                for p in sorted(base.rglob("*"))
                if p.is_file()
            )
    return files


def build(out=DEFAULT_OUT):
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, name in package_files():
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())
    return out


if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT))
