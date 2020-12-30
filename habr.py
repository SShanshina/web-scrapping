import requests
from bs4 import BeautifulSoup
from datetime import date

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='post')

for article in articles:
    previews = article.find_all('div', class_='post__text')
    previews_text = list(map(lambda preview: preview.text.strip().lower(), previews))

    for preview_text in previews_text:
        if any((key_word in preview_text for key_word in KEYWORDS)):
            article_date = article.find('span', class_='post__time').text.strip()

            # if 'сегодня' in article_date:
            #     article_date = article_date.replace('сегодня', str(date.today()))

            link = article.find('a', class_='post__title_link')
            link_url = link.attrs.get('href')
            link_text = link.text.strip()
            print(article_date, link_text, link_url)
