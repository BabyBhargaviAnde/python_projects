import xmltodict
import json
with open('udp6.xml') as in_file:
	xml=in_file.read()
	with open('jsonfileconvudp6.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)