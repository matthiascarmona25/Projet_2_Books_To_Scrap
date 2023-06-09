from Methods.getAllCategories import getAllCategories
from Methods.getAllPages import getAllPages

all_categories = getAllCategories()
# print(all_categories)

all_pages_by_category = getAllPages('https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html')
print(all_pages_by_category)


