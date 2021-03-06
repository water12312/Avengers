
from flask import render_template, request, url_for, session, redirect, flash, Blueprint

# reserveモデルを取得
from lib.models import Reserve, Users

# SQLAlchemyを取得
from lib.db import db

from admin import app

# Blueptintでreserveアプリケーションを登録
kid_reserve = Blueprint('kid_reserve', __name__)

# 保育予約画面を表示
@kid_reserve.route('/')
def reserve():
    # ログインのメソッドをいれる
    user_id = session.get('user_log')
    return render_template('kid_reserve/reserve.html' )

@kid_reserve.route('kid_reserve/reserve_check', methods=["POST"])
def reserve_check():
    # ログインのメソッドがいる
    user_id = session.get('user_log')
    # return render_template('kid_reserve/reserve_check.html')

    user_id = request.form.get('user_id')
    reserve_date = request.form.get('reserve_date')
    item = request.form.get('item')
    user_name = request.form.get('user_name')


    reserve_info = Reserve(
        user_id=request.form.get('user_id'),
        reserve_date = request.form.get('reserve_date'),
        item = request.form.get('item')  

    )  
    try:
        db.session.add(reserve_info)
        db.session.commit()
    except:
        return render_template('kid_reserve/reserve.html')
    return render_template('kid_reserve/reserve_check.html', reserve_date=reserve_date, user_id=user_id, user_name=user_name, item=item)

    


    # reserve_name = request.form.get('reserve_name')
    # items = request.form.getlist('items')  

    # return render_template('kid_reserve/reserve_check.html', reserve_date=reserve_date, user_id=user_id, item=item )

@kid_reserve.route('/reservehistory')
# @login_checkS
def reservehistory():
    #接続テスト確認必要
    user_id = session.get("user_log")
    # user_id = '0000001'
    reservehistory = Reserve.query.order_by(Reserve.user_id.asc()).all()
    

    return render_template('kid_reserve/reserve_history.html',reservehistory=reservehistory,user_id=user_id)