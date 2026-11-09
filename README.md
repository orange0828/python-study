# python-study

安全开发方向的学习记录：语法练习 + 边学边写的小工具。

不追求数量，只记录每天实际写出来的东西。每个练习都以「能独立跑通」为准，不以「看完了」为准。

## 进度

| 阶段 | 内容 | 状态 |
|---|---|---|
| Day01 | 环境搭建、第一个程序 | ✅ |
| Day02 | 第一个 Python 程序 | ✅ |
| Day03 | 变量、类型、类型转换 | ✅ |
| Day04 | 运算符、`//` 与 `%` | 进行中 |
| Day05– | 分支、循环、数据结构、函数、文件 | 待开始 |

## 目录

```
python-study/
├── grep.py            # 命令行文本检索工具（练习转工具的第一个）
├── test.log           # grep.py 的测试数据
├── exercises/         # 按天归档的语法练习
│   ├── day03_01_types.py
│   ├── day03_02_base_convert.py
│   ├── day03_03_char_code.py
│   ├── day03_04_fahrenheit.py
│   ├── day03_05_bmi.py
│   └── day03_06_swap.py
└── .gitignore
```

## grep.py

命令行文本检索：按关键词查找文件中的匹配行，输出行号与内容。

```bash
py grep.py test.log error
```

```
3: error: timeout
7: error: disk full
共匹配 2 行
```

出错时的行为：

```bash
py grep.py                      # 用法: py grep.py 文件路径 关键词   （退出码 1）
py grep.py nofile.txt abc       # 文件不存在：nofile.txt             （退出码 1）
```

设计上的两点说明：

- `search(path, keyword)` 只返回数据、不打印，输出与退出码由调用方处理 —— 便于后续用 pytest 断言
- 文件不存在返回 `None`，匹配为空返回 `[]`，两种情况可区分

## 环境

- Python 3.14.7
- VS Code + Python 扩展
- Windows 11

## 说明

`exercises/` 下是按天归档的语法练习，属于学习痕迹，不是成品。
根目录只放已成型的脚本；某个脚本功能变复杂后，会单独拆成独立仓库。
