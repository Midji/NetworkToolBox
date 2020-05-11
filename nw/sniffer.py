from scapy.all import *

class Ecoute (object):

	def __init__(self):
		self.fichier = "capture.pcapng"
		self.interface = "eth0"
		self.filtre = "icmp"

	def sniff(self):
		self.paquet = sniff(iface=self.interface,filter=self.filtre,count=10)
		self.paquet.display()
		
	def parametre(self):
		print ("Interface d'ecoute :" ,self.interface)
		print ("Filtre de capture :", self.filtre)
		return

