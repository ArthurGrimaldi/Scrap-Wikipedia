from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pdfkit

search = input("Quelle est la recherche du jour?")
search_url = re.sub(" ", "_", search)
url = "https://fr.wikipedia.org/wiki/" + search_url
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('div', {'class':'infobox'})
limit = 0

while True:
    table = table.find_next_sibling()
    try:
        table.find_next_sibling()
    except AttributeError:
        print(limit)
    if table.find_next_sibling().name == 'p':
        limit += 1
    else:
        break

intro = soup.find('div', {'class':'infobox'}).find_next_siblings('p', limit=limit + 1)

for i in intro:
    contenu = i.get_text()

title = '/Users/arthurgrimaldi/Desktop/' + search_url
pdfkit.from_string(contenu, output_path=title)

print(contenu)
