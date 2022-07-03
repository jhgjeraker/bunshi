# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

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


def draw_horisontal(string: str):
    print(string)
    n = len(string)
    rows = []

    row = 0
    for i in range(n):
        # Reverse the order to allow for simpler drawing.
        column = n - i - 1

        breakdown_entry = bunshi.breakdown(string[column])
        if breakdown_entry is None:
            continue

        # The columns is multiplied by 2 to account for full-width chars.
        rows = _draw_horisontal_branch(rows, column*2, breakdown_entry)

    for row in rows:
        print(''.join(row))


def draw_breakdown(entry):
    # Currently, only one drawing method is supported.
    draw_horisontal(entry)
