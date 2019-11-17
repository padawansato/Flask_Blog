"""このファイルでは、http://127.0.0.1:5000にリクエストがあったときの処理を書いている"""
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():             # # http://127.0.0.1:5000にリクエストがあった時、以下のメソッドが呼び出される
    return render_template('entires/index.html') # flaskではtemplatesはhtmlがあると自動で認識するため