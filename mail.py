import re
mails=["gmail","yahoo","outlook"]
#hello = "hello"+"world"
#print(hello)
for mail in mails:
	
	line = "good encryption is mailid  bhargavi.ande1@gmail.com of hindering investigations by FBI experts"
    
	match = re.findall(r'[\w\.-]+@'+mail+'[\w\.]+com', line)
	for i in match:
		print(i)
		print(match)

    