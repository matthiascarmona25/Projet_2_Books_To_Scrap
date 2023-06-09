import requests
from bs4 import BeautifulSoup

def getAllPages(url_category):
    list_all_pages = []
    list_all_pages.append(url_category)
    base_url = url_category[:-10]
    while True:
        response = requests.get(url_category)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            next = soup.find('li', class_ = 'next')
            if next is not None:
                next_page = next.find('a')['href']
                next_page = base_url + next_page
                list_all_pages.append(next_page)
                url_category = next_page
            else:
                return list_all_pages