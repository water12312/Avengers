from flask import Flask

from lib.db import init_db

app = Flask(__name__)

app.config.from_object('admin.config')
app.config.from_object('lib.config')

init_db(app)

from admin.views import views_money
# from admin.views import views_book, views_kids_reserve, views_money, views_staff,views_top

# app.register_blueprint(views_book.book, url_prefix='/book')
# app.register_blueprint(views_kids_reserve.kids_reserve, url_prefix='/kids_reserve')
app.register_blueprint(views_money.money, url_prefix='/money')
# app.register_blueprint(views_staff.staff, url_prefix='/staff')
# app.register_blueprint(views_top.top, url_prefix='/top')
