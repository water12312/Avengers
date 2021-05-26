from flask import render_template, request, url_for, session, redirect, flash

from admin import app

@app.route('/')
def index():
    return render_template('top.html')
