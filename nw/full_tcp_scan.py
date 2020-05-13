from scapy.all import *
import sys

if len(sys.argv) != 2 :
	print ("Utilisation python full_tcp_scan.py 192.168.100.9")
	sys.exit(1)

SYN = IP(dst=sys.argv[1])/TCP(dport=80, flags='S')
print ("Envoie du SYN")
SYN.display()

reponse = sr1(SYN,timeout=1, verbose=0)
print ("Reponse au SYN :")
reponse.display()

if int(reponse[TCP].flags) == 18:
	print ("ACk-SYN recu, fin d etablissement de la connexion")
	ACK = IP(dst=sys.argv[1])/TCP(dport=80,flags=16,ack=(reponse[TCP].seq +1))
	reponse2 = sr1(ACK, timeout = 1, verbose = 0)
	ACK.display()
	reponse2.display()
else :
	print ("SYN ACK non recu")

