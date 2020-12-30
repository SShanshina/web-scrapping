import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='post')

for article in articles:
    next_link = article.find('a', class_='post__habracut-btn')
    next_link_url = next_link.attrs.get('href')
    new_response = requests.get(next_link_url)
    new_soup = BeautifulSoup(new_response.text, 'html.parser')
    text = new_soup.find('div', class_='post__text').text.strip().lower()

    if any((key_word in text for key_word in KEYWORDS)):
        article_date = article.find('span', class_='post__time').text.strip()
        link = article.find('a', class_='post__title_link')
        link_url = link.attrs.get('href')
        link_text = link.text.strip()
        print(article_date, link_text, link_url)
