from flask import render_template, request, url_for, session, redirect, flash, Blueprint

from lib.db import db

reserve = Blueprint('reserve',__name__)

# 保育予約画面を表示
@reserve.route('/')
def index():
    return render_template('kid_reserve/reserve.html',users_id = users_id)

# 