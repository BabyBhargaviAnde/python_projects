import json
d="jsonfileconverterudp.json"
data=json.loads(open(d).read())
for i in data['nmaprun']['host']:
	#print(i['address']['@addr'])
	if 'port' in i['ports']:
		if(type(i['ports']['port'])==list):
			for k in i['ports']['port']:
				print(k['@portid'])

