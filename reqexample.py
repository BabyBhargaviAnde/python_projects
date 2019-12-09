import socket
print socket.gethostbyname(socket.gethostname())
import urllib
response = urllib.urlopen('http://api.hostip.info/get_html.php?   ip=xxx&position=true').read()
print(response)