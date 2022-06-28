from flask import Blueprint

from flask import render_template, redirect, url_for, request

from forms import MovieAddForm, MovieForm
from models import db, MovieModel

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    all_movies = MovieModel.query.all()
    return render_template("index.html", movies=all_movies)


@bp.route("/add/", methods=["GET", "POST"])
def add():
    form = MovieAddForm()
    if form.is_submitted():
        movie = MovieModel(
            title=form.data.get("title"),
            year=form.data.get("year"),
            description=form.data.get("description"),
            rating=form.data.get("rating"),
            ranking=form.data.get("ranking"),
            review=form.data.get("review"),
            img_url=form.data.get("img_url"),
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("views.home"))
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
        print("Form submitted")
        movie.rating = form.data.get('rating')
        movie.review = form.data.get('review')
        db.session.commit()
        return redirect(url_for("views.edit", id=id))

    return render_template('edit.html', form=form, movie=movie)
