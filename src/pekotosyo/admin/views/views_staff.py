from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from admin import app
from lib.models import Book,Users
from lib.db import db

staff = Blueprint('staff', __name__)

from functools import wraps
#ユーザー追加



@staff.route('/staffuseradd')
# @login_check
def staffadd():
    return render_template('staff/user_add.html')
@staff.route('/useradd',methods=['POST'])
def useradd():
    user_id = request.form.get('user_id')
    user_name = request.form.get('user_name')
    password = request.form.get('password')


    if user_id and user_name and password:
        user = Users(
            user_id = request.form.get('user_id'),
            user_name = request.form.get('user_name'),
            password = request.form.get('password'),
            )
        db.session.add(user)
        db.session.commit()
        return render_template('staff/user_addresult.html')
    else:
        
        return render_template('staff/user_addfalut.html')


# #ユーザー一覧
# @app.route('/')
@staff.route('/userlist')
# @login_check
def userlist():
    users = Users.query.order_by(Users.user_id.asc()).all()
    return render_template('staff/user.html',users = users)


###本の一覧
@staff.route('/booklist')
# @app.route('/')
# @login_check
def booklist():
    books = Book.query.order_by(Book.book_id.asc()).all()
    return render_template('staff/book_list.html',books = books)

