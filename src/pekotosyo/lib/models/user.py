from lib.db import db


class Users(db.Model):

    __tablename__ = 'users'
    user_id = db.Column(db.String(8), primary_key =True)
    password = db.Column(db.String(8), nullable=False)
    user_name = db.Column(db.String(8), nullable=False)
    borrowbook = db.relationship('Borrowbook', backref='user', uselist=False)
    card_info = db.relationship('Cardinfo', backref='user', uselist=False)
    reserve = db.relationship('Reserve', backref='user', uselist=False)
    card_history = db.relationship('Cardhistory', backref='user', uselist=False)



    def __init__(self,user_id,password,user_name):
        self.user_id = user_id
        self.password = password
        self.user_name = user_name
