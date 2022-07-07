# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import json
from typing import Any

import bunshi


def _draw_horisontal_branch(rows: list, col: int, kanji: dict) -> list[str]:
    # Insert a column pipe for each existing row.
    for i in range(len(rows)):
        rows[i][col] = '│'

    # The base print is static and can be hardcoded directly.
    base = [' ' for _ in range(col)]
    rows.append(base + ['│'])
    rows.append(base + ['└── ', '{}, {} ─ {}'.format(
        kanji['kanji'],
        kanji['meaning'],
        kanji['reading'],
    )])

    # Indent the base by four spaces.
    base += [' ' * 4]

    # Add a separator between kanji and components. Purely visual.
    rows.append(base + ['├──', '─' * (
        4                               # whitespace and padding
        + len(kanji['kanji'])
        + len(kanji['meaning'])
        + (len(kanji['reading']) * 2)   # 2x for full-width characters
    )])

    # Iterate though and add each component branch.
    for i, component in enumerate(kanji['components']):
        meaning = kanji['components'][component]
        branch = '├── ' if i < len(kanji['components']) - 1 else '└── '
        rows.append(base + [branch, component, f', {meaning}'])

    return rows


def draw_horisontal(entry: str) -> list[str]:
    rows = []

    for i in range(len(entry)):
        # Reverse the order to allow for simpler drawing.
        column = len(entry) - i - 1

        breakdown_entry = bunshi.breakdown(entry[column])
        if breakdown_entry is None:
            continue

        # The columns is multiplied by 2 to account for full-width chars.
        rows = _draw_horisontal_branch(rows, column*2, breakdown_entry)

    # Convert each row in the list to complete strings.
    output = []
    rows.insert(0, entry)
    for row in rows:
        output.append(''.join(row))

    return output


def draw_json(entry: str) -> list[str]:
    rows = []

    for i in range(len(entry)):
        breakdown_entry = bunshi.breakdown(entry[i])
        if breakdown_entry is None:
            continue

        rows.append(json.dumps(breakdown_entry, indent=4))

    return rows


def draw_breakdown(entry: str, args: Any) -> list[str]:
    # Choose the appropriate method based on arguments.
    if args.json:
        return draw_json(entry)
    else:
        return draw_horisontal(entry)
