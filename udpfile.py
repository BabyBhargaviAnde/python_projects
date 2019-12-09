import xmltodict
import json
with open('udp.xml') as in_file:
	xml=in_file.read()
	with open('jsonfile1.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)