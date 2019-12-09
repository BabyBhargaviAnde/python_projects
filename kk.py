import re
mailid=raw_input()
result=re.search("\w[a-zA-Z0-9_.]*@gmail[.]com",mailid)
if(result!=None):
	print("valid")
else:
	print("invalid")