#!/usr/bin/env python3
"""Cursor hook example: warn before risky research-data or secret commands."""

from __future__ import annotations

import json
import re
import sys


def _payload_text(payload: dict) -> str:
    parts = [
        str(payload.get("command") or ""),
        str(payload.get("cmd") or ""),
        str(payload.get("cwd") or ""),
    ]
    tool_input = payload.get("tool_input") or {}
    parts.extend(
        [
            str(tool_input.get("command") or ""),
            str(tool_input.get("file_path") or ""),
            str(tool_input.get("path") or ""),
        ]
    )
    return " ".join(parts)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    text = _payload_text(payload)
    warnings = [
        (r"\.env", "Do not read or print .env files or secrets."),
        (r"data/(raw|private)", "Raw or private data require explicit human approval."),
        (
            r">\s*examples/card-krueger/data/synthetic_fast_food_panel\.csv\b",
            "The Card-Krueger teaching CSV should not be overwritten by harness tasks.",
        ),
        (r"\brm\s+-rf\b", "Recursive force deletion requires explicit human approval."),
    ]

    for pattern, reason in warnings:
        if re.search(pattern, text):
            print(json.dumps({"message": f"Research safety policy warning: {reason}"}))
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
