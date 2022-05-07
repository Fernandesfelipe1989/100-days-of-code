from random import choice, randint, shuffle
import tkinter as tk
from tkinter import messagebox

import utils


def initialize_entries():
    website_entry.delete(0, tk.END) or email_entry.delete(0, tk.END) or password_entry.delete(0, tk.END)
    email_entry.insert(0, utils.DEFAULT_EMAIl)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [choice(utils.LETTERS) for _ in range(randint(8, 10))]
    symbols = [choice(utils.SYMBOLS) for _ in range(randint(2, 4))]
    numbers = [choice(utils.NUMBERS) for _ in range(randint(2, 4))]

    password_list = letters + symbols + numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website, message=utils.MESSAGE.format(email, password))

        if is_ok:
            info_text = utils.FORMAT_PATTERN.format(website, email, password)
            with open('data.txt', 'a') as file:
                file.write(info_text)
            initialize_entries()
    else:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty")

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg='white')
# window.resizable(False, False)

# Logo Config
logo_image = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels Config
website_text = tk.Label(text='Website:', bg='white', font=utils.FONT)
website_text.grid(row=1, column=0, sticky='e')

email_text = tk.Label(text="Email/Username:", bg='white', font=utils.FONT)
email_text.grid(row=2, column=0, sticky='e')

password_text = tk.Label(text='Password:', bg='white', font=utils.FONT)
password_text.grid(row=3, column=0, sticky='e')

# Entry Config
website_entry = tk.Entry(width=45)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')

email_entry = tk.Entry(width=45)
email_entry.insert(0, utils.DEFAULT_EMAIl)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

# Button Config

password_generate_button = tk.Button(bg='white', text='Generate Password', command=generate_password,)
password_generate_button.grid(row=3, column=2, sticky='e')

add_button = tk.Button(bg='white', text="Add", command=save_password, width=42)
add_button.grid(row=4, column=1, columnspan=2, sticky='e')

window.mainloop()
