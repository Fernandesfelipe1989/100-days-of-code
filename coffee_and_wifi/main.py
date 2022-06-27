from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TimeField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

COFFEE_CHOICES = ['☕' * i if i > 0 else '✘' for i in range(0, 6)]
WIFI_CHOICES = ['💪' * i if i > 0 else '✘' for i in range(0, 6)]
POWER_CHOICES = ['🔌' * i if i > 0 else '✘' for i in range(0, 6)]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open = StringField('Opening Time e.g. 8AM')
    close = StringField('Closing Time e.g. 5:30PM')
    coffee = SelectField('Coffee Rating', choices=COFFEE_CHOICES)
    wifi = SelectField('Wifi Rating', choices=WIFI_CHOICES)
    power = SelectField('Power Rating', choices=POWER_CHOICES)
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [
            form.data['cafe'],
            form.data['location'],
            form.data['open'],
            form.data['close'],
            form.data['coffee'],
            form.data['wifi'],
            form.data['power'],
        ]
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_file.write('\n')
            writer = csv.writer(csv_file)
            writer.writerow(data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
