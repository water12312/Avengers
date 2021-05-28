# Flaskの必要項目をインポート
from flask import render_template, request, url_for, session, redirect, flash, Blueprint

# reserveモデルを取得
from lib.models import Users, Reserve

# SQLAlchemyを取得
from lib.db import db

# from practice import app
# Blueptintでreserveアプリケーションを登録
reserve = Blueprint('reserve', __name__)

# 保育予約画面を表示
@app.route('/reserve')
def reserve():
    # ログインのメソッドをいれる
    return render_template('/reserve.html')
    #  users_id = users_id

# フォームの内容を取ってくる
@app.route('/reserve_check', methods=["POST"])
def reserve_check():
    # ログインのメソッドがいる
    reserve = Reserve(
        reserve_date = request.form.get('reserve_date')
        reserve_name = request.form.get('reserve_name')
        items = request.form.getlist('items')   
    )

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
    return render_template('reserve_check.html', reserve_date=reserve_date, reserve_name=reserve_name, selected_items=selected_items )
