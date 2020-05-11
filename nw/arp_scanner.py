import sys
from scapy.all import *

class arp_scanner():
	def __init__(self):
		self.machine={}
	
	def scann(self):
		self.alive,self.dead= srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.100.1/24"), timeout=2, verbose =0)
		for self.i in range(0, len(self.alive)):
			self.machine[self.alive[self.i][1].hwsrc]= self.alive[self.i][1].psrc
		return
	
	def affiche(self):
		print ("Machine UP :")
		print ("Adresse IP -- Adresse MAC\n")
		for self.key, self.value in self.machine.items():
			print (self.value+"\t" +self.key)
		return
scan = arp_scanner()
scan.scann()
scan.affiche()
