from bs4 import BeautifulSoup


with open('./website.html', 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.get('href'))

heading = soup.find(name="h1", id='name')
print(heading)
section_heading = soup.find(name='h3', class_="heading")
print(section_heading.getText())
print(section_heading.name)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select('.heading')
print(headings)
