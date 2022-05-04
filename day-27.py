import tkinter

window = tkinter.Tk()
window.title("My first Gui program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()


def button_clicked():
    message =_input.get()
    label.config(text=message)


button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

_input = tkinter.Entry(width=10)
_input.pack()


window.mainloop()
