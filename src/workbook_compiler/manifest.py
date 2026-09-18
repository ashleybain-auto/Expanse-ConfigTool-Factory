"""Migration manifest generation for ECCS."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON document."""

    if not path.exists():
        raise FileNotFoundError(
            f"Manifest input not found: {path}"
        )

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def generate_manifest(
    ir_file: str,
    config_file: str,
) -> dict[str, Any]:
    """Generate an ECCS migration manifest from Workbook IR."""

    ir = load_json(
        Path(ir_file)
    )

    config = load_json(
        Path(config_file)
    )

    workbook = ir["workbook"]

    config_tool = config[
        "configTools"
    ]["registration"]

    variant = (
        "EXPANSE"
        if "NonMagic" not in workbook["filename"]
        else "NONMAGIC"
    )

    domains = []

    for item in ir.get("domains", []):
        domains.append(
            {
                "name": item["domain"],
                "actions": item["actions"],
            }
        )

    manifest = {
        "suite": config["suite"],
        "factory": config["factory"],
        "configTool": {
            "code": config_tool["code"],
            "name": config_tool["name"],
            "variant": variant,
        },
        "source": {
            "workbook": workbook["filename"],
            "extension": workbook["extension"],
            "sha256": workbook["sha256"],
        },
        "domains": domains,
        "actions": ir.get(
            "actions",
            [],
        ),
        "integrations": {
            "sql": ir.get(
                "sql_references",
                [],
            ),
            "api": ir.get(
                "api_references",
                [],
            ),
        },
        "validation": {
            "required": True,
        },
        "audit": {
            "required": True,
        },
        "migration": {
            "status": "IN_PROGRESS",
            "generatedBy": "ECCS Workbook Compiler",
        },
    }

    return manifest


def write_manifest(
    ir_file: str,
    config_file: str,
    output_file: str,
) -> dict[str, Any]:
    """Generate and write the migration manifest."""

    manifest = generate_manifest(
        ir_file,
        config_file,
    )

    destination = Path(output_file)

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    destination.write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    return manifest
