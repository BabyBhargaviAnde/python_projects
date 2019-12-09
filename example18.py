import requests
url = 'https://entersoftsecurity.com'
x = requests.get(url)
print(x.headers)
response=requests.post('https://httpbin.org/post',json={'key':'value'})
response.requests.headers['Content-Type']