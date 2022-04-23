from data import QUESTIONS_DATA


class Question:

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = bool(answer)

    def __repr__(self):
        return self.text

    def correct_answer(self, answer: str) -> bool:
        if bool(answer) == self.answer:
            return True
        return False


QUESTION_BANK = [Question(text=question['text'], answer=question['answer']) for question in QUESTIONS_DATA]

if __name__ == "__main__":
    print(QUESTION_BANK)
