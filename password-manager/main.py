import tkinter as tk

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, width=500, height=500, border=2, bg='white')
window.resizable(False, False)

# Logo Config
logo_image = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels Config
website_text = tk.Label(text='Website:', bg='white', font=(FONT_NAME, 14, "normal"))
website_text.grid(row=1, column=0)

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_text = tk.Label(text="Email/Username:", bg='white', font=(FONT_NAME, 14, "normal"))
email_text.grid(row=2, column=0)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_text = tk.Label(text='Password:', bg='white', font=(FONT_NAME, 14, "normal"))
password_text.grid(row=3, column=0)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

password_generate_button = tk.Button(bg='white', text='Generate Password', command=generate_password)
password_generate_button.grid(row=3, column=2)

add_button = tk.Button(bg='white', text="Add", command=save_password, width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
