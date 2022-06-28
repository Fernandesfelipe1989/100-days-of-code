from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class MovieAddForm(FlaskForm):
    title = StringField(label="Movie's Title")
    submit = SubmitField(label="Search")


class MovieForm(FlaskForm):
    rating = FloatField(label="Rating", validators=[DataRequired(), ])
    review = StringField(label='Review', validators=[DataRequired(), ])
    submit = SubmitField(label="Update")
