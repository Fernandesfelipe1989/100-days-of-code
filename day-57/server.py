from datetime import datetime as dt
import requests

from flask import Flask, render_template


BASE_URL_AGIFY = "https://api.agify.io?"
BASE_URL_GENDERRIZE = "https://api.genderize.io"

app = Flask(__name__)


@app.route("/guess/<name>")
def guess(name):
    context = {}
    parameters = {
        'name': name,
    }
    response_gender = requests.get(url=BASE_URL_GENDERRIZE, params=parameters)
    response_age = requests.get(url=BASE_URL_AGIFY, params=parameters)
    if response_age.status_code == 200 and response_gender.status_code == 200:
        data_gender = response_gender and response_gender.json()
        data_age = response_age and response_age.json()
        context = dict(data_gender, **data_age)
    return render_template('guess.html', **context)


@app.route("/")
def home():
    date = dt.now()
    context = {
        'author': 'Felipe Fernandes',
        'year': date.year,
    }
    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
