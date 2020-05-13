from bs4 import BeautifulSoup
import urllib

url = input("Veuillez entrer l'addresse a analyser :\n")
r = urllib.request.urlopen("http://"+url)

soup = BeautifulSoup(r.read(), "lxml")

print ("[*]Recherche de Lien :\n")
for lien in soup.find_all('a'):
    print (lien['href'])
print ("[*]Recherche de PDF :\n")
for liens in soup.find_all('a'):
    current_lien = liens.get('href')
    if current_lien.endswith('pdf'):
        print (current_lien)
