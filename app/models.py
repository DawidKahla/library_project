from app import db

authors_books = db.Table(
    "authors_books",
    db.Model.metadata,
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id")),
    db.Column("book_id", db.Integer, db.ForeignKey("books.id")),
)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    year = db.Column(db.Integer, index=True)
    publisher = db.Column(db.String(128), index=True)
    genre = db.Column(db.String(128), index=True)
    done = db.Column(db.Boolean, index=True)
    authors = db.relationship("Author", secondary=authors_books, back_populates="books")
    hires = db.relationship("Hire", backref="book", lazy="dynamic")

    def __str__(self):
        return f'<Book "{self.title}" by {self.authors}>'

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    books = db.relationship("Book", secondary=authors_books, back_populates="authors")

    def __str__(self):
        return f"<Author {self.name}>"


class Hire(db.Model):
    __tablename__ = "hires"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(128), index=True)
    who = db.Column(db.String(128), index=True)
    done = db.Column(db.Boolean, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __str__(self):
        return f"<Hire {self.start}-{self.end}>"
