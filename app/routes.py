from app import app
from app.models import Book, Author
from app.forms import BookForm
from flask import render_template


@app.route("/books/", methods=["GET", "POST"])
def books():
    books = Book.query.all()
    form = BookForm()
    return render_template("books.html", books=books, form=form)
