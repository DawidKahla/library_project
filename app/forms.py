from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class BookForm(FlaskForm):
    title = StringField("Tytuł", [DataRequired()])
    author = StringField("Autor", [DataRequired()])
    year = IntegerField("Rok", [DataRequired()])
    publisher = StringField("Wydawca", [DataRequired()])
    genre = StringField("Gatunek")
    done = BooleanField("Przeczytane?")
