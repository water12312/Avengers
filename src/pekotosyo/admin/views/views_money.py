from flask import render_template, request, url_for, session, redirect,flash,Blueprint

from admin import app

from lib.models import Cardinfo, Cardhistory

from lib.db import db

from functools import wraps

money = Blueprint('money',__name__)

#電子マネーホーム
@money.route('/')
def index():
    return render_template('money/money_menu.html')

#口座登録
@money.route('/money/card')
def money_card():
    # user_id = session.get('user_id')
    return render_template('money/card.html')

#チャージ画面
@money.route('/money/charge')
def money_charge():
    return render_template('money/charge.html')


#チャージ履歴
@money.route('/money/history')
def charge_history():
    return render_template('money/charge_history.html')


#クレジットカード情報受信POST
@money.route('/money/card',methods=['POST'])
def card_info():
    info = Cardinfo(
        user_id=request.form.get('user_id'),
        card_number=request.form.get('card_number'),
        card_key=request.form.get('card_key'),
        card_date=request.form.get('card_date'),
        card_name=request.form.get('card_name'),
        user_money=0
    )
    try:
        db.session.add(info)
        db.session.commit()
    except:
        return render_template('money/money_menu.html')
    return render_template('money/card_check.html')
#チャージ金額を受信POST
@money.route('/money/charge',methods=['POST'])
def charge():
    user_money=request.form.get('chargemoney')
    return render_template('money/charge_check.html')


#チャージ履歴を送信GET


