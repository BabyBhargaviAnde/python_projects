import json
with open('destros.json', 'r') as f:
    destros_dict = json.load(f)
for destro in destros_dict:
    print(destro['Name'])