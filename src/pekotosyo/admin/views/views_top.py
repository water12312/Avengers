
from flask import render_template, request, url_for, session, redirect, flash, Blueprint

from admin import app

from lib.models import Users

from lib.db import db

from functools import wraps

top = Blueprint('top', __name__)


def login_check(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            flash('ログインしてください','error')
            return redirect(url_for('top'))
        return view(*args,**kwargs)
    return inner

@top.route('/')
@login_check
def mypage():
    user_name = session.get("user_in")
    user_id = session.get("user_log")
    return render_template('mypage.html',user_name=user_name, user_id=user_id)


@top.route('/top', methods=['GET', 'POST'])
def top2():
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
            return redirect(url_for('mypage'))
    return render_template('top.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_in', None)
    flash('ログアウトしました', 'success')
    return render_template('top.html')


