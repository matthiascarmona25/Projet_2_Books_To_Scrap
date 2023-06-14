from Methods.getAllCategories import getAllCategories
from Methods.getAllPages import getAllPages
from Methods.getAllBooks import getAllBooks
from Methods.getOneBook import getOneBook

import csv
import os
from pprint import pprint

data_repository = os.path.join(os.path.dirname(__file__), 'data')
list_all_books = []
all_categories = getAllCategories()
# print(all_categories)

for category in all_categories:
    all_pages_by_category = getAllPages(url_category=category['categorie_url'])
    # print(all_pages_by_category)
    for one_page_by_category in all_pages_by_category:
        print(one_page_by_category)
        all_books = getAllBooks(url_category_pages=one_page_by_category)
        # print(all_books)
        for book in all_books:
            one_book = getOneBook(url_book=book)
            print(f"    {one_book}")
            list_all_books.append(one_book)

    with open(os.path.join(data_repository, f"{category['categorie_name']}.csv"), "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=list(list_all_books[0].keys()))
        writer.writeheader()
        for list_one_book in list_all_books:
            writer.writerow(list_one_book)
    list_all_books = []
print(list_all_books)





