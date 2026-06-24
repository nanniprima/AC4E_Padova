#!/usr/bin/env python3
"""Cursor hook example: remind the agent to leave reviewable evidence."""

from __future__ import annotations

import json


print(
    json.dumps(
        {
            "message": (
                "Before claiming completion, summarize files changed, commands run, "
                "data/caveat consistency, and remaining human checks."
            )
        }
    )
)
