"""
This module provides some helper functions.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""


def fix_json(s: str) -> str:
    """Fix malformed JSON from the device by escaping internal quotes."""
    # Find all indices of "
    indices = [i for i, char in enumerate(s) if char == '"']
    if not indices:
        return s

    # We want to keep only those that are delimiters.
    to_escape = []
    for i in indices:
        is_start = (
            (i == 1)
            or (i > 1 and s[i - 1] == " " and s[i - 2] == ",")
            or (i > 0 and s[i - 1] == ",")
        )
        is_end = (
            (i == len(s) - 2)
            or (i < len(s) - 2 and s[i + 1] == "," and s[i + 2] == " ")
            or (i < len(s) - 1 and s[i + 1] == ",")
        )

        if not (is_start or is_end):
            to_escape.append(i)

    # Reconstruct
    result = list(s)
    for i in reversed(to_escape):
        result.insert(i, "\\")
    return "".join(result)
