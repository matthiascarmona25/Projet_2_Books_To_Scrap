import requests
from bs4 import BeautifulSoup

def getAllCategories():
    response = requests.get('https://books.toscrape.com/')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())