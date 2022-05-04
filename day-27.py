import tkinter

window = tkinter.Tk()
window.title("My first Gui program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack(side="left")
window.mainloop()
