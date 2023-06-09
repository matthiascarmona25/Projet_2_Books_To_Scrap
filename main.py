from Methods.getAllCategories import getAllCategories
from Methods.getAllPages import getAllPages
from Methods.getAllBooks import getAllBooks

all_categories = getAllCategories()
# print(all_categories)

all_pages_by_category = getAllPages('https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html')
# print(all_pages_by_category)

all_books = getAllBooks('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')
print(all_books)




