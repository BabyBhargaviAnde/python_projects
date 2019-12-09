import requests
r=requests.get(" https://entersoftsecurity.com")
#print(r.content)
f=open("soft.html","w+")
print(r.headers)
f.write(r.content)
f.close()
