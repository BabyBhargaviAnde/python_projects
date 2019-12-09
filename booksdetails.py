import json
d="books.json"
data=json.loads(open(d).read())
#print(type(data))
for i in data['catalog']['book']:
	if(i['@id']=='bk102' or i['@id']=='bk105'):
		print("id:",i['@id'])
	#author=data['catalog']['book'][0]['author']
		print("Author:",i['author'])
	#title=data['catalog']['book'][0]['title']
		print("Title:",i['title'])
	#genre=data['catalog']['book'][0]['genre']
		print("genre:",i['genre'])
	#price=data['catalog']['book'][0]['price']
		print("Price:",i['price'])
	#publish_date=data['catalog']['book'][0]['publish_date']
		print("Publish_date:",i['publish_date'])
		print("\n")
