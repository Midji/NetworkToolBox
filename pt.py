import getopt, sys
from nw import *

#definition des variables globales


def usage():
	print ("PTP Net Tool\n")
	print ("Usage:  python ptp.py")
	print ("-l --listen \t capture reseau par defaut 10 paquets")
	print ("-c --count \t specifie le nombre de paquets captures")
	print ("-a -ascan <IP> \t fait une recherche d'hote dans la plage IP specifiee, utilise ARP Who Has")

def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:],"hlca",["help","listen","count","ascan"])
	except getopt.GetoptError as err :
		print(str(err))
		usage()
	for o,a in opts :
		if o in ("h","--help"):
			usage()
		elif o in ("l","--list"):
			
		else:
			assert False, "Unhandled Options"
main()
