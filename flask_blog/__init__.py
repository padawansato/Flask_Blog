from flask import Flask

app = Flask(__name__)       # アプリケーション本体作成
app.config.from_object('flask_blog.config')     # configとして読み込む宣言

import flask_blog.views     # viewをインポート

