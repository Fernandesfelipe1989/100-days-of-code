import tkinter as tk


class QuizInterface:
    THEME_COLOR = "#375362"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler",)
        self.window.config(padx=20, pady=20, bg=self.THEME_COLOR, width=400, height=400)

        # Config Score label
        self.score_label = tk.Label(text=f'Score : 0', fg="white", bg=self.THEME_COLOR)
        self.score_label.grid(row=0, column=1,)

        # Config Canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(
            300//2, 250//2, text='Teste', font=('Arial', 20, 'italic'), fill=self.THEME_COLOR
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Config True Button
        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        # Config False Button
        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
