from flask import Flask, render_template

from post import Post

app = Flask(__name__)
post = Post()


@app.route('/about')
def about():
    context = dict(city='Sorocaba')
    return render_template("about.html", **context)


@app.route('/contact')
def contact():
    context = dict(city='Sorocaba')
    return render_template("contact.html", **context)


@app.route("/post/<int:id>")
def get_post(id):
    context = dict(city='Sorocaba', post=post.get_post(id=id))
    return render_template('post.html', **context)


@app.route('/')
def home():
    post_data = post.get_posts()
    context = dict(city='Sorocaba', all_post=post_data)
    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
