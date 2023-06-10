# データ解析Webアプリケーション

## 概要

このアプリケーションは、Web UIを介してデータ解析を実行します。データベースのCSVファイルを取り扱い、そのデータを視覚的にプロットします。

## 特徴

* Web UIからのデータ解析
* CSVデータのプロット
* インタラクティブなデータビジュアライゼーション

## 技術スタック

* Next.js - フロントエンドフレームワーク
* Flask - サーバーサイドフレームワーク
* Plotly - データの視覚化

## インストール方法

本プロジェクトをクローンし、依存関係をインストールします：

```bash
$ git clone <repository_url>
$ cd <repository_name>
$ npm install
$ pip install -r requirements.txt
```

## 使用方法

サーバーサイドアプリケーションとクライアントサイドアプリケーションを別々に起動します：

```bash
# サーバーサイド
$ python server/run.py

# クライアントサイド (別のターミナルで実行)
$ npm run dev
```
その後、ブラウザで http://localhost:3000 を開いてください。