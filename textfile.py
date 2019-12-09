import os
import re
mails=["gmail","yahoo","outlook"]
#for file in os.listdir("/python"):
 #   if file.endswith(".txt"):
     #   print(file)
f=open("./sv.txt","r")
 
k=f.readlines()
for num,i in enumerate(k,1):
	if 'access key' in i:
 		print("line number(AK):",num)
 		print(i)
 	if 'secret' in i:
 		print("line number(secret):",num)
 		print(i)
 	reg = re.findall("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",i)
 	if len(reg)>=1:
		print("line number(password):",num)
		print(i)
		#print(reg)
 	# if 'public' in i:
 	# 	print("line number(public):",num)
 	# 	print(i)
 	#for mail in mails:
 	match = re.findall(r'[\w\.-]+@gmail'+'[\w\.]+com',i)
	if len(match)>=1:
 		print("line number(mail):",num)
		print(i)
f.close()