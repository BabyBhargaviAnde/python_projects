import json
d="jsonfile1.json"
data=json.loads(open(d).read())
print(type(data))
for i in data['nmaprun']['host'][1]['ports']['port']:
	print(i['@portid'])
#portid=data['nmaprun']['host'][1]['ports']['port'][2]['@portid']
#print(portid)