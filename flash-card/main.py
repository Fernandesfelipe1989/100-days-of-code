import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Ariel'

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
word_text = canvas.create_text(400, 263, text="trouve", font=(FONT, 60, "bold"))

# Wrong button
image_wrong = tk.PhotoImage(file="./images/wrong.png")
unknown_button = tk.Button(image=image_wrong, highlightthickness=0, border=0)
unknown_button.grid(row=1, column=0)

# Right button
image_right = tk.PhotoImage(file="./images/right.png")
know_button = tk.Button(image=image_right, highlightthickness=0, border=0)
know_button.grid(row=1, column=1)

window.mainloop()
