from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from admin import app
from lib.models import Book,Borrowbook

from lib.db import init_db


book = Blueprint('book', __name__)

from functools import wraps
import statistics
#今借りているものを表示
# @app.route('/')
# @book.route('/borrowbook')
# @login_check
def borrowbook():
    
    # user_id = request.form.get('user_id')
    user_id = '0000001'
    borrowbook = Borrowbook.query.order_by(Borrowbook.book_id.asc()).all()
    books = Book.query.order_by(Book.book_id.asc()).all()

    return render_template('book/book_borrow.html',borrowbook = borrowbook,user_id=user_id,books=books)
#貸し出し履歴
@book.route('/bookhistory')
# @login_checkS
def bookhistory():
    #接続テスト確認必要
    # user_id = request.form.get('user_id')
    user_id = '0000001'
    borrowbook = Borrowbook.query.order_by(Borrowbook.book_id.asc()).all()
    books = Book.query.order_by(Book.book_id.asc()).all()

    return render_template('book/book_history.html',borrowbook = borrowbook,user_id=user_id,books=books)
#おすすめ表示
#過去にかりたものもおすすめとして表示されてしまう 変更予定
# @app.route('/')
@book.route('/bookrecommend')

# @login_check
def recommend():
    
    # user_id = request.form.get('user_id')
    user_id = '0000001'
    borrowbook = Borrowbook.query.order_by(Borrowbook.book_id.asc()).all()
    books = Book.query.order_by(Book.book_id.asc()).all()
    genrelist = []
    for book2 in books :
        for book in borrowbook:
            if user_id == book.user_id :

                if book.book_id == book2.book_id :
                    genre = book2.book_genre
                    genrelist.append(genre)
                    mostgenre = statistics.mode(genrelist)
                   

    return render_template('/book/recommend.html',borrowbook = borrowbook,user_id=user_id,books=books,mostgenre=mostgenre)
