import xmltodict
import json
with open('200_70_22_67.xml') as in_file:
	xml=in_file.read()
	with open('jsonfileconv.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)