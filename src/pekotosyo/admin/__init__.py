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

# from admin.views import views_money


from admin.views import views_book, views_kids_reserve, views_money, views_staff,views_top,views_mypage
# from admin.views import views_top, views_mypage, views_kids_reserve, views_money,views_book



app.register_blueprint(views_book.book, url_prefix='/book')
app.register_blueprint(views_kids_reserve.kid_reserve, url_prefix='/kid_reserve')
app.register_blueprint(views_money.money, url_prefix='/money')
app.register_blueprint(views_staff.staff, url_prefix='/staff')
app.register_blueprint(views_top.top_page, url_prefix='/')
app.register_blueprint(views_mypage.my_page, url_prefix='/mypage')
