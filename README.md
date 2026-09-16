# 妙笔词典数据

中文成语、名句、歇后语词典数据，供妙笔浏览器插件及其他项目使用。

## 数据概览

| 文件 | 条目数 | 说明 |
|------|--------|------|
| `idiom-dict.json` | 31,010 | 成语词面索引（不含解释、例句或其他详情） |
| `quotes.json` | 8,936 | 经典名句（含出处、作者） |
| `xiehouyu.json` | 14,031 | 歇后语（谜面+谜底） |
| `qianziwen.json` | 1 | 《千字文》全文（250句、繁简字集、拼音、异文） |
| `vocabulary-index.json` | 5 组 | HSK 与中小学常用词的词面索引（不含解释） |

## 数据来源

- 成语：[chinese-xinhua](https://github.com/pwxcoo/chinese-xinhua) 项目组
- 名句：[jingmo](https://github.com/jingmejingmo) 项目组
- 歇后语：综合整理

## 数据格式

### 成语 (idiom-dict.json)

```json
{
  "守株待兔": ""
}
```

这里只公开成语词面索引。解释、例句、出处等详情由网站服务端单独维护。

### 名句 (quotes.json)

```json
[
  {
    "text": "山有木兮木有枝，心悦君兮君不知",
    "from": "佚名《越人歌》"
  }
]
```

### 歇后语 (xiehouyu.json)

```json
[
  {
    "riddle": "愚公移山",
    "answer": "非一日之功"
  }
]
```

### 分级词汇 (vocabulary-index.json)

仅包含词面和分组，用于阅读覆盖率统计；不包含解释、例句或其他详情。当前为初始索引，不代表任何官方分级词表的完整全集。

## 协议

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) — 署名-相同方式共享 4.0 国际

您可以：
- 共享、改编、用于任何目的（包括商业用途）
- 只需署名并以相同方式共享

## 相关项目

- [妙笔插件](https://github.com/cobola/miaob-extension) — 中文网页阅读增强 Chrome 扩展
