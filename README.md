# Bunshi (分子)
Kanji can be broken down into basic components, much like molecules into atoms. Popular courses like [KKLC](https://keystojapanese.com/klc/), [RTK](https://en.wikipedia.org/wiki/Remembering_the_Kanji_and_Remembering_the_Hanzi), and [WaniKani](https://www.wanikani.com/) uses component mnemonics as a method of memorizing kanji, so learning them is quite useful.

Bunshi is a tiny tool for kanji component decomposition in the terminal. I made it mostly to fill a gap in my existing study technique, significantly reducing the friction associated with component lookup in the browser.

## Installation
Clone the repository and install from source.

```bash
pip install .
```

## Usage
Bunshi works with single kanji, words, or complete sentences.

```bash
bunshi これ便利ですね
```

Each kanji is shown with its meaning, On'yomi and Kun'yomi readings, and component breakdown.

```bash
これ便利だね
    │ └ 利, profit ─ リ、きく
    │   ├ 禾, grain
    │   │ ├ 丿, slash
    │   │ └ 木, tree
    │   └ 刂, knife
    └ 便, convenience ─ ベン、ビン、たより
      ├ 亻, man
      └ 更, grow late
        ├ 一, one
        ├ 日, day
        └ 乂,
          ├ 丿, slash
          └ 乀, slash
```
Note that the output is designed for monospace fonts. I had to adjust the output here as GitHub renders fullwidth at 1.5x (?) width, unlike terminals which use 2x.

## Custom Breakdowns
Bunshi can be configured with a custom breakdown using the following command, and expects the same format as found in `./bunshi/assets/breakdown.tsv`.

```bash
bunshi 列 --breakdown path/to/custom-breakdown.tsv
```

## Known Issues
- Names and readings not found in the Jouyou dataset are missing.
- Some unicode issues make a few components like `辶` render as a camera-icon, at least in my terminal.

## Asset Licence
Bunshi sources its breakdowns from `./assets/breakdown.tsv`, a remix of the work done by 3rd parties. Their efforts should not be attributed to me. The individual licences are listed below in an attempt at proper attribution.

- This publication has included material from the [CHISE project](http://www.chise.org/). License follows their terms.

- This project uses material from the Wikipedia article [Kangxi radical](https://en.wikipedia.org/wiki/Kangxi_radical), which is released under the [Creative Commons Attribution-Share-Alike License 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

- This project uses material from the Wikipedia article [List of jōyō kanji](https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji), which is released under the [Creative Commons Attribution-Share-Alike License 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

