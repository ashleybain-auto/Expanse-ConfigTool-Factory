"""Regression tests for ECCS VBA procedure discovery."""

from pathlib import Path

from workbook_compiler.procedure_reader import (
    discover_procedures,
)


SOURCE = Path(
    "workbooks/analyzed/"
    "ECCS_REG_EXPANSE/"
    "extracted-vba/"
    "api-test-vba-source.txt"
)


def test_procedure_reader_finds_registration_actions() -> None:
    """Verify known Registration procedures are discovered."""

    procedures = discover_procedures(str(SOURCE))

    names = {
        item["name"]
        for item in procedures
    }

    assert "RefreshData_Accommodations" in names
    assert "PushUpdates_Accommodations" in names
    assert "RefreshData_Locations" in names
    assert "PushUpdates_Locations" in names
