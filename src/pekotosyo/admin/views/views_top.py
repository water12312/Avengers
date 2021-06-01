
from flask import render_template, request, url_for, session, redirect, flash, Blueprint

from admin import app
# Users、データベースを取得
from lib.models import Users
from lib.db import db

#デコレータを使用
from functools import wraps

# blueprintでアプリケーションを登録
top_page = Blueprint('top_page', __name__)

# ログイン機能
def login_check(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            flash('ログインしてください','error')
            return redirect(url_for('top_page.top'))
        return view(*args,**kwargs)
    return inner

# myppegeへの遷移、ログイン
@top_page.route('/mypage')
@login_check
def mypage():
    user_name = session.get("user_in")
    user_id = session.get("user_log")
    return render_template('mypage.html', user_name=user_name, user_id=user_id)

@top_page.route('/staff')
@login_check
def staff():
    return render_template('staff/staff.html')


@top_page.route('/', methods=['GET', 'POST'])
def top():
    if request.method== 'POST':

        user_id = request.form.get('user_id')
        password = request.form.get('password')

        user = Users.query.filter_by(user_id=user_id).first()
        passcheck = Users.query.filter_by(user_id=user_id).filter_by(password=password).first()


        # if request.form.get('user_id') != app.config['USER_ID']:
        if not user:
            flash('ユーザーIDが異なります', 'error')
        # elif request.form.get('password') != app.config['PASSWORD']:
        if not passcheck:
            flash('パスワードが異なります', 'error')
        else:
            session['logged_in'] = True
            session['user_in'] = user.user_name
            session['user_log'] = user.user_id
            flash('ログインしました', 'success')
            user_id = session.get('user_log')
            if user_id == '00000011':
                 return redirect(url_for('top_page.staff'))
            else:
                return redirect(url_for('top_page.mypage'))
    return render_template('top.html')



@top_page.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_in', None)
    flash('ログアウトしました', 'success')
    return render_template('top.html')
