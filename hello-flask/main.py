from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def make_bold_wrapper():
        message = func()
        return '<b>' + message + '</b>'
    return make_bold_wrapper


def make_emphasis(func):
    def make_emphasis_wrapper():
        message = func()
        return '<em>' + message + '</em>'
    return make_emphasis_wrapper


def make_underlined(func):
    def make_underlined_wrapper():
        message = func()
        return '<u>' + message + '</u>'
    return make_underlined_wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return f"Hello!"


@app.route("/bye")
def say_bye():
    return "<h1 style='text-align: center;'>Bye</h1>"


if __name__ == "__main__":
    app.run(debug=True)
