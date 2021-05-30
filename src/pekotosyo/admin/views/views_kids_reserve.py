from flask import render_template, request, url_for, session, redirect, flash, Blueprint

# reserveモデルを取得
from lib.models import Users, Reserve

# SQLAlchemyを取得
from lib.db import db

from admin import app

# Blueptintでreserveアプリケーションを登録
kid_reserve = Blueprint('kid_reserve', __name__)

# 保育予約画面を表示
@kid_reserve.route('/')
def reserve():
    # ログインのメソッドをいれる
    return render_template('kid_reserve/reserve.html')

@kid_reserve.route('kid_reserve/reserve_check', methods=["POST"])
def reserve_check():
    # ログインのメソッドがいる
    # return render_template('kid_reserve/reserve_check.html')
    reserve_date = request.form.get('reserve_date')
    reserve_name = request.form.get('reserve_name')
    items = request.form.getlist('items')   

# 借りるおもちゃを選択
    selected_items = ""
    if len(items) !=0:
        for items in items:
            if items == "item":
                selected_items += "知育おもちゃ"
            elif items == "anime":
                selected_items += "アニメ"
            elif items == "noitem":
                selected_items += "借りるおもちゃはありません"
            else:
                selected_items +="???"
                # 選択した内容を返す
    return render_template('kid_reserve/reserve_check.html', reserve_date=reserve_date, reserve_name=reserve_name, selected_items=selected_items )

