import xmltodict
import json
with open('udp4.xml') as in_file:
	xml=in_file.read()
	with open('jsonfileconvudp4.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)