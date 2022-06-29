from flask import Blueprint

from flask import render_template, redirect, url_for, request

from forms import MovieAddForm, MovieForm
from models import db, MovieModel
from utils import MovieAPI

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    all_movies = MovieModel.query.order_by(MovieModel.rating).all()
    for index, movie in enumerate(all_movies):
        movie.ranking = len(all_movies) - index
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@bp.route("/add/<int:id>", methods=["GET"])
def add(id):
    data = MovieAPI().get_movie(id=id)
    movie = MovieModel(**data)
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("views.edit", id=movie.id))


@bp.route("/add/", methods=["GET", "POST"])
def select():
    form = MovieAddForm()
    if form.is_submitted():
        title = form.data.get("title")
        movies = MovieAPI().search_movie(title=title)
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)


@bp.route("delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    movie = MovieModel.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("views.home"))


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = MovieModel.query.filter_by(id=id).first()
    form = MovieForm(rating=movie.rating, review=movie.review)
    if form.is_submitted():
        movie.rating = form.data.get('rating')
        movie.review = form.data.get('review')
        db.session.commit()
        return redirect(url_for("views.edit", id=id))

    return render_template('edit.html', form=form, movie=movie)
