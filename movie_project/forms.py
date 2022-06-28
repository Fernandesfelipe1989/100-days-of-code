from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    rating = FloatField(label="Rating", validators=[DataRequired(), ])
    review = StringField(label='Review', validators=[DataRequired(), ])
    submit = SubmitField(label="Update")
