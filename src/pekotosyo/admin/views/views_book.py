from flask import render_template, request, url_for, session, redirect, flash, Blueprint

# from lib.models import Book,

from lib.db import db

book = Blueprint('views_book', __name__)

from functools import wraps

def login_check(view):
    @wraps(view)
    def innner(*args, **kwargs):
        if not session.get(''):
            flash('ログインしてください', 'error')
            return redirect(url_for(''))
        return view(*args, **kwargs)
    return innner

@item.route('/')
def index():
    return render_template('top.html')

