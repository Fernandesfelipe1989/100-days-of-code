import sqlite3

from flask import Flask, render_template, request, redirect, url_for
db_id = 1
app = Flask(__name__)


def connect_db(command: str):
    db = sqlite3.connect("books-collection.db")
    print(command)
    cursor = db.cursor()
    cursor.execute(
       command
    )
    db.commit()


INSERT = "INSERT INTO books VALUES({}, '{}', '{}', '{}')"
all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global db_id
    if request.method == "POST":
        name = request.form.get('name')
        author = request.form.get('author')
        rating = request.form.get('rating')
        if name and author:
            book = dict(
                id=db_id,
                title=name,
                author=author,
                rating=rating,
            )
            connect_db(INSERT.format(db_id, name, author, rating))
            db_id += 1
            all_books.append(book)
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
