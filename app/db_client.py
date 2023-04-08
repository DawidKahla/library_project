from app import db
from app.models import Book, Author, Hire
import logging


def add_or_get_author(name):
    author = Author.query.filter_by(name=name).first()
    if author is None:
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
    return author


def get_book_id_by_title(title):
    book = Book.query.filter_by(title=title).first()
    if book:
        return book.id 
    logging.error("Book not in database")

def get_book_title_by_id(id):
    book = Book.query.filter_by(id=id).first()
    if book:
        return book.title 
    logging.error("Book not in database")

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


def add_hire(data):
    book_id = get_book_id_by_title(data["title"])
    if book_id:
        hire = Hire(
            date=data["date"],
            who=data["who"],
            done=data["done"],
            book_id=book_id
        )

        db.session.add(hire)
        db.session.commit()
