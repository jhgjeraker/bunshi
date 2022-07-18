# Bunshi (分子)
Kanji can be broken down into basic components, much like molecules into atoms. Popular courses like [KKLC](https://keystojapanese.com/klc/), [RTK](https://en.wikipedia.org/wiki/Remembering_the_Kanji_and_Remembering_the_Hanzi), and [WaniKani](https://www.wanikani.com/) uses component mnemonics as a method of memorizing kanji, so learning them is quite useful.

Bunshi is a tiny tool for kanji component decomposition in the terminal. I made it mostly to fill a gap in my existing study technique, significantly reducing the friction associated with component lookup in the browser.

## Installation
Clone the repository and install from source.

```bash
pip install .
```

## Usage
Bunshi works with single kanji, words, or sentences.

```bash
bunshi この道具をごゆっくり楽しみください
```

Each kanji is shown with its meaning, On'yomi and Kun'yomi readings, and individual components.

```bash
この道具をごゆっくり楽しみください
    │ │          │
    │ │          └── 楽, pleasure ─ ガク、ラク、たのしい、たのしむ
    │ │              ├──────────────────────────────────────
    │ │              ├── 白, white
    │ │              ├── 木, tree
    │ │              └── 冫, ice
    │ │
    │ └── 具, tool ─ グ
    │     ├───────────
    │     ├── 一, one
    │     ├── ハ, fins
    │     └── 目, eye
    │
    └── 道, road ─ ドウ、トウ、みち
        ├───────────────────────
        ├── 辶, scooter
        ├── 自, self
        ├── 并, put together
        └── 首, head
```
Had to adjust the output here as GitHub renders fullwidth at 1.5x (?) width, unlike terminals which use 2x.

## Custom Breakdowns
The included breakdown is based on open-source assets and uses the offical [kangxi radicals](https://en.wikipedia.org/wiki/Kangxi_radical) as a basis for component names. While it would be great to include the breakdowns of both [KKLC](https://keystojapanese.com/klc/) and [WaniKani](https://www.wanikani.com/), I will not host their proprietary mnemonics and component names.

However, bunshi can be configured with a custom breakdown using the following command, so if you have bought either products you can, of course, use `./bunshi/assets/breakdown.tsv` as a reference and create your own mapping.

```bash
bunshi 列 --breakdown path/to/custom-breakdown.tsv
```

## Known Issues
- The breakdown is mostly generated through scripts and is incomplete. 
- Some unicode issues make a few components like `辶` render as a camera-icon, at least in my terminal.

## Asset Licence
Bunshi sources its breakdowns from `./assets/breakdown.tsv`, a remix of the work done by 3rd parties. Their efforts should not be attributed to me. The individual licences are listed below in an attempt at proper attribution.

- This publication has included material from the JMdict (EDICT, etc.) dictionary files in accordance with the licence provisions of the Electronic Dictionaries Research Group. See [http://www.edrdg.org/](http://www.edrdg.org/).

- This project uses material from the Wikipedia article [Kangxi radical](https://en.wikipedia.org/wiki/Kangxi_radical), which is released under the [Creative Commons Attribution-Share-Alike License 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

- This project uses material from the Wikipedia article [List of jōyō kanji](https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji), which is released under the [Creative Commons Attribution-Share-Alike License 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

