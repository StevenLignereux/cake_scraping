from bs4 import BeautifulSoup

# Lecture des données HTML
f = open("recette.html", "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
div_centre = soup.find("div", class_="centre")
paragraphe_description = soup.find("p", class_="description")

texte_titre = titre_h1.text
texte_paragraphe_description = paragraphe_description.text

print("Titre de la page html : ", texte_titre)
print("Paragraphe de description de la page html : ", texte_paragraphe_description)
