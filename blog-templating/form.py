from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, validators, TextAreaField


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[validators.input_required()])
    email = EmailField(label="Email", validators=[validators.input_required()])
    phone = StringField(label="Phone", validators=[validators.optional()])
    message = TextAreaField(label="Message", validators=[validators.input_required()])
