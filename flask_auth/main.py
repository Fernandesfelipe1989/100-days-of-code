from urllib.parse import urlparse, urljoin
from flask import abort, Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", 'https') and ref_url.netloc == test_url.netloc


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get("email")
        password = request.form.get('password')
        user_exists = User.query.filter_by(email=email).first()
        if not user_exists:
            user = User(
                name=name,
                email=email,
                password=generate_password_hash(
                    password=password,
                    method="pbkdf2:sha256",
                    salt_length=8,
                ),
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("home"))
        flash("This email was already used")
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        match_password = check_password_hash(user.password, password=password)
        if match_password:
            login_user(user)
            next = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)
            return redirect(url_for("secrets"))
        flash("User email and password doesn't match")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    user = current_user
    return render_template("secrets.html", user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
