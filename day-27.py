import tkinter


def button_clicked():
    message =_input.get()
    label.config(text=message)


window = tkinter.Tk()
window.title("My first Gui program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

button = tkinter.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="New button")
button_2.grid(column=2, row=0)

_input = tkinter.Entry(width=10)
_input.grid(column=3, row=2)


window.mainloop()
