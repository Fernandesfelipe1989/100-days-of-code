from data import QUESTIONS_DATA


class Question:

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer

    def __repr__(self):
        return self.text

    def correct_answer(self, answer: str) -> bool:
        return answer == self.answer


QUESTION_BANK = [Question(text=question['text'], answer=question['answer']) for question in QUESTIONS_DATA]

if __name__ == "__main__":
    assert QUESTION_BANK[0].text == QUESTIONS_DATA[0]['text']
    assert QUESTION_BANK[0].answer == QUESTIONS_DATA[0]['answer']
    assert QUESTION_BANK[0].correct_answer(QUESTIONS_DATA[0]['answer'])
    assert not QUESTION_BANK[0].correct_answer('False' if QUESTIONS_DATA[0]['answer'] == 'True' else 'True')
