import requests
res=requests.post('https://httpbin.org/post', data={'key':'value'})
print(res.status_code)
print(res.headers)
