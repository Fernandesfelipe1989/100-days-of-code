from decouple import config
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from form import BookForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return self.title


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    book = Book.query.filter_by(id=id).first()
    form = BookForm(title=book.title, author=book.author, rating=book.rating)
    if form.is_submitted():
        book.title = form.data['title']
        book.author = form.data['author']
        book.rating = form.data['rating']
        db.session.commit()
        return redirect(url_for("edit", id=book.id))
    return render_template('book.html', form=form, book=book)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get('name')
        author = request.form.get('author')
        rating = request.form.get('rating')
        if name and author:
            data = dict(
                title=name,
                author=author,
                rating=rating,
            )
            book = Book(**data)
            db.session.add(book)
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.config.update(
        DEBUG=config('DEBUG', cast=bool),
        SECRET_KEY=config('CSRF_SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI="sqlite:///new-books-collection.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    app.run()
