"""Generate a VBA procedure inventory for an ECCS workbook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from workbook_compiler.procedure_reader import (
    write_procedure_inventory,
)


def main() -> None:
    """Generate a procedure inventory from a selected VBA source file."""

    parser = argparse.ArgumentParser(
        description="Build an ECCS VBA procedure inventory."
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to extracted VBA source.",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path for procedures.json.",
    )

    args = parser.parse_args()

    procedures = write_procedure_inventory(
        args.source,
        args.output,
    )

    counts: dict[str, int] = {}

    for procedure in procedures:
        classification = procedure["classification"]

        counts[classification] = (
            counts.get(classification, 0) + 1
        )

    print(
        f"Procedures discovered: {len(procedures)}"
    )

    for classification, count in sorted(
        counts.items()
    ):
        print(
            f"{classification}: {count}"
        )

    print(
        f"Output: {args.output}"
    )

    # Verify the generated JSON is readable.
    json.loads(
        Path(args.output).read_text(
            encoding="utf-8"
        )
    )


if __name__ == "__main__":
    main()
