from bs4 import BeautifulSoup

# lecture des données html
f = open("recette.html","r")
html_content = f.read()
f.close()
soup = BeautifulSoup(html_content,"html.parser")

titre_h1 = soup.find("h1")
texte_titre = titre_h1.text

paragraphe_description = soup.find("p",class_="description")

div_info = soup.find("div",class_="info")
image_info = div_info.find("img")



print("paragraphe de description :",paragraphe_description.text)
print("titre de la page html :",texte_titre)
print("le src de l'image : ",image_info["src"])


print("Hello")

