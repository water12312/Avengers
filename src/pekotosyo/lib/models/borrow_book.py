from lib.db import db

class Borrowbook(db.Model):

    __tablename__ = 'borrowbook'

    keyid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(8), db.ForeignKey('users.user_id'))
    book_id = db.Column(db.String(8), db.ForeignKey('books.book_id'))
    frag = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, book_id, frag,deadline):
        self.user_id = user_id
        self.bookid = bookid
        self.frag = frag
        self.deadline = deadline