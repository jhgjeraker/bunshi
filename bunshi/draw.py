# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import json
from typing import Any

import bunshi


def draw_json(entry: str) -> list[str]:
    rows = []

    for i in range(len(entry)):
        breakdown_entry = bunshi.breakdown(entry[i])
        if breakdown_entry is None:
            continue

        breakdown_entry['key'] = entry[i]
        rows.append(json.dumps(breakdown_entry, indent=4))

    return rows


def draw_cjk_branch(rows, key, data, col, branch, level=0):
    # Insert a column pipe for each previous row.
    if level == 0:
        for i in range(len(rows)):
            rows[i][col] = '│'

    # Add readings only to level 0 entries.
    readings = '' if level > 0 else f' ─ {data["readings"]}'

    rows.append([' ' for _ in range(col)])
    rows[-1] += [f'{branch} {key}, {data["meaning"]}{readings}']

    # Connect the lower levels with a pipe if
    # necessary, but skip last section of each level.
    for i in range(1, level):
        if rows[-2][col-(2*(i))][0] in ['│', '├']:
            rows[-1][col-(2*(i))] = '│'

    for i, symbol in enumerate(data['breakdown']):
        rows = draw_cjk_branch(
            rows,
            symbol,
            data['breakdown'][symbol],
            col+2,
            '├' if i < len(data['breakdown']) - 1 else '└',
            level=level+1,
        )

    return rows


def draw_cjk(entry: str) -> list[str]:
    rows = []

    exists = []
    entry_nb = 1
    for i in range(len(entry)):
        column = len(entry) - i - 1

        key = entry[column]
        data = bunshi.breakdown(key)
        if data is None or key in exists:
            continue

        rows = draw_cjk_branch(rows, key, data, column*2, '└')
        exists.append(key)
        entry_nb += 1

    # Convert each row in the list to complete strings.
    output = []
    rows.insert(0, entry)
    for row in rows:
        output.append(''.join(row))

    return output


def draw_breakdown(entry: str, args: Any) -> list[str]:
    # Choose the appropriate method based on arguments.
    if args.json:
        return draw_json(entry)
    else:
        # return draw_horisontal(entry)
        return draw_cjk(entry)
