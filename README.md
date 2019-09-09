# Django チュートリアルのサンプルアプリケーション

## 使い方

このアプリケーションを動かす場合は、まずはリポジトリを手元にクローンしてください。
その後、次のコマンドで必要になるライブラリをインストールします。

```
$ pip install -r requirements.txt
```

その後、Dockerコンテナをビルドします。

```
$ docker-compose build web
```

最後に、サーバーを起動してください。

```
$ docker-compose up web
```