import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"


# ------------------- UI Designer -------------------
window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")

# Card Back
image_card_back = tk.PhotoImage(file="./images/card_back.png")
card_back = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back.create_image(400, 526//2, image=image_card_back)
card_back.grid(row=0, column=0, columnspan=2)

# Card Front
image_card_front = tk.PhotoImage(file="./images/card_front.png")
card_front = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front.create_image(800//2, 526//2, image=image_card_front)
card_front.grid(row=0, column=0, columnspan=2)

# Wrong button
image_wrong = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=image_wrong, highlightthickness=0, border=0)
wrong_button.grid(row=1, column=0)

# Right button
image_right = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=image_right, highlightthickness=0, border=0)
right_button.grid(row=1, column=1)

window.mainloop()
