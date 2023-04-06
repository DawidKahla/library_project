from wtforms import StringField, BooleanField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class BookForm(FlaskForm):
    title = StringField("Tytuł", [DataRequired()])
    author = StringField("Autor", [DataRequired()])
    year = IntegerField("Rok", [DataRequired()])
    publisher = StringField("Wydawca", [DataRequired()])
    genre = StringField("Gatunek")
    done = BooleanField("Przeczytane?")


class HireForm(FlaskForm):
    title = SelectField("Tytuł", [DataRequired()])
    date = DateField(
        "Data wypożyczenia", format="%d-%m-%Y", validators=[DataRequired()]
    )
    who = StringField("Wypożyczający")
    done = BooleanField("Czy zwrócono?")
