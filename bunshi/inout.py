# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'entry',
        type=str,
        help='kanji, word, or sentence to breakdown',
    )

    return parser.parse_args()


def _load_breakdown():
    breakdown = dict()

    with open('assets/breakdown.tsv', 'r') as f:
        lines = f.readlines()

        for line in lines:
            columns = line.split('\t')
            columns[-1] = columns[-1].replace('\n', '')

            # breakdown.tsv has the following column indices
            # 0, kanji
            # 1, kanji_meaning
            # 2, kanji_readings
            # 3, kanji_strokes
            # 4, component
            # 5, component_meaning

            if columns[0] not in breakdown:
                breakdown[columns[0]] = {
                    'kanji': columns[0],
                    'meaning': columns[1],
                    'reading': columns[2],
                    'strokes': columns[3],
                    'components': {},
                }

            breakdown[columns[0]]['components'][columns[4]] = columns[5]

    return breakdown
