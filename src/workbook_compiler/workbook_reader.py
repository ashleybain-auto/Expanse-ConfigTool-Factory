from __future__ import annotations

import hashlib
from pathlib import Path

import openpyxl
from pyxlsb import open_workbook


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def read_xlsb(path: Path) -> list[dict]:
    sheets: list[dict] = []

    with open_workbook(path) as workbook:
        for name in workbook.sheets:
            sheets.append(
                {
                    "name": name,
                    "visibility": "unknown",
                    "classification": "unknown",
                }
            )

    return sheets


def read_xlsm_or_xlsx(path: Path) -> list[dict]:
    workbook = openpyxl.load_workbook(
        path,
        read_only=True,
        data_only=False,
        keep_vba=path.suffix.lower() == ".xlsm",
    )

    sheets: list[dict] = []

    for worksheet in workbook.worksheets:
        sheets.append(
            {
                "name": worksheet.title,
                "visibility": "visible",
                "row_count": worksheet.max_row or 0,
                "column_count": worksheet.max_column or 0,
                "classification": "unknown",
            }
        )

    workbook.close()

    return sheets


def read_workbook(path: str) -> dict:
    source = Path(path)

    if not source.exists():
        raise FileNotFoundError(f"Workbook not found: {source}")

    extension = source.suffix.lower()

    if extension == ".xlsb":
        worksheets = read_xlsb(source)

    elif extension in {".xlsm", ".xlsx"}:
        worksheets = read_xlsm_or_xlsx(source)

    else:
        raise ValueError(
            f"Unsupported workbook type: {extension}"
        )

    return {
        "filename": source.name,
        "extension": extension,
        "sha256": sha256_file(source),
        "file_size_bytes": source.stat().st_size,
        "worksheets": worksheets,
    }