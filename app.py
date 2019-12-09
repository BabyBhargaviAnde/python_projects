import requests
import json
r= requests.get("https://api.builtwith.com/free1/api.json?KEY=dcfd9007-2fcb-4731-89c9-12d7e1040383&LOOKUP=github.com")
k=json.loads(r.text)
print(k)
print(type(k))
