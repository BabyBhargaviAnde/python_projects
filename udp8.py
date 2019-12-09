import xmltodict
import json
with open('udp8.xml') as in_file:
	xml=in_file.read()
	with open('jsonfileconverterudp.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)