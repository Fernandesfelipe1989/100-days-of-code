from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {name}!<p>"


@app.route("/bye")
def say_bye():
    return "<h1 style='text-align: center;'>Bye</h1>"


if __name__ == "__main__":
    app.run(debug=True)
