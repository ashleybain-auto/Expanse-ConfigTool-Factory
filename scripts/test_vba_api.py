"""Standalone VBA extraction test for the ECCS project."""

from pathlib import Path

from oletools.olevba import VBA_Parser


WORKBOOK = Path(
    "workbooks/baseline/Mapping_Expanse_REG_Domain.xlsb"
)

OUTPUT = Path(
    "workbooks/analyzed/ECCS_REG_EXPANSE/extracted-vba"
)


def main() -> None:
    """Extract VBA directly through the oletools Python API."""

    OUTPUT.mkdir(
        parents=True,
        exist_ok=True,
    )

    parser = VBA_Parser(str(WORKBOOK))

    try:
        print(f"Workbook: {WORKBOOK}")
        print(f"VBA detected: {parser.detect_vba_macros()}")

        modules = list(parser.extract_macros())

        print(f"Modules found: {len(modules)}")

        source_parts: list[str] = []

        for (
            filename,
            stream_path,
            vba_filename,
            vba_code,
        ) in modules:
            print(f"Module: {vba_filename}")

            source_parts.append(
                f"===== {vba_filename} =====\n"
                f"Source: {filename}\n"
                f"Stream: {stream_path}\n\n"
                f"{vba_code}"
            )

        source_file = OUTPUT / "api-test-vba-source.txt"

        source_file.write_text(
            "\n\n".join(source_parts),
            encoding="utf-8",
        )

        analysis = list(parser.analyze_macros() or [])

        analysis_file = OUTPUT / "api-test-analysis.txt"

        analysis_file.write_text(
            "\n".join(
                f"{item[0]} | {item[1]} | {item[2]}"
                for item in analysis
            ),
            encoding="utf-8",
        )

        print(f"Source output: {source_file}")
        print(f"Analysis output: {analysis_file}")

    finally:
        parser.close()


if __name__ == "__main__":
    main()
