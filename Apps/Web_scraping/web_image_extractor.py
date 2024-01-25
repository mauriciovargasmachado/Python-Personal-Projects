import bs4
import requests

result = requests.get(input('Insert the selected URL: '))

req = bs4.BeautifulSoup(result.text, 'lxml')

images = req.select('img')
for i in images:
    print(i)

