from random import randint
import tkinter as tk

import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Ariel'


def selected_word(data: pd.DataFrame) -> tuple:
    row = randint(0, len(data) - 1)
    selected_data = data.iloc[row]
    return selected_data


def known_word_flow():
    pass


def unknown_word_flow():
    pass


if __name__ == "__main__":
    try:
        data = pd.read_csv("./data/french_words.csv")
    except FileNotFoundError:
        raise FileNotFoundError("The data file was not find.")
    else:
        french, english = selected_word(data)

    # ------------------- UI Designer -------------------
    window = tk.Tk()
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("Flash Card")

    # Card Canvas
    card_front = tk.PhotoImage(file="./images/card_front.png")
    card_back = tk.PhotoImage(file="./images/card_back.png")
    canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.create_image(800//2, 526//2, image=card_front)
    canvas.grid(row=0, column=0, columnspan=2)

    # Card Front Language text
    language_text = canvas.create_text(400, 150, text="French", font=(FONT, 40, "italic"))
    word_text = canvas.create_text(400, 263, text=french, font=(FONT, 60, "bold"))

    # Wrong button
    image_wrong = tk.PhotoImage(file="./images/wrong.png")
    unknown_button = tk.Button(image=image_wrong, highlightthickness=0, border=0)
    unknown_button.grid(row=1, column=0)

    # Right button
    image_right = tk.PhotoImage(file="./images/right.png")
    know_button = tk.Button(image=image_right, highlightthickness=0, border=0)
    know_button.grid(row=1, column=1)

    window.mainloop()
