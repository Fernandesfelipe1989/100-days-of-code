
from flask import Blueprint


from flask import render_template, redirect, url_for, request


from forms import MovieForm
from models import MovieModel, db

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    all_movies = MovieModel.query.all()
    return render_template("index.html", movies=all_movies)


@bp.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = MovieModel.query.filter_by(id=movie_id).first()
    form = MovieForm(rating=movie.rating, review=movie.review)
    if form.is_submitted():
        print("Form submitted")
        movie.rating = form.data.get('rating')
        movie.review = form.data.get('review')
        db.session.commit()
        return redirect(url_for("views.edit", movie_id=movie_id))

    return render_template('edit.html', form=form, movie=movie)
