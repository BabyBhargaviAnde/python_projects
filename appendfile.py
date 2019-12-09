with open("mm.txt","r") as f:
	print(type(f))
	with open("ll.txt","a") as f1:
		for line in f:
			f1.write(line)
			
