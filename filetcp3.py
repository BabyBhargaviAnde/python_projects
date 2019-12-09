import json
import io
d="jsonfileconvtcp3.json"
data=json.loads(open(d).read())
for i in data['nmaprun']['host']:
	print("\n*****************\n")
	print "ip address:",i['address']['@addr']
 	if (i['hostnames']):
		print(i['hostnames']['hostname']['@name'])
	else:
		print(i['hostnames'])
 	if 'port' in i['ports']:
		if (type(i['ports']['port']) == list):
			for k in i['ports']['port']:
				print "Portid:",k['@portid'],
		else:
			print "portid:",i['ports']['port']['@portid']
# print "id:",data['nmaprun']['postscript']['script']['@id']
# print "output:",data['nmaprun']['postscript']['script']['@output']
# #print(data['nmaprun']['host'][0]['hostscript'])

	
