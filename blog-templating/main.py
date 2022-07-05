from datetime import datetime as dt
from functools import wraps

from decouple import config
from flask import abort, flash, Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


from forms import CreatePostForm, ContactForm, CommentForm, LoginForm, RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config["DEBUG"] = config("DEBUG")
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy()
db.init_app(app)


## CONFIG LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@app.errorhandler(401)
def unauthorized(e):
    return render_template('errors/401.html'), 401


@app.errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def admin_only(func):
    @wraps(func)
    def wrapper_admin_only(*args, **kwargs):
        if not current_user.id == 1:
            return abort(403)
        return func(*args, **kwargs)
    return wrapper_admin_only


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id', ondelete="CASCADE"))
    parent_post = relationship("BlogPost", back_populates="comments")


##CONFIGURE TABLE
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id',  ondelete="CASCADE"))
    author = relationship("User", back_populates="posts")

    comments = relationship("Comment", back_populates="parent_post")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(250))

    posts = relationship("BlogPost", back_populates="author", cascade="all, delete", passive_deletes=True)
    comments = relationship("Comment", back_populates="comment_author", cascade="all, delete", passive_deletes=True)


@app.route('/', methods=["GET", ])
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.is_submitted():
        name = form.data.get('name')
        email = form.data.get("email")
        password = form.data.get("password")
        if not User.query.filter_by(email=email).first():
            user = User(
                name=name,
                email=email,
                password=generate_password_hash(
                    password=password,
                    method='pbkdf2:sha256',
                    salt_length=8,
                ),
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("get_all_posts"))
        flash("This email was already used")
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.data.get("email")
        password = form.data.get("password")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(pwhash=user.password, password=password):
            login_user(user)
            return redirect(url_for('get_all_posts'))
        flash("The user's email and password doesn't match")
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:index>", methods=["GET", "POST"])
def show_post(index):
    requested_post = BlogPost.query.get_or_404(index)
    form = CommentForm()
    if form.is_submitted():
        if current_user.is_authenticated:
            user = current_user
            comment = Comment(
                comment_author=user,
                parent_post=requested_post,
                text=form.data.get("text")
            )
            db.session.add(comment)
            db.session.commit()
            flash("Success, Your comment was save.")
        flash("You need to login or register to comment a post")
        return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, form=form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost(
            title=form.data.get("title"),
            subtitle=form.data.get("subtitle"),
            date=dt.now().strftime("%B %d, %Y"),
            author=current_user,
            body=form.data.get("body"),
            img_url=form.data.get("img_url"),
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:index>", methods=["GET", "POST"])
@admin_only
def edit_post(index):
    post = BlogPost.query.get_or_404(index)
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
@admin_only
def delete_post(index):
    post = BlogPost.query.get_or_404(index)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


# TODO Create the contact flow
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Successfully, The email was send")
    return render_template("contact.html", form=form)


if __name__ == "__main__":
    db.create_all(app=app)
    app.run()
