import requests
from bs4 import BeautifulSoup
import os

def getAllCategories():
    list_categories = []
    data_repository = os.path.dirname(__file__)
    data_repository = os.path.join(os.path.dirname(data_repository), 'data\\images')
    base_url = 'https://books.toscrape.com/'
    response = requests.get(base_url)

    if not os.path.exists(data_repository):
        os.mkdir(data_repository)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        categories_url = soup.find('div', class_ = 'side_categories')\
            .find('ul', class_ = 'nav nav-list')\
            .find('li').find('ul')\
            .find_all('li')
        for category_url in categories_url:
            category_repository = category_url.find('a').string
            category_repository = category_repository.strip().lower()
            category_repository = os.path.join(data_repository, category_repository)
            isExist = os.path.exists(category_repository)
            if not isExist:
                os.mkdir(category_repository)
            category_url = base_url + category_url.find('a')['href']
            list_categories.append(category_url)
        return list_categories