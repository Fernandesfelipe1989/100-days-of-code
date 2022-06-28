from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class MovieAddForm(FlaskForm):
    title = StringField(label="Movie's Title")
    year = IntegerField(label="Movie's Year")
    description = StringField(label="Description")
    rating = FloatField(label="Rating")
    ranking = IntegerField(label="Movie's ranking")
    review = StringField(label="Review")
    img_url = StringField(label="Movie's image url")
    submit = SubmitField(label="Save")


class MovieForm(FlaskForm):
    rating = FloatField(label="Rating", validators=[DataRequired(), ])
    review = StringField(label='Review', validators=[DataRequired(), ])
    submit = SubmitField(label="Update")
