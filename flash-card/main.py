from random import randint
import tkinter as tk

import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE_PATH = "./data/french_words.csv"
FONT = 'Ariel'
STUDY_LANGUAGE = "French"
MOTHER_LANGUAGE = "English"


def selected_word(data: pd.DataFrame) -> tuple:
    row = randint(0, len(data) - 1)
    word_info = data.iloc[row].to_dict()
    language_1, language_2 = word_info.keys()
    word, word_translation = word_info.values()
    return (language_1, language_2), (word, word_translation)


def update_canvas_text():
    languages, word = selected_word(data)
    canvas.itemconfig(language_text, text=languages[0])
    canvas.itemconfig(word_text, text=word[0])


def known_word_flow():
    update_canvas_text()
    pass


def unknown_word_flow():
    update_canvas_text()
    pass


if __name__ == "__main__":
    try:
        data = pd.read_csv(DATA_FILE_PATH)
    except FileNotFoundError:
        raise FileNotFoundError("The data file was not find.")
    else:
        languages, word = selected_word(data)

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
    language_text = canvas.create_text(400, 150, text=languages[0], font=(FONT, 40, "italic"))
    word_text = canvas.create_text(400, 263, text=word[0], font=(FONT, 60, "bold"))

    # Wrong button
    image_wrong = tk.PhotoImage(file="./images/wrong.png")
    unknown_button = tk.Button(image=image_wrong, highlightthickness=0, border=0, command=unknown_word_flow)
    unknown_button.grid(row=1, column=0)

    # Right button
    image_right = tk.PhotoImage(file="./images/right.png")
    know_button = tk.Button(image=image_right, highlightthickness=0, border=0, command=known_word_flow)
    know_button.grid(row=1, column=1)

    window.mainloop()
