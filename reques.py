# import requests
# #headers={'Content-Type':'Application/json'}
# #r = requests.post('https://demo.testfire.net/swagger/properties.json/post')
# r = requests.post("https://demo.testfire.net/api/login",data={"username":"jsmith","password":"demo123"})

# #print(r.json())

# print(r.status_code)
# # print(r.text)
# # k=r.json()
# #print(k['headers']['Content-Type'])
import requests
import json

url = "https://demo.testfire.net/api/login"
#body="{\"toAccount\": \"800002\",\"fromAccount\": \"800003\",\"transferAmount\": \"200\"}"
#body='{"toAccount": "800002","fromAccount": "800003","transferAmount": "200"}'
body='{"name": "J Smith","email": "jsmtih@altoromutual.com","subject": "Amazing web design","message": "I like the new look of your applicaiton"}'
#payload = "{\n    \"toAccount\": \"800002\",\n    \"fromAccount\": \"800003\",\n    \"transferAmount\": \"200\"\n}"
headers = {
   'accept': "application/json",
   'Content-Type': "application/json",
   'User-Agent': "PostmanRuntime/7.18.0",
   'Cache-Control': "no-cache",
   'Host': "demo.testfire.net",
   'Accept-Encoding': "gzip, deflate",
   'Content-Length': "56",
   'Connection': "keep-alive",
   'cache-control': "no-cache"
   }

#response = requests.request("POST", url, data=payload, headers=headers)
#response=requests.post(url,data=payload,headers=headers)
#print(response.text)
#response=requests.post(url,data=body)
#print(json.dumps(response.text))
#print((response.text))
#k=json.dumps(response.text)
#k=json.loads(response.text)
#print(type(k))
#print(k['Authorization'])
#url = "https://demo.testfire.net/api/account/"

#response=requests.get(url,headers={"Authorization":k['Authorization']})
#print(response.text)
# url="https://demo.testfire.net/api/account"
response=requests.get(url,data=body,headers={"Authorization":"YW5OdGFYUm86WkdWdGJ6RXlNelE9OiE/XyJyMDU="})
print(response.text)
#m=json.loads(response.text)
url="https://demo.testfire.net/api/feedback/submit"
response=requests.post(url,data=body)
print(response.text)




