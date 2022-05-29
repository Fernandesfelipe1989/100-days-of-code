from random import choice
import tkinter as tk

import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
ORIGINAL_DATA_FILE_PATH = "./data/french_words.csv"
LEARN_DATA_FILE_PATH = "./words_to_learn.csv"
FONT = 'Ariel'
STUDY_LANGUAGE = "French"
MOTHER_LANGUAGE = "English"

all_data = []
flip_back = None
language_to_learn = ''
language_to_translation = ''
current_word = ""
# ------------------- Generate a Card information -------------------


def check_languages() -> None:
    global all_data
    global language_to_learn
    global language_to_translation
    language_to_learn, language_to_translation = all_data[0].keys()


def selected_word() -> dict:
    global all_data
    word_info = choice(all_data)
    return word_info


# ------------------- Manage the Next Card flow -------------------


def next_card() -> None:
    global flip_back
    global current_word
    current_word = selected_word()
    flip_card(image=card_front, title=language_to_learn, word=current_word[language_to_learn], font_color='black')
    flip_back = window.after(
        3000,
        flip_card,
        card_back,
        language_to_translation,
        current_word[language_to_translation],
        'white'
        )

# ------------------- Flip Card flow -------------------


def flip_card(image: tk.PhotoImage, title: str, word: str, font_color: str) -> None:
    canvas.itemconfig(canvas_image, image=image)
    canvas.itemconfig(title_text, text=title, fill=font_color)
    canvas.itemconfig(word_text, text=word,  fill=font_color)


# ------------------- Manage the Button flow -------------------


def known_word_flow():
    global current_word
    all_data.remove(current_word)
    export_data = pd.DataFrame(all_data)
    export_data.to_csv('words_to_learn.csv', index=False)
    next_card()


def unknown_word_flow():
    next_card()


if __name__ == "__main__":
    try:
        data = pd.read_csv(LEARN_DATA_FILE_PATH)
    except FileNotFoundError:
        original_data = pd.read_csv(ORIGINAL_DATA_FILE_PATH)
        to_learn = original_data
    else:
        to_learn = data
    finally:
        all_data = to_learn.to_dict(orient='records')
        check_languages()

        current_word = selected_word()

        # ------------------- UI Designer -------------------
        window = tk.Tk()
        window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        window.title("Flash Card")

        # Card Canvas
        card_front = tk.PhotoImage(file="./images/card_front.png")
        card_back = tk.PhotoImage(file="./images/card_back.png")
        canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        canvas_image = canvas.create_image(800 // 2, 526 // 2, image=card_front)
        canvas.grid(row=0, column=0, columnspan=2)

        # Card Front Language text
        title_text = canvas.create_text(400, 150, text=language_to_learn, font=(FONT, 40, "italic"))
        word_text = canvas.create_text(400, 263, text=current_word[language_to_learn], font=(FONT, 60, "bold"))

        # Wrong button
        image_wrong = tk.PhotoImage(file="./images/wrong.png")
        unknown_button = tk.Button(image=image_wrong, highlightthickness=0, border=0, command=unknown_word_flow)
        unknown_button.grid(row=1, column=0)

        # Right button
        image_right = tk.PhotoImage(file="./images/right.png")
        know_button = tk.Button(image=image_right, highlightthickness=0, border=0, command=known_word_flow)
        know_button.grid(row=1, column=1)

        flip_back = window.after(
            3000,
            flip_card,
            card_back,
            language_to_translation,
            current_word[language_to_translation],
            'white'
            )
        window.mainloop()
