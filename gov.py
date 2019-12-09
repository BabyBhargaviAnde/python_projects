import json
import io
d="gov.json"
data=json.loads(open(d).read())
for i in data['meta']['view']['columns']:
  print(i['id'])
  print(i['name'])
  if(i['id']>-1):
    if(i['cachedContents']):
      if(i['top']):
        for j in i['cachedContents']['top']:
          print(j['item'])
          print(j['count'])