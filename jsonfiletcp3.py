import xmltodict
import json
with open('tcp3.xml') as in_file:
	xml=in_file.read()
	with open('jsonfileconvtcp3.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)