from flask import render_template, request, url_for, session, redirect, flash, Blueprint

from admin import app

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

@app.route('/')
@login_check
def mypage():
    return render_template('mypage.html')


@app.route('/top', methods=['GET', 'POST'])
def top():
    if request.method== 'POST':
        if request.form.get('user_id') != app.config['USER_ID']:
            flash('ユーザーIDが異なります', 'error')
        elif request.form.get('password') != app.config['PASSWORD']:
            flash('パスワードが異なります', 'error')
        else:
            session['logged_in'] = True
            flash('ログインしました', 'success')
            return redirect(url_for('mypage'))
    return render_template('top.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました', 'success')
    return render_template('top.html')



