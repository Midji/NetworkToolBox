from scapy.all import *
import sys

if len(sys.argv) != 2:
	print "Utilisation python ack_tcp_scan.py 192.168.100.9"
	sys.exit(1)
try :
	ACK=IP(dst=sys.argv[1])/TCP(dport=80,flags='A')
	ans, unans = sr(ACK, timeout=1, verbose=0)
	
	if ans[TCP].flags == 'R' :
		print "Port filtre", ans[TCP].dport
	else :
		print "Port non filtre"
		ans.display()

except:
	print "erreur"
	pass
