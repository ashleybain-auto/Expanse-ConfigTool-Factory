"""Regression tests for the ECCS Workbook IR."""

from pathlib import Path

from workbook_compiler.ir_builder import (
    build_workbook_ir,
)


ANALYSIS_DIR = Path(
    "workbooks/analyzed/"
    "ECCS_REG_EXPANSE"
)


def test_workbook_ir_contains_expected_sections() -> None:
    """Verify that the Workbook IR contains core sections."""

    ir = build_workbook_ir(
        str(ANALYSIS_DIR)
    )

    assert "workbook" in ir
    assert "worksheets" in ir
    assert "procedures" in ir
    assert "domains" in ir
    assert "sql_references" in ir
    assert "actions" in ir

    assert len(ir["worksheets"]) > 0
    assert len(ir["procedures"]) > 0
    assert len(ir["domains"]) > 0
    assert len(ir["sql_references"]) > 0
