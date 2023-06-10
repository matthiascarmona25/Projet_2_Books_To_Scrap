from Methods.getAllCategories import getAllCategories
from Methods.getAllPages import getAllPages
from Methods.getAllBooks import getAllBooks
from Methods.getOneBook import getOneBook

all_categories = getAllCategories()
# print(all_categories)

for category in all_categories:
    all_pages_by_category = getAllPages(url_category=category)
    # print(all_pages_by_category)
    for one_page_by_category in all_pages_by_category:
        print(one_page_by_category)
        all_books = getAllBooks(url_category_pages=one_page_by_category)
        # print(all_books)
        for book in all_books:
            one_book = getOneBook(url_book=book)
            print(f"    {one_book}")






