"""このファイルでは、http://127.0.0.1:5000にリクエストがあったときの処理を書いている"""
from flask_blog import app

@app.route('/')
def show_entries():             # # http://127.0.0.1:5000にリクエストがあった時、以下のメソッドが呼び出される
    return "Hello World!"