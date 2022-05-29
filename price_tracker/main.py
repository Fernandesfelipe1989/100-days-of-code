import requests

from bs4 import BeautifulSoup


AMAZON_BASE_URL = 'https://www.amazon.com.br/Geladeira-Brastemp-Frost-Inverse-litros/dp/B079ZHBWKK/'
HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'Accept-Language': 'en-US;q=0.9',
}

amazon_response = requests.get(url=AMAZON_BASE_URL, headers=HEADERS)
amazon_response.raise_for_status()
try:
    soup = BeautifulSoup(amazon_response.text, 'html.parser')
except Exception as error:
    print(error)
else:
    product_tag = soup.find(name='span', class_="a-offscreen")
    if product_tag:
        product_price = product_tag.getText().split("R$")[1]
        price = float(product_price.replace(".", '').replace(",", "."))
        print(price)
