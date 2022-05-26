import requests

from bs4 import BeautifulSoup


response = requests.get(url="https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all(name="a", class_='titlelink')
scores = soup.find_all(name="span",  class_='score')
articles_texts = []
articles_links = []
articles_score = []
for article in articles:
    articles_texts.append(article.getText())
    articles_links.append(article.get('href'))
articles_score = [int(article.getText().split(" ")[0]) for article in scores]

largest_score = max(articles_score)
largest_index = articles_score.index(largest_score)
print(largest_score)
print(articles_texts[largest_index], articles_links[largest_index])
