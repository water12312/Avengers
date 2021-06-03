from lib.db import db

import datetime

class Cardhistory(db.Model):

    __tablename__ ='cardhistory'

    cardhistory_id = db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.String(8), db.ForeignKey('users.user_id'))
    history_date = db.Column(db.Date, nullable=False)
    chargemoney = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, history_date, chargemoney):
        self.user_id = user_id
        self.history_date = history_date
        self.chargemoney = chargemoney