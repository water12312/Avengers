from flask import render_template, request, url_for, session, redirect, flash, Blueprint

from admin import app

from lib.models import Users, Book

from lib.db import db

from functools import wraps

mypage = Blueprint('mypage', __name__)

# book_reserveに飛ばす
@mypage.route('/book_reserve')
def book_reserve(user_id):
    id_send = Users.query.get(user_id)
    return render_template('book_reserve.html', user_id=id_send)

# kid_reserveに飛ばす
@mypage.route('/kid_reserve')
def kid_reserve():
    return render_template('kid_reserve.html')

# moneyに飛ばす
@mypage.route('/money')
def money():
    return render_template('money.html')

# book_recommendに飛ばす
@mypage.route('/book_recommend')
def book_recommend():
    return render_template('book_recommend')



# flashで期限が迫っている場合、知らせを表示する
# @mypage.route('/result', methods=['POST'])
# def result():
#     item = request.form.get('item')
#     items = [('精霊の守り人','ファンタジー'), ('月の影　影の海','ファンタジー'), ('空の中','SF'), ('ジョーカーゲーム', 'サスペンス')]
#     genre = 'は未登録です'
#     for row in items:
#         if row[0] == item:
#             genre = row[1] + 'ジャンル'
#     return '<p>「{0}」 {1}</p>'.format(item, genre)

@mypage.route('/result', methods={'POST'})
def result():
    search_name = request.form.get('item')
    book = Book.query.filter_by(book_name=search_name).first()
    # genre_express = Books.query.filter_by()
    if not book:
        # genre_result = Book.query.filter_by(genre).first()
        # return render_template('book_search.html', genre_result=genre_result)
        return render_template('mypage.html')
        
    else:
        return render_template('book_search.html', book=book)
        
        
        # print('その商品はありません')
    


