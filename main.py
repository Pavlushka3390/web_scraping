import requests
from bs4 import BeautifulSoup

def parse():
    URL = 'https://habr.com'

    KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

    page = 3
    while True:
        response = requests.get('https://habr.com/ru/all/page' + str(page))
        response.raise_for_status()
        page +=3

        soup = BeautifulSoup(response.text, features='html.parser')

        articles = soup.find_all('article', class_='tm-articles-list__item')

        for article in articles:
            time = article.find('span', class_='tm-article-snippet__datetime-published').text
            title = article.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').text
            title_links = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
            title_link = URL + title_links

            text = article.find('div', class_='tm-article-body tm-article-snippet__lead').text
            elm = {elm for elm in text.split(' ')}

            hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
            hub_set = {hub.text.strip() for hub in hubs}


            if KEYWORDS & elm or KEYWORDS & hub_set:
                print(time, '-', title, '-', title_link)

parse()




