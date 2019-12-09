import requests
#headers={'X-XSS-Protection': '1; mode=block'}
req=requests.get('https://entersoftsecurity.com')
k=req.headers
if (k['X-XSS-Protection']=="1; mode=block"):
	print("X-XSS-Protection is ENABLE")
else:
	print("NO")
if (k['X-Frame-Options']=="SAMEORIGIN"):
	print("X-Frame-Options is ENABLE")
else:
	print("NO")
if (k['X-Content-Type-Options']=="nosniff"):
	print("X-Content-Type-Options is OK")
else:
	print("NO")
#print(type(k['Content-Security-Policy']))
m="upgrade-insecure-requests;"
if "upgrade" in m or (k['Content-Security-Policy']=="upgrade-insecure-requests"):
	print("Content-Security-Policy is OK")
else:
	print("NO")


