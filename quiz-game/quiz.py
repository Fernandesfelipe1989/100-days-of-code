from question import QUESTION_BANK


class Quiz:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.user_score = 0

    def play_quiz(self):
        """Checking if we're the end of the quiz"""
        if not self.question_number < len(self.question_list):
            return False
        self.ask_question()
        self._next_question()
        return True

    def _next_question(self):
        self.question_number += 1

    def get_question(self):
        return self.question_list[self.question_number]

    def _check_current_answer(self, answer):
        """Checking if the answer was correct"""
        return self.get_question().correct_answer(answer) and self.add_score()

    def add_score(self):
        self.user_score += 1
        return True

    def show_result(self, user, question):
        """Show the question result and the current user's score """
        print("You got it right!" if self._check_current_answer(user) else "You wrong the answer")
        print("The correct answer was:{}".format(question.answer))
        print(f"Your current score is: {self.user_score}/{self.question_number + 1}")

    def ask_question(self):
        """Asking the questions"""
        question = self.get_question()
        answer = input(f"Q{self.question_number + 1} : {question.text}: (True or False)\n")
        self.show_result(answer, question)


quiz = Quiz(questions=QUESTION_BANK)

if __name__ == "__main__":
    quiz.play_quiz()
    quiz.play_quiz()


