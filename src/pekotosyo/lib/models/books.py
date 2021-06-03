from lib.db import db

class Book(db.Model):
    __tablename__ = 'books'


    book_id = db.Column(db.String(8),primary_key=True)
    book_name = db.Column(db.String(255),nullable=False)
    book_genre = db.Column(db.String(255),nullable=False)
    borrowbook = db.relationship('Borrowbook',backref='books',uselist=False)


    def __init__(self,book_name,book_genre):
        self.book_name = name
        self.book_genre = genre