import html
import requests

URL_BASE = "https://opentdb.com/api.php"

parameters = {
    'amount': 10,
    'type': 'boolean',
    'category': 18
}
response = requests.get(URL_BASE, params=parameters).json()
data = [data for data in response['results']]
QUESTIONS_DATA = [{'text': html.unescape(information['question']),
                   'answer': information['correct_answer']} for information in data]


if __name__ == "__main__":
    for question in QUESTIONS_DATA[:4]:
        print(question)
