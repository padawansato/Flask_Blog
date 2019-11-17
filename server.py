"""これは起動ファイル　つまり　'python server.py'で起動する"""
from flask_blog import app      # initで作成したappをインポート

if __name__ == '__main__':
    app.run() # デバッグモードでエラーが詳細に