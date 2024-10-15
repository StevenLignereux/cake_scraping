from bs4 import BeautifulSoup

# Lecture des données HTML
f = open("recette.html", "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
texte_titre = titre_h1.text

print("Titre de la page html : ", texte_titre)
