import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://vms.enprobe.io") # Insert your URL to extract
bsObj = BeautifulSoup(html.read());

for link in bsObj.find_all('a'):
    print(link.get('href'))