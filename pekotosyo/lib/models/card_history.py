from lib.db import db

class Cardhistory(db.model):

    __tablename__ ='card_history'

    cardhistory_id = db.Column(db.Integer,primary_key=True)
    userid =db.Column(db.String(8), nullable=False, db.ForeignKey('users.userid'))
    history_date = db.Column(db.Integer, nullable=False)
    chargemoney = db.Column(db.Integer, nullable=False)

    def __init__(self, userid, history_date, chargemoney):
        self.userid = userid
        self.history_date = history_date
        self.chargemoney = chargemoney