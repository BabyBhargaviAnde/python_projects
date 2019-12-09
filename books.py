import xmltodict
import json
with open('books.xml') as in_file:
	xml=in_file.read()
	with open('books.json', 'w') as out_file:
		json.dump(xmltodict.parse(xml), out_file)

#pp = pprint.PrettyPrinter(indent=4)

