import random
for x in range(10):
	file_name = random.randint(1,10)
	#print(file_name)
	f= open(str(file_name)+".txt","w+")
	f.write("This is line ")
	f.close()