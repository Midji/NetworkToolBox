import dns.resolver


 #voir pour tester le transfert de zone
reponse = dns.resolver.query("kondah.com", "MX")
for data in reponse :
	print "Serveur MX :", data.exchange, " avec une priorite de: ", data.preference
