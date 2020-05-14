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
        print("Enumeration des liens presents sur la page :")
        for self.lien in self.soup.find_all('a'):
            print (self.lien.get('href')+" "+self.lien.string)
            self.linklink("http://"+self.url+self.lien.get('href'))
        return

    def linklink(self,newpage=""):
        if not newpage:
            print ("vide")
            return
        else :
            print("Nouvelle page a analyser: "+newpage)
            self.new = urllib.request.urlopen(newpage)
            self.newsoup = BeautifulSoup(self.new.read(),"lxml")
            for self.newlien in self.newsoup.find_all('a'):
                print(self.newlien.get('href'))
        return

    def form(self):
        print("Enumeration des formulaires :")
        for self.form in self.soup.find_all('form'):
            print (self.form.string)

site = Crawl()
site.titre()
site.link()
#site.form()