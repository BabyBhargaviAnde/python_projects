from BeautifulSoup import BeautifulSoup
import urllib2
import re
html_page = urllib2.urlopen("https://vms.enprobe.io")
#print(html_page)
soup = BeautifulSoup(html_page)
#print(soup)
for link in soup.findAll('a'):
	if "http" not in link.get('href'):
		html_page = urllib2.urlopen('https://vms.enprobe.io'+link.get('href'))
		soup = BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			print(link.get('href'))
