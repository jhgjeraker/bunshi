# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import argparse

import bunshi.draw as draw


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Bunshi is a small tool for decomposing kanji.'
    )

    parser.add_argument(
        'entry',
        type=str,
        help='kanji, word, or sentence (full-wdith)',
    )

    return parser.parse_args()


def entry_point() -> None:
    args = parse_arguments()
    draw.draw_breakdown(args.entry)
