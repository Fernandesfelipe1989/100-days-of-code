
class Question:

    def __int__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer

    def __repr__(self):
        return self.text

    def correct_answer(self, answer: bool) -> bool:
        if answer == self.answer:
            return True
        return False
