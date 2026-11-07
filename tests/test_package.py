#!/usr/bin/env python3
"""Offline checks. Not a substitute for schema, sign-in or live integration tests."""
import hashlib
import json
import pathlib
import re
import struct
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED_ENDPOINT = "https://mcp.kauneonga.com/api/v2/mcp"
EXPECTED_NAME = "kauneonga"
EXPECTED_SKILLS = {
    "kauneonga",
    "setup",
    "message-triage",
    "oncall-changes",
    "contact-delivery",
}
# Words and phrases public material must not contain: internal systems, vendors,
# restricted internal roles and other brands. Stored as SHA-256 hashes of the lowercase
# phrase so this file doesn't name them; ask a maintainer for the list.
FORBIDDEN_SHA256 = {
    "ade19f5315c3cf44cbc4d01d062b19745eb686558cca562cebbe7935a571e525",
    "9298f1dd1046b9442cab2483c19b03205361e5d73fe64b2ee532e7013e443e39",
    "f41f2c785e15ca0c3fa8776852d7dec9166e163011bf41d9f40ad67b8e93cc5f",
    "866e1f18c9370d5db858a022608af1d74146e2943fbd3666ab03f55d1c4d2f67",
    "d329f11d9a60de9b6f268d88fc6b40726b9e1496890bd0502f12899ac9cf8e61",
    "48b00f66e22389fcfb4fd483b9dc675f4e54a9b1688cdfa9e47bac6e4c58794d",
}


def names_something_internal(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    for n in (1, 2, 3):
        for i in range(len(words) - n + 1):
            phrase = " ".join(words[i : i + n]).encode("utf-8")
            if hashlib.sha256(phrase).hexdigest() in FORBIDDEN_SHA256:
                return True
    return False
PUBLIC_FILES = ["README.md", "plugin.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check_manifests():
    claude = read_json(".claude-plugin/plugin.json")
    marketplace = read_json(".claude-plugin/marketplace.json")
    portable = read_json("plugin.json")
    cmcp = read_json(".mcp.json")
    pmcp = read_json("mcp.json")

    assert claude["name"] == portable["name"] == EXPECTED_NAME
    assert claude["version"] == portable["version"]
    listed = marketplace["plugins"]
    assert [p["name"] for p in listed] == [EXPECTED_NAME], listed
    assert listed[0]["source"] == "./"
    assert listed[0]["version"] == claude["version"]
    assert portable["$schema"].endswith("plugin.schema.json")
    assert pmcp["$schema"].endswith("mcp.schema.json")
    assert portable["repository"].endswith("/kauneonga-plugin")

    for cfg in (cmcp, pmcp):
        servers = cfg["mcpServers"]
        assert set(servers) == {EXPECTED_NAME}, servers
        assert servers[EXPECTED_NAME]["url"] == EXPECTED_ENDPOINT
        assert "headers" not in servers[EXPECTED_NAME], "Never put credentials in the manifest"
    assert cmcp["mcpServers"][EXPECTED_NAME]["type"] == "http"
    assert pmcp["mcpServers"][EXPECTED_NAME]["type"] == "streamable-http"
    assert pmcp["mcpServers"][EXPECTED_NAME]["extensions"]["com.openai"]["auth"]["type"] == "oauth"

    openai = portable["extensions"]["com.openai"]
    assert openai["onboardingSkill"] == "./skills/setup/SKILL.md"
    listing = openai["interface"]
    assert len(listing["displayName"]) <= 30
    assert len(listing["shortDescription"]) <= 30
    assert len(listing["longDescription"]) <= 4000
    assert 1 <= len(listing["defaultPrompt"]) <= 3
    assert all(len(p) <= 128 for p in listing["defaultPrompt"])
    assert listing["capabilities"] == ["Read", "Write"]
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        assert listing[key].startswith("https://"), key
    check_logo(ROOT / listing["logo"])


def check_logo(path):
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "logo must be a PNG"
    width, height = struct.unpack(">II", data[16:24])
    assert width == height and width >= 48, (width, height)


def check_skills():
    found = set()
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", text, re.S)
        assert match, f"{skill} needs name and description frontmatter"
        name, description = match.groups()
        assert name == skill.parent.name, f"{skill}: name must match its folder"
        assert len(name) <= 64 and len(description) <= 1024, skill
        assert not names_something_internal(text), f"{skill} names something internal"
        found.add(name)
    assert found == EXPECTED_SKILLS, found ^ EXPECTED_SKILLS


def check_public_text():
    for name in PUBLIC_FILES:
        text = (ROOT / name).read_text(encoding="utf-8")
        assert not names_something_internal(text), f"{name} names something internal"
    assert "/plugin install kauneonga --marketplace Kauneonga/kauneonga-plugin" in (
        ROOT / "README.md"
    ).read_text(encoding="utf-8")


def check_chatgpt_package():
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_chatgpt_package

    with tempfile.TemporaryDirectory() as tmp:
        out = build_chatgpt_package.build(pathlib.Path(tmp) / "pkg.zip")
        names = set(zipfile.ZipFile(out).namelist())
    assert {"plugin.json", "mcp.json", "LICENSE", "assets/logo.png"} <= names, names
    skills = {n.split("/")[1] for n in names if n.startswith("skills/")}
    assert skills == EXPECTED_SKILLS, skills
    assert not any(n.startswith(".claude-plugin/") or n == ".mcp.json" for n in names)


def check_license():
    text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "MIT License" in text and "Kauneonga LLC" in text


if __name__ == "__main__":
    check_manifests()
    check_skills()
    check_public_text()
    check_chatgpt_package()
    check_license()
    print("PASS")
