# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import bunshi.draw as draw
import bunshi.inout as inout


def main():
    args = inout.parse_arguments()
    draw.draw_breakdown(args.entry)


def entry_point() -> None:
    main()
