import requests
url = 'https://www.w3schools.com/python/demopage.htm'
x = requests.get(url)
print(x.links)
