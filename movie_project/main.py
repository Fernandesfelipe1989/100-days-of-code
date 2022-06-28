from decouple import config
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from model import db

import requests


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    db.init_app(app)
    return app


app = create_app()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.config.update(
        DEBUG=config('DEBUG', cast=bool),
        SECRET_KEY=config('CSRF_SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=config('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool),
    )
    app.run()
