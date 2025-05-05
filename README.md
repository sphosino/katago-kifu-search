# 🎮 katago-kifu-search - KataGo棋譜分析ツール

HSP3で開発されたKataGo棋譜閲覧ツール。KataGoの自己対戦棋譜の棋譜を検索、閲覧できます。

[![GitHub license](https://img.shields.io/github/license/sphosino/katago-kifu-search)](LICENSE)
[![HSP3](https://img.shields.io/badge/HSP-3.6+-brightgreen)](https://hsp.tv/)

<img src="docs/screenshot.png" width="600" alt="スクリーンショット">
（注）開発中の画面です

## 🚀 クイックスタート

### 必要条件
- HSP3.6以上

### インストール
```bash
# 1. 基本モジュール
git clone --recurse-submodules https://github.com/sphosino/hsp_commmon.git

## 📂 ディレクトリ構造
```plaintext
root/
├── hsp_common/     ← 共通ライブラリ（別リポジトリ）（下にリンクあります）
│   ├── basic_module1.hsp
│   ├── basic_module2.hsp
│   └── basic_module3.hsp
└── katago-kifu-search/
    ├── main.hsp
    └── modules/
        ├── p1_module1.hsp
        └── p1_module2.hsp


```

開発には[hsp_common](https://github.com/sphosino/hsp_common)が必要です。



---
[開発日誌](https://sphosino.github.io/katago-kifu-search)
