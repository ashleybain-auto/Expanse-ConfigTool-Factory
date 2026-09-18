"""Build the ECCS Registration domain/action matrix."""

from __future__ import annotations

import json
from pathlib import Path


SOURCE = Path(
    "workbooks/analyzed/"
    "ECCS_REG_EXPANSE/"
    "procedures.json"
)

OUTPUT = Path(
    "workbooks/analyzed/"
    "ECCS_REG_EXPANSE/"
    "domain-actions.json"
)


def main() -> None:
    """Build domain/action metadata from classified VBA procedures."""

    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Procedure inventory not found: {SOURCE}"
        )

    procedures = json.loads(
        SOURCE.read_text(encoding="utf-8")
    )

    domains: dict[str, set[str]] = {}

    for procedure in procedures:
        name = procedure["name"]
        classification = procedure["classification"]

        if classification == "REFRESH":
            domain = name.removeprefix("RefreshData_")

        elif classification == "PUBLISH":
            domain = name.removeprefix("PushUpdates_")

        else:
            continue

        if domain:
            domains.setdefault(domain, set()).add(
                classification
            )

    output = [
        {
            "domain": domain,
            "actions": sorted(actions),
        }
        for domain, actions in sorted(domains.items())
    ]

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(f"Domains discovered: {len(output)}")

    for item in output:
        print(
            f"{item['domain']}: "
            f"{', '.join(item['actions'])}"
        )

    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
