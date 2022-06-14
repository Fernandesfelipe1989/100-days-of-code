from random import randint

from flask import Flask

app = Flask(__name__)

random_number = randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/b3Bg2bfAVD3ws/giphy.gif" alt="Grapefruit ' \
           'slice atop a pile of other slices"> '


@app.route("/<int:num>")
def guess_number(num):
    message = '<h1>{} {}</h1> <img src="{}" alt="Grapefruit slice atop a pile of other slices"> '
    if num < random_number:
        message = f'<h1>{num} is too low</h1>'
    if num > random_number:
        message = f'<h1>{num} is too high</h1>'
    return message


if __name__ == "__main__":
    app.run(debug=True)
