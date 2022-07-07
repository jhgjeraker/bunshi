# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import argparse

import bunshi


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Bunshi is a small tool for decomposing kanji.'
    )

    parser.add_argument(
        'entry',
        type=str,
        help='kanji, word, or sentence (full-wdith)',
    )
    parser.add_argument(
        '--breakdown',
        type=str,
        help='path to custom breakdown file',
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='breakdown json output',
    )

    return parser.parse_args()


def entry_point() -> None:
    args = parse_arguments()

    if args.breakdown is not None:
        bunshi.BREAKDOWN_PATH = args.breakdown

    rows = bunshi.draw.draw_breakdown(args.entry, args)

    for row in rows:
        print(row)
