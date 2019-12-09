import urllib
ip='192.168.5.188'
response = urllib.urlopen("http://api.hostip.info/get_html.php?ip={}&position=true".format(ip)).read()
print(response)