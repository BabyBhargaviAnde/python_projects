with open("mm.txt") as f:
	print(type(f))
	with open("bhar.txt","w") as f1:
		for line in f:
			#print(line)
			f1.write(line)