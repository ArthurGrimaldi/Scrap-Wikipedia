from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://fr.wikipedia.org/wiki/%C3%89mile_Zola"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

print(soup)

# test boucle trouvée sur internet
# Marche pas
for section in soup.find('div', {'class':'mw-parser-output'}):
    nextNode = section
    i = 0
    while True:
        nextNode = nextNode.name
        try:
            tag_name = nextNode.name
        except AttributeError:
            tag_name = ""
            if tag_name == 'p':
                i += 1
            else:
                print(i)
                break

while True:
    test = soup.find('div', {'class':'infobox'})
    limit = 0
    if test.next_sibling == 'p':
        limit += 1
    else:
        print(limit)
        break

print(soup.find('div', {'class':'infobox'}).find_next_sibling())