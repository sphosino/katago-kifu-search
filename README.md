# 🎮 KataGo棋譜検索システム

HSP3で開発されたKataGo-rating-gamesの棋譜閲覧ツール。KataGoの自己対戦棋譜の棋譜を検索、閲覧できます。

ダウンロードはこちらから→[KataGo棋譜検索システム](https://github.com/sphosino/katago-kifu-search/releases)

[操作方法](https://sphosino.github.io/katago-kifu-search/readme.html)

[![GitHub license](https://img.shields.io/github/license/sphosino/katago-kifu-search)](LICENSE)
[![HSP3](https://img.shields.io/badge/HSP-3.6+-brightgreen)](https://hsp.tv/)

<img src="docs/sum4.gif" width="600" alt="スクリーンショット">
<sub>※開発中の画面です</sub>

## 🍎️ 機能一覧
- 棋譜の自動再生（一手ごとの時間を複数のパラメータで調整）
- 局面検索
- 棋譜出力（SGF、ファイル）
- Katago公式サイトから最新棋譜取得
  
---
## 🚀 開発クイックスタート

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

4.katago-kifu-searchフォルダを開く。
  config_path.hsp を開いてDIRNAME ="C:...."という行を編集してください。リリース用のフォルダになります。
　開発中もこのフォルダのパスで起動します。
  フォルダの構成は現状以下のようになっています。
  release_root/
  ├── hspda.dll
  ├── hspext.dll
  ├── hspinet.dll
  ├── sub/
  │   ├── hspinet.dll
  │   ├── auto_download.exe
　│   ├── save_file_list.exe
  │   └── search_process.exe
  ├── title/
  │   └── ; 起動画面用画像フォルダ
  ├── 棋譜/
  │   └── ; デフォルトでプログラムが読み込むフォルダ
  └── save/
      └── ; 一時的に棋譜を保存するフォルダ

5. search_process.hsp, download_sgf.hsp,save_file_listをexe化して、subフォルダにいれる
6. dllも上記の通りに適切に入れる

7. main.hspがエラーなく実行できるようになっていればOKです。
8. main.hsp とconfig.hsp をexe化してrelease_rootに入れたら。フォルダはリリース可能な状態になっているはずです。

```


hsp_commonのリポジトリは[こちら](https://github.com/sphosino/hsp_common)

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
---
開発の進捗や技術メモは[開発日誌](https://sphosino.github.io/katago-kifu-search)にまとめています。
