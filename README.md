# データ解析Webアプリケーション

## 概要

動悸や動作について記載しています。
Qiita：https://qiita.com/kaneda-masaya/private/7abc3355d1ddd9588110

このアプリケーションは、Web UIを介して効率的に研究データの解析を行うアプリケーションです。2次元系列データをインタラクティブなグラフを表示します。

## 技術スタック

* Next.js - フロントエンドフレームワーク
* Flask - サーバーサイドフレームワーク
* Plotly - データの視覚化

## インストール

本プロジェクトをクローンし、依存関係をインストールします：

```bash
$ git clone <repository_url>
$ cd <repository_name>
$ npm install
$ pip install -r requirements.txt
```

その後、以下で実行：

```bash
# サーバーサイド
$ python server/run.py

# クライアントサイド (別のターミナルで実行)
$ npm run dev
```

