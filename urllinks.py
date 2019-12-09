import urllib2
import re
from BeautifulSoup import BeautifulSoup
#connect to a URL
website = urllib2.urlopen("http://demo.testfire.net/")
#print(website)
soup = BeautifulSoup(website)
for link in soup.findAll('a'):
	website = urllib2.urlopen("http://demo.testfire.net/"+link.get('href'))
	#soup = BeautifulSoup(website)
	for link in soup.findAll('a'):
		print link.get('href')





