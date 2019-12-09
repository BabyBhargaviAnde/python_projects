import requests
url="https://entersoftsecurity.com"
headers = {'user-agent': 'customize header string', 'Content-Type': 'application/json; charset=utf-8'}  
response = requests.get(url, headers=headers)   # modify request headers 
print(response.headers)                         # print response headers 
#print(response.headers['Content-Type'])