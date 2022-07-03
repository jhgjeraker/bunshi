# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import bunshi.inout as inout


def _draw_down_symbol(col: int, kanji: dict, rows: list) -> list[str]:
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


def draw_down(entry, breakdown):
    print(entry)
    rows = []

    row = 0
    n = len(entry)
    for i in range(n):
        col = n - i - 1
        symbol = entry[col]

        if symbol in breakdown:
            rows = _draw_down_symbol(col*2, breakdown[symbol], rows)

    for row in rows:
        print(''.join(row))


def draw_breakdown(entry):
    breakdown = inout._load_breakdown()
    # Currently, only one drawing method is supported.
    draw_down(entry, breakdown)
