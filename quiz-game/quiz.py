from question import QUESTION_BANK


class Quiz:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

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
        return self.get_question().correct_answer(answer)

    def ask_question(self):
        """Asking the questions"""
        answer = input(f"Q{self.question_number + 1} : {self.get_question().text}: (True or False)\n")
        result = self._check_current_answer(answer)


quiz = Quiz(questions=QUESTION_BANK)

if __name__ == "__main__":
    quiz.play_quiz()
    quiz.play_quiz()


