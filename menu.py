import sys, os
import time
from nw import *

class menu():
	def __init__(self):
		self.menu_actions = {"0":self.main_menu,"1":self.arp,"1.0":self.main_menu,"1.1":self.arp_scan, "8":self.snif, "8.0":self.main_menu, "99":self.bye}
		
	def bye(self):
		print ("[!] Fermeture du programme")
		sys.exit(1)
		
	def	exec_act(self,choix):
		os.system('clear')
		if self.choix == '':
			print("[!] Aucun choix obtenu")
			time.sleep(1)
			self.main_menu()
		else :
			try :
				self.menu_actions[self.choix]()
			except KeyError:
				print("[!] Erreur dans le choix")
				time.sleep(0.5)
				self.main_menu()
		return
		
	def snif(self):
		os.system('clear')
		print ("\n Module d'ecoute reseau")
		test = Ecoute()
		test.parametre()
		self.valide = input ("[?] ok o/N: ")
		if self.valide == "o" :
			os.system('clear')
			test.sniff()
			print ("\n8 Module Sniff")
			print ("0 Menu principal")
			self.choix = input(" >> ")
			self.exec_act('1.'+self.choix)
		else :
			test.parametre()
			time.sleep(0.5)
			self.snif()
		return
	
	def arp (self):
		os.system('clear')
		print ("Menu ARP\n")
		print ("1 ARP Scan")
		print ("2 ARP Spoofing\n")
		print ("0 Menu principal")
		self.choix = input(" >> ")
		self.choix ="1."+self.choix
		self.exec_act(self.choix)
		return
		
	def arp_scan(self):
		os.system('clear')
		print ("Module de Scan ARP\n")
		arpscan = arp_scanner()
		arpscan.scann()
		arpscan.affiche()
		print ("\n1 Menu ARP")
		print ("2 Ecoute reseau")
		print ("0 Menu principal")
		self.choix = input(" >> ")
		self.exec_act('1.'+self.choix)
		return
		
	def main_menu(self):
		os.system('clear')
		print ("Framework reseau\n")
		print ("Choisir l'actions:")
		print ("1. ARP")
		print ("8. Ecoute")
		print ("\n99. Quitter")
		self.choix = input(" >> ")
		self.exec_act(self.choix)
		return

#End class
monmenu = menu()
monmenu.main_menu()
