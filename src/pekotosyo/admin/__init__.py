# Flaskのインポート
from flask import Flask

# init_dbのインポート
from lib.db import init_db

# Flaskのアプリケーション本体を作成して変数appに代入
app = Flask(__name__)

# config.pyを設定ファイルとして扱う
app.config.from_object('admin.config')
app.config.from_object('lib.config')

init_db(app)

from admin.views import views_top, views_mypage
