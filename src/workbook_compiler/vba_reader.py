from __future__ import annotations

import subprocess
from pathlib import Path


def extract_vba(
    workbook_path: str,
    output_dir: str,
) -> str:

    source = Path(workbook_path)
    destination = Path(output_dir)

    destination.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = destination / "vba-source.txt"

    command = [
        "olevba",
        "--decode",
        str(source),
    ]

    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )

    if completed.returncode != 0:
        raise RuntimeError(
            completed.stderr.strip()
            or "olevba failed"
        )

    output_file.write_text(
        completed.stdout,
        encoding="utf-8",
    )

    return str(output_file)