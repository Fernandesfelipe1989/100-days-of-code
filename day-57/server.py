from random import randint

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {
        'num': randint(0, 9)
    }
    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
