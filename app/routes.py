from app import app
from app.models import Book, Hire
from app.forms import BookForm, HireForm
from app.db_client import add_book, add_hire
from flask import render_template, request, redirect, url_for


@app.route("/books/", methods=["GET", "POST"])
def books():
    books = Book.query.all()
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            add_book(data=form.data)
        return redirect(url_for("books"))
    return render_template("books.html", books=books, form=form)


@app.route("/hires/", methods=["GET", "POST"])
def hires():
    books = Book.query.all()
    hires = Hire.query.all()
    books_list = [book.title for book in books]
    form = HireForm()
    form.title.choices = books_list
    # if request.method == "POST":
    #     if form.validate_on_submit():
    #         add_hire(data=form.data)
    #     return redirect(url_for("hires"))
    return render_template("books.html", books=books, form=form)
