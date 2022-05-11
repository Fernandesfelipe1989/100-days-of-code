import tkinter as tk
from tkinter import messagebox
from quiz import Quiz


class QuizInterface:
    THEME_COLOR = "#375362"

    def __init__(self, quiz_brain: Quiz):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler",)
        self.window.config(padx=20, pady=20, bg=self.THEME_COLOR, width=400, height=400)

        # Config Score label
        self.score_label = tk.Label(text=f'Score : 0', fg="white", bg=self.THEME_COLOR)
        self.score_label.grid(row=0, column=1,)

        # Config Canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(
            300//2,
            250//2,
            text='Teste',
            font=('Arial', 20, 'italic'),
            fill=self.THEME_COLOR,
            width=280,
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()
        # Config True Button
        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        # Config False Button
        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz.get_question()
        self.canvas.itemconfig(self.quiz_text, text=question)

    def update_score(self, score: int):
        self.score_label.config(text=f'Score : {score}')

    def give_feedback(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.on_closing()

    def change_color(self, user_answer: bool):
        if user_answer:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.update_score(score=self.quiz.get_score())

    def check_user_answer(self, answer: str):
        is_right = self.quiz.check_current_answer(answer)
        self.change_color(user_answer=is_right)
        self.window.after(1000, self.give_feedback)

    def true_answer(self):
        self.check_user_answer(answer='True')

    def false_answer(self):
        self.check_user_answer(answer='False')

    def on_closing(self):
        messagebox.showinfo(title='Your Score', message=f"Your final score is {self.quiz.final_score():.1f}%")
        self.window.destroy()
