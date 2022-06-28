from decouple import config
from flask import Flask
from flask_bootstrap import Bootstrap

from models import db

import requests


def create_app():
    app = Flask(__name__)
    app.config.update(
        DEBUG=config('DEBUG', cast=bool),
        SECRET_KEY=config('CSRF_SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=config('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool),
    )
    from views import bp
    app.register_blueprint(bp)
    Bootstrap(app)
    db.init_app(app)
    return app


app = create_app()


if __name__ == '__main__':
    app.run()
