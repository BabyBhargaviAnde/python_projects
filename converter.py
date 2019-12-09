import xmltodict
import json
with open('ioof-tcp_Scan.xml') as in_file:
	xml=in_file.read()
	with open('jsonfile123.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)