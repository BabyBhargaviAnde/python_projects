import requests
r= requests.post('https://httpbin.org/post', json={'key':'value'})
print(r.request.headers['Content-Type'])
print(r.request.url)
print(r.request.body)