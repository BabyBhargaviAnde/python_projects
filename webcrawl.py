import requests
from bs4 import BeautifulSoup
page=requests.get('https://vms.enprobe.io')
print(page.content)
#html_page = urllib2.urlopen("https://vms.enprobe.io")

#soup = BeautifulSoup(page)
#print(soup)
for link in page.findAll('a'):
	print link.get('href')