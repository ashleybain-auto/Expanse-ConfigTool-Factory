"""Static VBA extraction utilities for the ECCS Workbook Compiler."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from oletools.olevba import VBA_Parser


def extract_vba(
    workbook_path: str,
    output_dir: str,
) -> dict[str, Any]:
    """Extract VBA source and analysis using the oletools Python API."""

    source = Path(workbook_path)
    destination = Path(output_dir)

    destination.mkdir(
        parents=True,
        exist_ok=True,
    )

    source_file = destination / "vba-source.txt"
    modules_file = destination / "vba-modules.json"
    analysis_file = destination / "vba-analysis.json"

    parser = VBA_Parser(str(source))

    modules: list[dict[str, Any]] = []
    analysis: list[dict[str, str]] = []

    try:
        has_vba = parser.detect_vba_macros()

        if has_vba:
            for (
                filename,
                stream_path,
                vba_filename,
                vba_code,
            ) in parser.extract_macros():

                modules.append(
                    {
                        "filename": filename,
                        "stream_path": stream_path,
                        "vba_filename": vba_filename,
                        "source": vba_code,
                    }
                )

            for (
                result_type,
                keyword,
                description,
            ) in parser.analyze_macros() or ():

                analysis.append(
                    {
                        "type": str(result_type),
                        "keyword": str(keyword),
                        "description": str(description),
                    }
                )

        combined_source_parts: list[str] = []

        for module in modules:
            combined_source_parts.append(
                f"===== {module['vba_filename']} ====="
            )
            combined_source_parts.append(
                module["source"]
            )

        source_file.write_text(
            "\n\n".join(combined_source_parts),
            encoding="utf-8",
        )

        modules_file.write_text(
            json.dumps(
                modules,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        analysis_file.write_text(
            json.dumps(
                analysis,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return {
            "workbook": str(source),
            "has_vba": has_vba,
            "module_count": len(modules),
            "analysis_count": len(analysis),
            "source_file": str(source_file),
            "modules_file": str(modules_file),
            "analysis_file": str(analysis_file),
        }

    finally:
        parser.close()
