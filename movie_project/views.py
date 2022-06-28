
from flask import Blueprint


from flask import render_template, redirect, url_for, request


bp = Blueprint('views', __name__, url_prefix='/')

@bp.route("/")
def home():
    return render_template("index.html")