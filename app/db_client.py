from app import db
from app.models import Book, Author


def add_or_get_author(name):
    author = Author.query.filter_by(name=name).first()
    if author is None:
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
    return author


def add_book(data):
    book = Book(
        title=data["title"],
        year=data["year"],
        publisher=data["publisher"],
        genre=data["genre"],
        done=data["done"],
    )

    authors = data["author"].split(", ")
    for i in range(len(authors)):
        authors[i] = add_or_get_author(authors[i])

    for author in authors:
        book.authors.append(author)

    db.session.add(book)
    db.session.commit()


def add_hire():
    pass
