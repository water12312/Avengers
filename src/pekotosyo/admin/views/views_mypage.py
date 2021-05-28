from flask import render_template, request, url_for, session, redirect, flash, Blueprint

from admin import app

from functools import wraps

mypage = Blueprint('mypage', __name__)

# book_reserveに飛ばす
@app.route('/book_reserve')
def book_reserve():
    return render_template('book_reserve.html')

# kid_reserveに飛ばす
@app.route('/kid_reserve')
def kid_reserve():
    return render_template('kid_reserve.html')

# moneyに飛ばす
@app.route('/money')
def money():
    return render_template('money.html')

# book_recommendに飛ばす
@app.route('/book_recommend')
def book_recommend():
    return render_template('book_recommend')



# flashで期限が迫っている場合、知らせを表示する
@app.route('/result', methods=['POST'])
def result():
    item = request.form.get('item')
    items = [('精霊の守り人','ファンタジー'), ('月の影　影の海','ファンタジー'), ('空の中','SF'), ('ジョーカーゲーム', 'サスペンス')]
    genre = 'は未登録です'
    for row in items:
        if row[0] == item:
            genre = row[1] + 'ジャンル'
    return '<p>「{0}」 {1}</p>'.format(item, genre)

