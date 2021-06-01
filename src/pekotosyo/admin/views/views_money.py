from flask import render_template, request, url_for, session, redirect,flash, Blueprint

from admin import app

from lib.models import Cardinfo, Cardhistory, Users

from lib.db import db

from functools import wraps

import datetime

money = Blueprint('money',__name__)

#電子マネーホーム
@money.route('/')
def index():
    return render_template('money/money_menu.html')

#---------------------------------------------------------------

#口座登録の画面表示
@money.route('/card')
def money_card():
    return render_template('money/card.html')


#クレジットカード情報受信POST useridと入力内容を挿入。
@money.route('/card', methods=['POST'])
def card_info():
    card_number=request.form.get('card_number')
    card_key=request.form.get('card_key')
    card_date=request.form.get('card_date')
    card_name=request.form.get('card_name')

    cardinfo = Cardinfo.query.all()
    if user_log == cardinfo.user_id:
        if card_number and card_key and card_date and card_name:
        info = Cardinfo(
            user_id=sesseion.get('user_log')
            card_number=request.form.get('card_number'),
            card_key=request.form.get('card_key'),
            card_date=request.form.get('card_date'),
            card_name=request.form.get('card_name'),
            user_money= user_money + ca
        )
        db.session.add(info)
        db.session.commit()
        return render_template('money/card_check.html')
    
    if card_number and card_key and card_date and card_name:
        info = Cardinfo(
            user_id=sesseion.get('user_log')
            card_number=request.form.get('card_number'),
            card_key=request.form.get('card_key'),
            card_date=request.form.get('card_date'),
            card_name=request.form.get('card_name'),
            user_money=0
        )
        db.session.add(info)
        db.session.commit()
        return render_template('money/card_check.html')
    else:
        # return render_template('money/money_menu.html')
        return redirect('money/money_menu.html')

# #-----------------------------------------------------------------

# #チャージ画面を表示。
@money.route('/charge')
def money_charge():
    return render_template('money/charge.html')


# #チャージ金額を受信POST　IDを取得してそれとチャージ金額を登録。
@money.route('/charge',methods=['POST'])
def charge():
    chargemoney=request.form.get('chargemoney')
    history_date=datetime.date
    if chargemoney and history_date:
        history = Cardhistory(
            chargemoney=request.form.get('chargemoney'),
            userid='00000001',
            history_date=datetime.date
        )
        db.session.add(history)
        db.session.commit()
        return render_template('money/charge_check.html',history=history)
    else:
        return redirect('money/money_menu.html')
# #--------------------------------------------------------------------

# #チャージ履歴の画面を表示。IDを取得してそれと一致するレコードをリストで渡す
@money.route('/history', methods=['GET'])
def charge_history():   #get ID
    userid = '00000001'
    histories = Cardhistory.query.order_by(Cardhistory.user_id.asc()).all()
    list = []
    if user_id == histories.user_id:
        chargemoney2 = histories.chargemoney

        list.append(chargemoney2)
        summoney = sum(list)

    # histries = Cardhistory.query.filter(Users.user_id==userid).all()
    return render_template('money/charge_history.html', histories=histories, userid='00000001',sum)


