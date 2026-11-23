#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP from the shared package.

plugins/kauneonga/ is the package root for every app: the Claude manifest
(.claude-plugin/, .mcp.json) and the portable Agent Plugins manifest
(plugin.json, mcp.json) sit beside one shared skills/ tree. The ZIP holds the
portable manifest, its MCP config, the license, every skill and the listing
logo; Claude-only files are left out.

The Claude directory refuses a plugin folder where a file names an image, so
the portable manifest in the repository has no logo fields. They are added
to the copy written into the ZIP.

To update the plugin already created in the OpenAI dashboard, pass its app id:
the dashboard requires plugin.json's name to be that id, and refuses an
mcp.json sign-in block because the app's connection is configured there.

Usage: python3 scripts/build_chatgpt_package.py [output.zip] [--openai-app-id app-...]
"""
import json
import pathlib
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "plugins" / "kauneonga"
DEFAULT_OUT = ROOT / "dist" / "kauneonga-chatgpt.zip"
TOP_LEVEL = ["plugin.json", "mcp.json", "LICENSE"]
LOGO = "./assets/logo.png"


def package_files():
    files = [PLUGIN_DIR / name for name in TOP_LEVEL]
    for folder in ("skills", "assets"):
        base = PLUGIN_DIR / folder
        if base.is_dir():
            files.extend(sorted(p for p in base.rglob("*") if p.is_file()))
    return files


def contents(name, path, openai_app_id=None):
    if name == "mcp.json" and openai_app_id:
        config = json.loads(path.read_text(encoding="utf-8"))
        for server in config["mcpServers"].values():
            openai = server.get("extensions", {}).get("com.openai", {})
            openai.pop("auth", None)
            if not openai:
                server.get("extensions", {}).pop("com.openai", None)
            if not server.get("extensions", True):
                server.pop("extensions")
        return (json.dumps(config, indent=2) + "\n").encode("utf-8")
    if name != "plugin.json":
        return path.read_bytes()
    manifest = json.loads(path.read_text(encoding="utf-8"))
    interface = manifest["extensions"]["com.openai"]["interface"]
    interface["logo"] = LOGO
    interface["composerIcon"] = LOGO
    if openai_app_id:
        manifest["name"] = openai_app_id
    return (json.dumps(manifest, indent=2) + "\n").encode("utf-8")


def build(out=DEFAULT_OUT, openai_app_id=None):
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in package_files():
            name = path.relative_to(PLUGIN_DIR).as_posix()
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, contents(name, path, openai_app_id))
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    app_id = None
    if "--openai-app-id" in args:
        i = args.index("--openai-app-id")
        app_id = args[i + 1]
        del args[i : i + 2]
    print(build(args[0] if args else DEFAULT_OUT, app_id))
