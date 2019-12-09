import json
d="jsonfile123.json"
data=json.loads(open(d).read())
for i in data['nmaprun']['host']:
	print(i['address']['@addr'])
	if (i['hostnames']):
		print(i['hostnames']['hostname']['@name'])
	#if (type(i['hostnames']) == str):
		#for j in  i['hostnames']['hostname']:
		#	print(j['@name'])
	if (type(i['ports']['port']) == list):
		for k in i['ports']['port']:
			print(k['@portid'])
	else:
		print(i['ports']['port']['@portid'])
		#print(i['hostnames']['hostname']['@name'])


	# for k in data['nmaprun']['host'][1]['address']:
# 	print(k)
#data['nmaprun']['host'][1]['hostnames']['hostname']['@name']
#print(i)
#print(data['nmaprun']['host'][1]['ports']['port'])
#	print(data['nmaprun']['host'][0]['ports']['port'][j])
