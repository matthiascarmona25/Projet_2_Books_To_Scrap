import requests
from bs4 import BeautifulSoup
from pprint import pprint
from os import path


def getOneBook(url_book):
    base_url = 'https://books.toscrape.com/'
    data_repository = r'.\data\img'
    response = requests.get(url_book)
    response.encoding = 'UTF-8'
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Titre du livre
        title = soup.find('div', class_='product_main').find('h1')

        product_info = soup.find('table', class_='table table-striped').find_all('td')

        # Universal Product Code (upc)
        universal_product_code = product_info[0].string

        # Prix, taxe exclue
        price_exclude_tax = product_info[2].string

        # Prix, taxe incluse
        price_include_tax = product_info[3].string

        # Quantité disponible
        quantity =  product_info[5].string
        quantity = quantity[10:-1].split(" ")[0]

        # Description du livre
        product_description = soup.find('div', {'id': 'product_description'}).find_next_sibling().string

        # Catégorie du livre
        category = soup.find('ul', class_='breadcrumb').find_all('li')
        category = category[len(category)-2].find('a').string

        # Chemin local de l'image téléchargée
        image_path = soup.find('div', {'id': 'product_gallery'}).find('img')['src']
        filename_image = image_path.split("/")[-1]

        # URL de l'image
        image_url = base_url + image_path[6:]

        # Nombre d'étoile
        rating_stars = soup.find('div', class_='product_main').find("p", class_='star-rating')['class'][1]

    dict_books = {
        'URL du livre': url_book,
        'UPC': universal_product_code,
        'Titre du livre': title.string,
        'Prix, taxe incluse': price_include_tax,
        'Prix, taxe exclue': price_exclude_tax,
        'Quantité disponible': quantity,
        'Description du produit': product_description,
        'Catégorie': category,
        'Rating': rating_stars,
        "Chemin local de l'image téléchargée": path.join(data_repository, filename_image),
        "URL de l'image": image_url
    }
    pprint(dict_books)
