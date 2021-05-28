from lib.db import db
from datetime import datetime

class Reserve(db.Model):

    __tablename__ = 'reserve'

    reserve_id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(8),db.ForeignKey('users.user_id'))
    reserve_date = db.Column(db.Date)
    item = db.Column(db.String(255))

def__init__(self,user_id,reserve_date,item):
    self.user_id = user_id
    self.reserve_date = datetime.today()
    self.item = item

