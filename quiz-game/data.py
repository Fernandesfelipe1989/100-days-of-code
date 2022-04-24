from re import sub
import requests

PATTERN = r'[^a-zA-Z_ ]'
URL_BASE = "https://opentdb.com/api.php?amount=25&type=boolean"


def text_filter(text):
    return sub(PATTERN, "", text, count=100)


response = requests.get(URL_BASE).json()
data = [data for data in response['results']]
QUESTIONS_DATA = [{'text': text_filter(information['question']),
                   'answer': information['correct_answer']} for information in data]


if __name__ == "__main__":
    print(QUESTIONS_DATA[0])
