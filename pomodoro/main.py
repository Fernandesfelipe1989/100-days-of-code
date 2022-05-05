import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,)
window.resizable(False, False)

# Create the widgets
timer_text = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_text.grid(column=1, row=0)
start_button = tk.Button(text="Start", fg='black', bg=YELLOW)
start_button.grid(column=0, row=2)
reset_button = tk.Button(text="Reset", fg='black', bg=YELLOW)
reset_button.grid(column=2, row=2)
check_mark = tk.Label(text='✓', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark.grid(column=1, row=3)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
