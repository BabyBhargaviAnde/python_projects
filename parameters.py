import json
d="jsonfileconv.json"
data=json.loads(open(d).read())
k=data['nmaprun']['host']['address']['@addr']
print(k)
j=data['nmaprun']['host']['hostnames']['hostname']['@name']
print(j)
for i in data['nmaprun']['host']['ports']['port']:
	print(i['@portid'])
