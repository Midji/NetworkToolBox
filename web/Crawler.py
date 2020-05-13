from bs4 import BeautifulSoup
import urllib

class Crawl():
    def __init__(self):
        self.url=input ("Page a analyser :\n")
        self.r = urllib.request.urlopen("http://"+self.url)
        self.soup = BeautifulSoup(self.r.read(),"lxml")

    def titre(self):
        print ("Titre de la page : \n\t"+self.soup.title.string)
        return

    def link(self):
        print("Enumeration des liens presents sur la page :\n\t")
        self.reference = self.soup.find_all('a')
        print (self.reference)
        for self.lien in self.reference:
            print (self.lien.get('href')+" "+self.lien.string)
            return

site = Crawl()
site.titre()
site.link()