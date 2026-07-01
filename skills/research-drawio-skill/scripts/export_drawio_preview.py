#!/usr/bin/env python3
"""Export draw.io diagrams through diagrams.net/draw.io Desktop CLI.

The helper uses relative input/output paths from a stable working directory
where possible. Some Windows draw.io Desktop builds return exit code 0 but skip
output creation when absolute paths are passed to `--output`.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


def windows_registry_candidates() -> list[Path]:
    if os.name != "nt":
        return []
    try:
        import winreg
    except ImportError:
        return []

    candidates: list[Path] = []
    hives = [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]
    keys = [
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall",
        r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
    ]
    for hive in hives:
        for key_name in keys:
            try:
                root = winreg.OpenKey(hive, key_name)
            except OSError:
                continue
            with root:
                for index in range(winreg.QueryInfoKey(root)[0]):
                    try:
                        sub_name = winreg.EnumKey(root, index)
                        sub = winreg.OpenKey(root, sub_name)
                    except OSError:
                        continue
                    with sub:
                        try:
                            display = str(winreg.QueryValueEx(sub, "DisplayName")[0]).lower()
                        except OSError:
                            continue
                        if "draw.io" not in display and "diagrams.net" not in display:
                            continue
                        for value_name in ("DisplayIcon", "InstallLocation"):
                            try:
                                value = str(winreg.QueryValueEx(sub, value_name)[0])
                            except OSError:
                                continue
                            if value_name == "DisplayIcon":
                                candidates.append(Path(value.split(",")[0].strip('"')))
                            else:
                                candidates.append(Path(value) / "draw.io.exe")
    return candidates


def find_drawio_cli(explicit: str | None = None) -> Path:
    raw_candidates: list[str | Path] = []
    if explicit:
        raw_candidates.append(explicit)
    env_cli = os.environ.get("DRAWIO_CLI") or os.environ.get("DIAGRAMS_NET_CLI")
    if env_cli:
        raw_candidates.append(env_cli)
    for name in ("drawio", "draw.io", "diagrams.net", "drawio.exe", "draw.io.exe"):
        found = shutil.which(name)
        if found:
            raw_candidates.append(found)

    if os.name == "nt":
        local = Path(os.environ.get("LOCALAPPDATA", ""))
        raw_candidates.extend(
            [
                local / "Programs" / "draw.io" / "draw.io.exe",
                local / "draw.io" / "draw.io.exe",
                Path(r"D:\drawio\draw.io\draw.io.exe"),
            ]
        )
        for env_name in ("ProgramFiles", "ProgramFiles(x86)"):
            base = os.environ.get(env_name)
            if base:
                raw_candidates.append(Path(base) / "draw.io" / "draw.io.exe")
        raw_candidates.extend(windows_registry_candidates())

    for candidate in raw_candidates:
        path = Path(candidate).expanduser()
        if path.is_file():
            return path
    raise SystemExit(
        "ERROR: diagrams.net/draw.io CLI not found. Install JGraph.Draw with winget "
        "or set DRAWIO_CLI to the draw.io executable path."
    )


def rel_to_cwd(path: Path, cwd: Path) -> str:
    try:
        return str(path.resolve().relative_to(cwd.resolve()))
    except ValueError:
        return str(path.resolve())


def wait_for_output(path: Path, timeout_s: float = 10.0) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if path.exists() and path.stat().st_size > 0:
            return
        time.sleep(0.25)


def run_export(exe: Path, drawio: Path, out_path: Path, fmt: str, timeout_s: int) -> subprocess.CompletedProcess[str]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        out_path.unlink()

    cwd = drawio.parent.resolve()
    cmd = [
        str(exe),
        "--export",
        "--format",
        fmt,
        "--output",
        rel_to_cwd(out_path, cwd),
        rel_to_cwd(drawio, cwd),
    ]
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout_s)
    wait_for_output(out_path)
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise SystemExit(
            f"ERROR: draw.io export produced no {fmt} output.\n"
            f"command: {' '.join(cmd)}\n"
            f"cwd: {cwd}\n"
            f"exit: {proc.returncode}\n"
            f"stdout: {proc.stdout.strip()}\n"
            f"stderr: {proc.stderr.strip()}"
        )
    return proc


def png_probe(path: Path) -> str:
    try:
        from PIL import Image, ImageStat
    except ImportError:
        return "png_probe=skipped:Pillow_unavailable"
    image = Image.open(path).convert("RGB")
    stat = ImageStat.Stat(image)
    extrema = stat.extrema
    if all(lo == hi for lo, hi in extrema):
        raise SystemExit(f"ERROR: exported PNG appears blank or single-color: {path}")
    return f"png_probe=size={image.size[0]}x{image.size[1]} extrema={extrema}"


def svg_probe(path: Path) -> str:
    head = path.read_text(encoding="utf-8", errors="replace")[:500].lower()
    if "<svg" not in head:
        raise SystemExit(f"ERROR: exported SVG does not start like SVG: {path}")
    return "svg_probe=ok"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drawio", type=Path, help="Input .drawio file")
    parser.add_argument("--out-dir", type=Path, help="Output directory. Defaults to <drawio-dir>/exports")
    parser.add_argument("--formats", nargs="+", default=["png", "svg"], choices=["png", "svg", "pdf"])
    parser.add_argument("--drawio-cli", help="Explicit path to draw.io/diagrams.net executable")
    parser.add_argument("--timeout", type=int, default=90, help="Per-export timeout in seconds")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    drawio = args.drawio.resolve()
    if not drawio.is_file():
        raise SystemExit(f"ERROR: input .drawio file does not exist: {drawio}")
    out_dir = (args.out_dir or drawio.parent / "exports").resolve()
    exe = find_drawio_cli(args.drawio_cli)

    print(f"drawio_cli={exe}")
    for fmt in args.formats:
        out_path = out_dir / f"{drawio.stem}.{fmt}"
        proc = run_export(exe, drawio, out_path, fmt, args.timeout)
        print(f"export={fmt} path={out_path} bytes={out_path.stat().st_size} exit={proc.returncode}")
        if fmt == "png":
            print(png_probe(out_path))
        elif fmt == "svg":
            print(svg_probe(out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
