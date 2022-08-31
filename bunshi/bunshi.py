# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

from typing import Optional

import bunshi

KANJI_DICT = None


def _load_cjk_breakdown(path: str):
    breakdown = dict()

    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            columns = line.split('\t')
            columns[-1] = columns[-1].replace('\n', '')

            # breakdown.tsv has the following column indices
            # 0, key
            # 1, meaning
            # 2, readings
            # 3, breakdown

            breakdown[columns[0]] = {
                'key': columns[0],
                'meaning': columns[1],
                'readings': columns[2],
                'breakdown': columns[3],
            }

    return breakdown


def breakdown(symbol: str) -> Optional[dict]:
    # Lazyload breakdown dictionary if necessary.
    global KANJI_DICT
    if KANJI_DICT is None:
        KANJI_DICT = _load_cjk_breakdown(bunshi.BREAKDOWN_PATH)

    if symbol in KANJI_DICT:
        return {
            'meaning': KANJI_DICT[symbol]['meaning'],
            'readings': KANJI_DICT[symbol]['readings'],
            'breakdown': _rec(symbol, KANJI_DICT),
        }
    else:
        return None


def _rec(local_key: str, key_map: dict):
    local_breakdown = {}
    if local_key not in key_map:
        return local_breakdown

    for component in key_map[local_key]['breakdown'].split(','):
        if component == local_key or component not in key_map:
            continue

        local_breakdown[component] = {
            'key': local_key,
            'meaning': key_map[component]['meaning'],
            'readings': key_map[component]['readings'],
            'breakdown': _rec(component, key_map),
        }

    return local_breakdown
