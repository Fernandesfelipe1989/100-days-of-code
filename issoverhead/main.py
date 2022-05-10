import requests

URL_BASE = "http://api.open-notify.org/iss-now.json"

if __name__ == "__main__":
    response = requests.get(url=URL_BASE)
    if response.status_code == 200:
        data = response.json()
        print(data)
