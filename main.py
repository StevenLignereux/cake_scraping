from bs4 import BeautifulSoup

# Lecture des données HTML
f = open("recette.html", "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1").text
paragraphe_description = soup.find("p", class_="description").text
img = soup.find("img", class_="centre info")["src"]


print("Titre de la page html : ", titre_h1)
print("Paragraphe de description de la page html : ", paragraphe_description)
print("Source de l'image de la page html : ", img)
