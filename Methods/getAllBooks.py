import requests
from bs4 import BeautifulSoup

def getAllBooks(url_category_pages):
    base_url = 'https://books.toscrape.com/catalogue/'
    list_all_books = []
    response = requests.get(url_category_pages)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        all_books = soup.find_all('article', class_ = 'product_pod')
        for book in all_books:
            book = book.find('h3').find('a')['href']
            book = base_url + book[9:]
            list_all_books.append(book)
    return list_all_books