import tkinter as tk


class QuizInterface:
    THEME_COLOR = "#375362"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler",)
        self.window.config(padx=20, pady=20, bg=self.THEME_COLOR, width=400, height=400)

        # Config Score label
        self.score = tk.Label(text=f'Score : 0', font=('Arial', 12, 'italic'), fg="white", bg=self.THEME_COLOR)
        self.score.grid(row=0, column=1, sticky='e')

        # Config Canvas
        self.canvas = tk.Canvas(width=250, height=300, bg="white")
        self.quiz_text = self.canvas.create_text(100, 100, text='Teste', font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        # Config True Button
        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=self.true_image, border=0, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        # Config False Button
        self.false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=self.false_image, border=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
