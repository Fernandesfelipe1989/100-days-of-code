import requests


class Post:
    BASE_URL = "https://api.npoint.io/790a028aa38e1c2bcd50"

    def __init__(self):
        response = requests.get(url=self.BASE_URL)
        response.raise_for_status()
        self.post = response and response.json()

    def get_posts(self):
        return self.post

    def get_post(self, id):
        index = id - 1
        return self.post[index] if len(self.post) > index >= 0 else {}
