#!/usr/bin/env python3
"""Install the skill snapshot from original upstream repositories."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile
from pathlib import Path


RAW_BASE = "https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main"


def download(url: str, destination: Path, attempts: int = 3) -> None:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(
                url, headers={"User-Agent": "codex-skills-kit-installer"}
            )
            with urllib.request.urlopen(request, timeout=90) as response:
                destination.write_bytes(response.read())
            return
        except Exception as error:  # noqa: BLE001
            last_error = error
            if attempt < attempts:
                time.sleep(attempt * 2)
    raise RuntimeError(f"Failed to download {url}: {last_error}") from last_error


def load_manifest(script_root: Path) -> dict:
    local = script_root.parent / "manifest" / "install-manifest.json"
    if local.exists():
        return json.loads(local.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="codex-skills-manifest-") as temp:
        path = Path(temp) / "manifest.json"
        download(f"{RAW_BASE}/manifest/install-manifest.json", path)
        return json.loads(path.read_text(encoding="utf-8"))


def safe_replace(source: Path, destination: Path, force: bool) -> str:
    if destination.exists():
        if not force:
            return "skipped"
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        backup = destination.with_name(f"{destination.name}.backup-{timestamp}")
        destination.rename(backup)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return "installed"


def install_sources(manifest: dict, codex_home: Path, latest: bool, force: bool) -> None:
    skills_root = codex_home / "skills"
    skills_root.mkdir(parents=True, exist_ok=True)
    installed = skipped = failed = 0

    for package in manifest["sources"]:
        source_name = package["source"]
        owner, repo = source_name.split("/", 1)
        ref = "main" if latest else package["ref"]
        print(f"\n[{source_name}] ref={ref}")
        pending = []
        for item in package["items"]:
            destination = skills_root / item["destination"]
            if destination.exists() and not force:
                print(f"  SKIPPED   {item['name']} -> {destination}")
                skipped += 1
            else:
                pending.append(item)
        if not pending:
            continue
        try:
            with tempfile.TemporaryDirectory(prefix="codex-skills-source-") as temp:
                temp_path = Path(temp)
                if all(item.get("single_file") for item in pending):
                    for item in pending:
                        source_path = temp_path / item["name"]
                        source_path.mkdir(parents=True)
                        relative = (
                            f"{item['source_path'].rstrip('/')}/{item['single_file']}"
                        )
                        download(
                            f"https://raw.githubusercontent.com/{source_name}/{ref}/{relative}",
                            source_path / item["single_file"],
                        )
                        destination = skills_root / item["destination"]
                        result = safe_replace(source_path, destination, force)
                        print(
                            f"  {result.upper():9} {item['name']} -> {destination}"
                        )
                        if result == "installed":
                            installed += 1
                        else:
                            skipped += 1
                    continue
                archive = temp_path / "source.zip"
                download(
                    f"https://codeload.github.com/{owner}/{repo}/zip/{ref}", archive
                )
                with zipfile.ZipFile(archive) as bundle:
                    bundle.extractall(temp_path / "expanded")
                roots = [
                    path for path in (temp_path / "expanded").iterdir() if path.is_dir()
                ]
                if len(roots) != 1:
                    raise RuntimeError("Unexpected GitHub archive layout")
                root = roots[0]
                for item in pending:
                    source_path = root if item["source_path"] == "." else root / item["source_path"]
                    destination = skills_root / item["destination"]
                    if not source_path.is_dir():
                        print(f"  FAILED {item['name']}: missing {item['source_path']}")
                        failed += 1
                        continue
                    result = safe_replace(source_path, destination, force)
                    print(f"  {result.upper():9} {item['name']} -> {destination}")
                    if result == "installed":
                        installed += 1
                    else:
                        skipped += 1
        except Exception as error:  # noqa: BLE001
            print(f"  PACKAGE FAILED: {error}", file=sys.stderr)
            failed += len(pending)

    print(f"\nSkills complete: installed={installed}, skipped={skipped}, failed={failed}")
    if failed:
        raise RuntimeError(f"{failed} skill items failed")


def find_codex() -> str | None:
    command = shutil.which("codex")
    if command:
        return command
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA", "")) / "OpenAI" / "Codex" / "bin"
        candidates = sorted(base.glob("*/codex.exe"), reverse=True)
        if candidates:
            return str(candidates[0])
    return None


def install_plugins(manifest: dict) -> None:
    codex = find_codex()
    if not codex:
        print("\nPlugin restore skipped: codex CLI was not found.")
        return
    print("\nRestoring Codex plugins (best effort)")
    failures = []
    for item in manifest.get("plugins", []):
        selector = item["selector"]
        result = subprocess.run(
            [codex, "plugin", "add", selector, "--json"],
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode == 0:
            print(f"  INSTALLED {selector}")
        else:
            failures.append(selector)
            detail = (result.stderr or result.stdout).strip().splitlines()
            suffix = detail[-1] if detail else "unknown error"
            print(f"  WARNING   {selector}: {suffix}")
    if failures:
        print(
            "\nSome plugins require a newer Codex build, marketplace access, or connector login:"
        )
        for selector in failures:
            print(f"  - {selector}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", type=Path)
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-plugins", action="store_true")
    args = parser.parse_args()

    codex_home = (
        args.codex_home
        or Path(os.environ.get("CODEX_HOME", ""))
        or Path.home() / ".codex"
    )
    if str(codex_home) == ".":
        codex_home = Path.home() / ".codex"
    codex_home = codex_home.expanduser().resolve()

    manifest = load_manifest(Path(__file__).resolve().parent)
    install_sources(manifest, codex_home, args.latest, args.force)
    if not args.skip_plugins:
        install_plugins(manifest)
    print("\nRestart Codex to load the installed skills.")


if __name__ == "__main__":
    main()
