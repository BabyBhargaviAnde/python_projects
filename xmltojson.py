import xmltodict
import json
with open('201_216_208_169.xml') as in_file:
	xml=in_file.read()
	with open('jsonfile.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)