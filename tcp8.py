import json
d="jsonfileconverter.json"
data=json.loads(open(d).read())
#print(type(data))

for i in data['nmaprun']['host']:
	print(i['address']['@addr'])
	if (i['hostnames']):
		print(i['hostnames']['hostname']['@name'])
	if 'port' in i['ports']:
		if (type(i['ports']['port']) == list):
			for k in i['ports']['port']:
				print(k['@portid'])
		else:
			print(i['ports']['port']['@portid'])
print(data['nmaprun']['postscript']['script']['@id'])
print(data['nmaprun']['postscript']['script']['@output'])                          