from bs4 import BeautifulSoup
from urllib.request import urlopen

# Transformer espace dans la recherche en _
# research = 'Karl Lagerfeld'
# word = re.sub(" ", "_", research)

# Transfo en PDF
# import pdfkit
# pdfkit.from_string(text_header, output_path='/Users/arthurgrimaldi/Desktop/TITRE')


url = "https://fr.wikipedia.org/wiki/%C3%89mile_Zola"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.body.table.get_text())

# Récupération de l'intro
print(soup.find('div', {'class':'infobox'}).findNext('p').name)

soup.find('div', {'class':'infobox'}).find_next_siblings('p', limit=4)
# essayer while next_siblings == 'p' i += 1 else return i

for section in soup.find('div', {'class':'infobox'}):
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

type(soup.find('div', {'class':'infobox'}))

print(soup.find('div', {'class':'toc_niveau_3'}).a)
