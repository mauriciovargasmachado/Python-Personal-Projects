import bs4
import requests

base_URL = 'https://books.toscrape.com/catalogue/page-{}.html'

#LIST OF BOOKS WITH 4 O MORE STARTS
four_stars_book_rating = []

#ITERATION
for i in range (1,51):

    #CREATE REQUEST IN EACH PAGE
    URL_page = base_URL.format(i)
    result = requests.get(URL_page)
    req = bs4.BeautifulSoup(result.text,'lxml')

    #SELECT BOOKS DATA
    books = req.select('.product_pod')

    # BOOKS ITERATION
    for book in books:
        # CHECK IF THE BOOK HAS 4 O 5 STARS
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            # SAVE TITLE IN NEW VARIABLE
            book_title = book.select('a')[1]['title']

            # ADD THE BOOK TO THE FOUR_STAR_BOOK_RATING VARIABLE
            four_stars_book_rating.append(book_title)

#PRINT EACH ELEMENT
print('')
print(f'From the URL: {base_URL} we found the following books with 4 or more stars: ')
print('************************************************')
print('')
for i, k in enumerate(four_stars_book_rating):
    print(f"{i}. {k}")
print('')
print('************************************************')





