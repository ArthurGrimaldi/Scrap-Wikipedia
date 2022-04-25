from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://fr.wikipedia.org/wiki/Steve_Jobs"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

print(soup)

table = soup.find('div', {'class':'infobox'})
limit = 0

# C'est bon ça marche grosse folle
while True:
    table = table.find_next_sibling()
    try:
        table.find_next_sibling()
    except AttributeError:
        print(limit)
    if table.find_next_sibling().name == 'p':
        limit += 1
    else:
        print(limit)
        break
