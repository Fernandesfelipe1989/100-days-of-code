import requests

URL_BASE = "http://api.open-notify.org/iss-now.json"

if __name__ == "__main__":
    response = requests.get(url=URL_BASE)
    response.raise_for_status()
    data = response.json()
    print(data)
