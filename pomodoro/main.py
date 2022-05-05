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
resp = 0


def start_timer():
    global resp
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN
    if resp % 2 == 0:
        title_text.config(text="Work", fg=GREEN)
        time = work_sec
    else:
        if resp % 7 == 0:
            title_text.config(text="Break", fg=RED)
            time = long_break_sec
        else:
            title_text.config(text="Break", fg=PINK)
            time = short_break_sec
    countdown(time)
    resp += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    minutes = count // 60
    seconds = count % 60
    seconds = seconds if seconds > 9 else f'0{seconds}'
    minutes = minutes if minutes > 9 else f'0{minutes}'
    if count > 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,)
window.resizable(False, False)


# Create the widgets
title_text = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_text.grid(column=1, row=0)

start_button = tk.Button(text="Start", fg='black', bg=YELLOW, highlightthickness=0, border=2, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", fg='black', bg=YELLOW, highlightthickness=0, border=2)
reset_button.grid(column=2, row=2)

check_mark = tk.Label(text='✓', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark.grid(column=1, row=3)

tomato_image = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
