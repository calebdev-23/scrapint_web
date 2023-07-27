import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import os.path
import pandas as pd

'''url = 'http://localhost:3000/crud-operation'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')'''

'''f = open('table.html', "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, 'html.parser')
rows = soup.find('table', class_='table').find('tbody').find_all('tr')
listes = []
dictionnaire = {}
for row in rows:
    dic = {"id": row.find_all('td')[0].text, "firsName": row.find_all('td')[1].text,
           "lastName": row.find_all('td')[2].text}
    listes.append(dic)

df = pd.DataFrame(listes)
filename = 'listes.xlsx'

if os.path.exists(filename):
    os.remove(filename)
df.to_excel(filename, index=False) '''

# Version 2
'''url = 'https://www.placedeslibraires.fr/list-53558/liste-de-104-livres-preferes-de-lecteurs-du-monde-des-livres/'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
}
request = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(request) as response:
    html = response.read()

soup = BeautifulSoup(html, 'html.parser')
listes = soup.find('ul', id="liste_livres").find_all('h2', class_="livre_titre")
auteurs = soup.find('ul', id="liste_livres").find_all('h2', class_="livre_auteur")
prix = soup.find('ul', id="liste_livres").find_all('span', class_='item_prix')
dict = {}
for i in range(len(listes)):
    if dict.get("Titre") and dict.get("Auteur") and dict.get("Prix"):
        dict["Titre"].append(listes[i].text.replace("\n", "").replace("  ", ""))
        dict["Auteur"].append(auteurs[i].text.replace("\n", ""))
        dict["Prix"].append(prix[i].text.replace("\n", "").replace("  ", ""))
    else:
        dict["Titre"] = [listes[i].text.replace("\n", "").replace("  ", "")]
        dict["Auteur"] = [auteurs[i].text.replace("\n", "")]
        dict["Prix"] = [prix[i].text.replace("\n", "").replace("  ", "")]
df = pd.DataFrame(dict)
print(df)
if os.path.exists("titre.xlsx"):
    os.remove("titre.xlsx")
df.to_excel("titre.xlsx", index=False) '''

# Version 3
