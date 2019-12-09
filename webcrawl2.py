from BeautifulSoup import BeautifulSoup
import urllib2
import re
html_page = urllib2.urlopen("http://demo.testfire.net/")
#print(html_page)
soup = BeautifulSoup(html_page)
#print(soup)
for link in soup.findAll('a'):
	print(link.get('href'))
