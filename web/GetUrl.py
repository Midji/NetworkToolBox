import sys, urllib, urllib.parse

class GetURL():
    def __init__(self):
        self.site = input("Indiquer l'url :\n")
        self.requete = input("Parametre de la requete : \n")
        self.donnee = input("Donnee de la requete : \n")

    def createURL(self):
        self.test = self.site+'?'+self.requete+self.donnee
        print (self.test)
        self.url = urllib.parse.urlencode[(self.requete+self.donnee)]
        return (self.test)


test = GetURL()
url = test.createURL()
print ("La requete est : ", url)