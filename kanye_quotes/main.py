import requests
from tkinter import *

BASE_URL = "https://api.kanye.rest/"


def get_quote():
    response = requests.get(url =BASE_URL)
    try:
        response.raise_for_status()
    except:
        message = "Opsss!!! Something is wrong"
    else:
        message = response.json()['quote']
    canvas.itemconfig(quote_text, text=message)


if __name__ == "__main__":
    window = Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()
