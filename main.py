# This file is part of bunshi, a kanji breakdown cli.
# License: GNU GPL version 3, see the file "LICENCE" for details.

import os
import re
from typing import Tuple
import unicodedata

import yaml
import pandas as pd


def load_config() -> dict:
    with open('config.yaml', 'r') as f:
        cfg = yaml.full_load(f)
    return cfg


def format_krad_line(line: str) -> Tuple[str, list[str]]:
    split = line.split(' : ')
    return split[0], split[1].replace('\n', '').split(' ')


def load_kradfile(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f'Kradfile not found at path {path}.'
        )

    rows = []
    p = re.compile('.\\s:\\s')
    with open(path, 'r') as f:
        raw_kradfile = f.readlines()
        for line in raw_kradfile:
            if not p.match(line):
                continue

            # The kradfile format is not amazing for DataFrames, so we
            # do a little formatting before appending the rows list.
            kanji, components = format_krad_line(line)

            # We expand components list to map one kanji row one component.
            rows += [[kanji, component] for component in components]

    return pd.DataFrame(rows, columns=['kanji', 'component'])


def load_jouyou(path: str):
    return pd.read_csv(path, index_col='id')


def load_kangxi(path: str):
    return pd.read_csv(path, index_col='id')


def join(kradfile, jouyou, kangxi):
    df = kradfile.merge(
        jouyou[[
            'kanji',
            'kanji_meaning',
            'kanji_strokes',
            'kanji_readings',
        ]],
        on='kanji',
        how='left',
    ).merge(
        kangxi[[
            'component',
            'component_meaning',
        ]],
        on='component',
        how='left',
    )

    # Remove english readings from the kanji_readings column.
    # This is done by check if each character is fullwidth.
    def prune_halfwidth(x: str):
        out = ''

        if not isinstance(x, str):
            return x

        for symbol in x:
            if unicodedata.east_asian_width(symbol) == 'W':
                out += symbol
        return out

    df['kanji_readings'] = df['kanji_readings'].apply(
        lambda x: prune_halfwidth(x)
    )

    # Some components are equivilent to kanji, so we add the
    # jouyou meanings to the relevant components.
    k = df.merge(
        jouyou.set_index('kanji')['kanji_meaning'].rename('component_meaning'),
        left_on='component',
        right_index=True,
        how='left',
    )[[
        'component_meaning_x',
        'component_meaning_y',
    ]]

    # Combine kangxi- and jouyou component meanings, prioritizing
    # the kangxi meaning if it exists.
    df['component_meaning'] = k['component_meaning_x'].combine_first(
        k['component_meaning_y'],
    )

    # Reorder columns in DataFrame in a kanji -> component order.
    df = df[[
        'kanji',
        'kanji_meaning',
        'kanji_readings',
        'kanji_strokes',
        'component',
        'component_meaning',
    ]]

    return df[~df['kanji_meaning'].isna()]


def main():
    cfg = load_config()

    # Load each asset into individual DataFrames.
    kradfile_df = load_kradfile(cfg['kradfile']['relative_path'])
    jouyou_df = load_jouyou(cfg['jouyou']['relative_path'])
    kangxi_df = load_kangxi(cfg['kangxi']['relative_path'])

    # A series of left-joins produces the final DataFrame.
    df = join(kradfile_df, jouyou_df, kangxi_df)
    # print(df[df['component_meaning'].isna()])

    # Write to .tsv without index as some entries include comma.
    df.to_csv(cfg['output']['save_path'], index=False, sep='\t')


if __name__ == '__main__':
    main()
