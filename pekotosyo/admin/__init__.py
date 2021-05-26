from flask import Flask

app = Flask(__name__)

app.config.from_object('admin.config')

app.config.from_object('lib.config')

init_db(app)

from admin.views import views_top.py views_kids_reserve.py views_book.py views_money.py views_staff.py

