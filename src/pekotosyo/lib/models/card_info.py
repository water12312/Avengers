from lib.db import db
from datetime import datetime
class Cardinfo(db.Model):


    __tablename__ = 'cardinfo'

    cardinfo_id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(8),db.ForeignKey('users.user_id'))
    card_number = db.Column(db.String(16))
    card_key = db.Column(db.String(3))
    card_date = db.Column(db.Date)
    card_name = db.Column(db.String(10))
    user_money = db.Column(db.Integer,nullable=False)


    def __init__(self,user_id,card_number,card_key,card_date,card_name,user_money):
        self.user_id = user_id
        self.card_number = card_number
        self.card_key = card_key
        self.card_date = card_date
        self.card_name = card_name
        self.user_money = user_money

