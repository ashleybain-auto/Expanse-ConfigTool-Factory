"""Functional classification for extracted ECCS VBA procedures."""

from __future__ import annotations


def classify_procedure(name: str) -> str:
    """Classify a VBA procedure by its functional responsibility."""

    normalized = name.casefold()

    if normalized.startswith("refreshdata_"):
        return "REFRESH"

    if normalized.startswith("pushupdates_"):
        return "PUBLISH"

    if normalized.startswith("copydata_"):
        return "STAGE"

    if normalized.startswith("validate"):
        return "VALIDATE"

    if "export" in normalized:
        return "EXPORT"

    if "setting" in normalized:
        return "CONFIGURE"

    return "OTHER"
