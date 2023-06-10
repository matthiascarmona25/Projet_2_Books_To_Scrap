import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os


def getOneBook(url_book):
    base_url = 'https://books.toscrape.com/'
    data_repository = os.path.dirname(__file__)
    data_repository = os.path.join(os.path.dirname(data_repository), 'data\\images')
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
        product_description = soup.find('div', {'id': 'product_description'})
        if product_description is not None:
            product_description = product_description.find_next_sibling().string
        else:
            product_description = ''

        # Catégorie du livre
        category = soup.find('ul', class_='breadcrumb').find_all('li')
        category = category[len(category)-2].find('a').string

        # Chemin local de l'image téléchargée
        image_path = soup.find('div', {'id': 'product_gallery'}).find('img')['src']
        # Nom du fichier image
        filename_image = image_path.split("/")[-1]

        # URL de l'image
        image_url = base_url + image_path[6:]

        # Chemin complet de l'image
        image_path = os.path.join(data_repository, f"{category.lower()}\\{filename_image}")

        # Nombre d'étoile
        rating_stars = soup.find('div', class_='product_main').find("p", class_='star-rating')['class'][1]

    dict_book = {
        'URL du livre': url_book,
        'UPC': universal_product_code,
        'Titre du livre': title.string,
        'Prix, taxe incluse': price_include_tax,
        'Prix, taxe exclue': price_exclude_tax,
        'Quantité disponible': quantity,
        'Description du produit': product_description,
        'Catégorie': category,
        'Rating': rating_stars,
        "Chemin local de l'image téléchargée": image_path,
        "URL de l'image": image_url
    }
    return dict_book

