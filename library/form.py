from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    author = StringField(label="Author", validators=[DataRequired()])
    rating = FloatField(label="Phone", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
