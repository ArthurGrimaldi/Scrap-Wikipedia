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

# Récupération de l'intro
soup.find('div', {'class':'infobox'}).find_next_siblings('p', limit=4)
# essayer while next_siblings == 'p' i += 1 else return i
# mw-parser-output -> section contenant l'intro



