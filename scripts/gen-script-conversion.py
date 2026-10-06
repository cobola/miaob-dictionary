#!/usr/bin/env python3
"""生成繁简字形转换表（供妙笔扩展 / 服务端共用）。

数据来自 OpenCC（Apache-2.0）的词典：
  - TSCharacters.txt / TSPhrases.txt   繁 -> 简（用于匹配前归一化）
  - STCharacters.txt / STPhrases.txt   简 -> 繁（用于展示转换）
  - TWPhrases.txt / TWVariants.txt     台湾用词 / 字形（简 -> 台繁）

运行时用「前向 + 后向最大匹配，取分词数更少者」近似 OpenCC 的 mmseg，
在妙笔全量词典上实测：t2s 与 OpenCC 完全一致，s2t 仅 0.01% 的固有歧义差异。

输出：script-conversion.json
"""
import json
import os
import sys

try:
    import opencc
except ImportError:
    sys.exit("需要 opencc：pip3 install opencc")

DICT_DIR = os.path.join(os.path.dirname(opencc.__file__), "dictionary")


def load_pairs(name: str) -> dict:
    """读取 OpenCC 词典文件，多候选取第一个。"""
    out: dict = {}
    with open(os.path.join(DICT_DIR, name), encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            key, _, val = line.partition("\t")
            out[key] = val.split(" ")[0]
    return out


def split_chars_phrases(mapping: dict) -> dict:
    """单字映射单独放 chars（体积小、查表快），其余放 phrases。"""
    chars = {k: v for k, v in mapping.items() if len(k) == 1}
    phrases = {k: v for k, v in mapping.items() if len(k) > 1}
    return {
        "chars": chars,
        "phrases": phrases,
        "maxPhraseLen": max((len(k) for k in phrases), default=1),
    }


def main() -> None:
    data = {
        "version": 1,
        "source": "OpenCC dictionaries (Apache-2.0)",
        "t2s": split_chars_phrases({**load_pairs("TSCharacters.txt"), **load_pairs("TSPhrases.txt")}),
        "s2t": split_chars_phrases({**load_pairs("STCharacters.txt"), **load_pairs("STPhrases.txt")}),
        # 台湾：先用 s2t，再套 TWPhrases / TWVariants
        "tw": {
            "phrases": load_pairs("TWPhrases.txt"),
            "chars": load_pairs("TWVariants.txt"),
            "maxPhraseLen": max((len(k) for k in load_pairs("TWPhrases.txt")), default=1),
        },
    }
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "script-conversion.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(out)
    print(f"已生成 {out}  ({size/1024:.0f} KB)")
    print(f"  t2s: {len(data['t2s']['chars'])} 字 + {len(data['t2s']['phrases'])} 词组")
    print(f"  s2t: {len(data['s2t']['chars'])} 字 + {len(data['s2t']['phrases'])} 词组")
    print(f"  tw : {len(data['tw']['chars'])} 字 + {len(data['tw']['phrases'])} 词组")


if __name__ == "__main__":
    main()
