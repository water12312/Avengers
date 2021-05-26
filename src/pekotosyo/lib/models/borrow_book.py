from lib.db import db

class Borrowbook(db.Model):

    __tablename__ = 'borrow_book'

    keyid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(8), nullable=False, db.ForeignKey('users.user_id'))
    book_id = db.Column(db.String(8), nullable=False, db.ForeignKey('books.book_id'))
    frag = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, book_id, frag):
        self.userid = userid
        self.bookid = bookid
        self.frag = frag