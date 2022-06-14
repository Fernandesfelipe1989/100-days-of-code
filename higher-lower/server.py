from random import randint

from flask import Flask

app = Flask(__name__)

random_number = None


@app.route('/')
def home():
    global random_number
    random_number = randint(0, 9)
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/b3Bg2bfAVD3ws/giphy.gif" alt="Grapefruit ' \
           'slice atop a pile of other slices"> '


@app.route("/<int:num>")
def guess_number(num):
    low_gif = 'https://media.giphy.com/media/xT39DoN744uOb8PiE0/giphy.gif'
    high_gif = 'https://media.giphy.com/media/3FQhyrjNs6c2HLXs4i/giphy.gif'
    right_gif = 'https://media.giphy.com/media/xUA7aZMejLmk0ov2CY/giphy.gif'
    message = '<h1>{} {}</h1> <img src="{}" alt="Grapefruit slice atop a pile of other slices">'
    img = right_gif
    info = 's just right'
    if num < random_number:
        img = low_gif
        info = 'is too low'
    if num > random_number:
        img = high_gif
        info = 'is too high'
    return message.format(num, info, img)


if __name__ == "__main__":
    app.run(debug=True)
