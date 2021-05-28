# Flaskのインポート
from flask import Flask

# init_dbのインポート
from lib.db import init_db

# Flaskのアプリケーション本体を作成して変数appに代入
app = Flask(__name__)

# config.pyを設定ファイルとして扱う
app.config.from_object('admin.config')
app.config.from_object('lib.config')

# dbの作成
init_db(app)

# 各ビューのインポート
from admin.views import views_kids_reserve

app.register_blueprint(views_kids_reserve.reserve, url_prefix='/views_kids_reserve')
