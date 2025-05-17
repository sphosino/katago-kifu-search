# 🎮 KataGo棋譜検索システム

HSP3で開発されたKataGo-rating-gamesの棋譜閲覧ツール。KataGoの自己対戦棋譜の棋譜を検索、閲覧できます。

ダウンロードはこちらから→[https://github.com/sphosino/katago-kifu-search/releases]

[![GitHub license](https://img.shields.io/github/license/sphosino/katago-kifu-search)](LICENSE)
[![HSP3](https://img.shields.io/badge/HSP-3.6+-brightgreen)](https://hsp.tv/)

<img src="docs/screenshot.png" width="600" alt="スクリーンショット">
<sub>※開発中の画面です</sub>

## 🍎️ 機能一覧
- 棋譜の自動再生（一手ごとの時間を複数のパラメータで調整）
- パターンによる複雑な局面検索
- 棋譜出力（SGF、ファイル）
- Katago公式サイトから最新棋譜取得
  
---
## 🚀 開発者向けクイックスタート

### 🛠 必要条件
- HSP3.6以上

### インストール
```bash
## セットアップ手順

1. リポジトリをクローンします：（別フォルダに分ける）

git clone https://github.com/sphosino/katago-kifu-search.git
git clone https://github.com/sphosino/hsp_common.git

2. 以下のように同じ階層に配置してください。　
root/
   ├── katago-kifu-search/
   └── hsp_common/

3.hsp_commonの中にあるgenerate_headers.hsp を一度実行してください。
    これでall_includeというファイルがhsp_common内の各フォルダ内に生成されます。

katago-kifu-searchフォルダのmain.hspが実行できるようになっていればインストール完了！
```

## 📂 開発時のおすすめディレクトリ構成(例）
```plaintext
root/
├── hsp_common/     ← 共通ライブラリ（別リポジトリ、下にリンクあります）
│   ├── basic_module1.hsp
│   ├── basic_module2.hsp
│   └── basic_module3.hsp
├── katago-kifu-search/　←このリポジトリ
│    ├── main.hsp
│    └── modules/
│       ├── p1_module1.hsp
│       └── p1_module2.hsp
│
└──その他プロジェクトのリポジトリ
```
hsp_commonのリポジトリは[こちら](https://github.com/sphosino/hsp_common)

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
---
開発の進捗や技術メモは[開発日誌](https://sphosino.github.io/katago-kifu-search)にまとめています。
