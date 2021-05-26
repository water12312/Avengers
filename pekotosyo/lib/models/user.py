from lib.db import db


class Users(db.Model):
    user_id = db.Column(db.Integer(8), primary_key =True)
    password = db.Column(db.String(8), nullable=False)
    user_name = db.Column(db.String(8), nullable=False)
    borrow_book = db.relationship('borrowbook', backref='user_id', userlist=False)
    card_info = db.relationship('card_info', backref='user_id', userlist=False)
    reserve = db.relationship('reserve', backref='user_id', userlist=False)
    card_history = db.relationship('card_history', backref='user_id', userlist=False)


    def __init__(self, password,user_name):
        self.passwoed = passwoed
        self.user_name = user_name
