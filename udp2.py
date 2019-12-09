import json
import io
d="jsonfileudp2.json"
data=json.loads(open(d).read())
for i in data['nmaprun']['host']:
	print("\n*****************\n")
	print "ip address:",i['address']['@addr']
	print "Hostname:",i['hostnames']['hostname']['@name']
	if 'port' in i['ports']:
		if (type(i['ports']['port']) == list):
			for k in i['ports']['port']:
				print "Portid:",k['@portid'],
		else:
			print "portid:",i['ports']['port']['@portid']
print "id:",data['nmaprun']['postscript']['script']['@id']
print "output:",data['nmaprun']['postscript']['script']['@output']
#print(data['nmaprun']['host'][0]['hostscript'])
