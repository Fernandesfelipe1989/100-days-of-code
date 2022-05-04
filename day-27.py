import tkinter

RATE_MILES_TO_KM = 1.609


def converter():
    miles = user_input.get()
    calculate_value = miles and float(miles) * RATE_MILES_TO_KM
    label_result.config(text=f'{calculate_value:.1f}' if calculate_value else "Invalid")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)

label = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
label.grid(column=0, row=1)

user_input = tkinter.Entry(width=15)
user_input.grid(column=1, row=0)

label_result = tkinter.Label(text=f"{0}", font=("Arial", 24, "bold"))
label_result.grid(column=1, row=1)

label_km = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
label_km.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=converter)
button.grid(column=1, row=3)

label_miles = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
label_miles.grid(column=2, row=0)


window.mainloop()
