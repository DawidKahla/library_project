from app import app, db
from app.models import Book, Author
from flask import render_template
from app.routes import books


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Book": Book, "Author": Author}
