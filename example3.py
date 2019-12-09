import json 

database = "example.json"
data = json.loads(open(database).read())

id_number = data[0]["id_number"]
print id_number