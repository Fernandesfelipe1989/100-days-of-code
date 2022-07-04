from datetime import datetime as dt

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from sqlalchemy.orm import relationship
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash, check_password_hash


from forms import CreatePostForm, ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


@app.route('/', methods=["GET", ])
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:index>", methods=["GET", ])
def show_post(index):
    requested_post = BlogPost.query.filter_by(id=index).first()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost(
            title=form.data.get("title"),
            subtitle=form.data.get("subtitle"),
            date=dt.now().strftime("%B %d, %Y"),
            author=form.data.get("author"),
            body=form.data.get("body"),
            img_url=form.data.get("img_url"),
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:index>", methods=["GET", "POST"])
def edit_post(index):
    try:
        post = BlogPost.query.get_or_404(index)

    except NotFound:
        return render_template("404.html")

    else:
        form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            author=post.author,
            body=post.body,
            img_url=post.img_url,
        )
        if form.validate_on_submit():
            post.title = form.data.get("title")
            post.subtitle = form.data.get("subtitle")
            post.author = form.data.get("author")
            post.body = form.data.get("body")
            post.img_url = form.data.get("img_url")
            db.session.commit()
            return redirect(url_for("get_all_posts"))
        return render_template("make-post.html", form=form)


@app.route("/delete/<int:index>", methods=["GET"])
def delete_post(index):
    try:
        post = BlogPost.query.get_or_404(index)
    except NotFound:
        return render_template("404.html")
    else:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


# TODO Create the contact flow
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
