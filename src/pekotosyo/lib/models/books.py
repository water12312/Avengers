from lib.db import db

class Books(db.Model):
    __tablename__ = 'books'


    book_id = db.Column(db.String(8),primary_key=True)
    book_name = db.Column(db.String(255),nullabele=False)
    book_genre = db.Column(db.String(255),nullabele=False)
    borrowbook = db.relationship('borrowbook',backref='books',uselist=False)


    def __init__(self,book_name,book_genre):
        self.book_name = name
        self.book_genre = genre