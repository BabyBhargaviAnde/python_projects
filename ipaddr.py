import json
d="jsonfile.json"
data=json.loads(open(d).read())
#print(data)
#ipnumber=data['nmaprun']['host'][0]['ports']['port'][0]['service']['@name']
ipnumber=data['nmaprun']['host'][0]['address']['@addr']
print(ipnumber)

