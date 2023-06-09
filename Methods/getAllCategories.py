import requests
from bs4 import BeautifulSoup

def getAllCategories():
    list_categories = []
    base_url = 'https://books.toscrape.com/'
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        categories_url = soup.find('div', class_ = 'side_categories')\
            .find('ul', class_ = 'nav nav-list')\
            .find('li').find('ul')\
            .find_all('li')
        for category_url in categories_url:
            category_url = base_url + category_url.find('a')['href']
            list_categories.append(category_url)
        return list_categories