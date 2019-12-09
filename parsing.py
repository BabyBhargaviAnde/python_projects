import json
json_data = '[[{"a": 1, "b": 2, "c": 3, "d": 4, "e": {"x":"h","y":12,"z":3}},{"c": 8, "d": 9, "e": 15}]]'
#print(e)
#print(type(json_data))
parsed_json = (json.loads(json_data))
#print(e)
print(parsed_json[0][1]['e'])
#print(json.dumps(parsed_json, indent=4, sort_keys=True))
#loaded_json = json.loads(json_data)
#for x in loaded_json:
#	print("%s: %d" % (x, loaded_json[x]))
