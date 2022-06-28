
from flask import Blueprint


from flask import render_template, redirect, url_for, request

from forms import MovieForm
from models import MovieModel

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    all_movies = MovieModel.query.all()
    return render_template("index.html", movies=all_movies)


@bp.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = MovieModel.query.filter_by(id=movie_id).first()
    form = MovieForm()
    if form.is_submitted():
        return redirect(url_for("edit", id=movie_id))

    return render_template('edit.html', form=form, movie=movie)
