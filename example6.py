n=int(input("enter the no,of elemnts"))
rev=0
while(n>0):
	rem=n%10
	rev=rev*10+rem
	n=n/10
print(rev)

n=int(input("enter the no,of elemnts"))
rev=0
temp=n
while(n>0):
	rem=n%10
	rev=rev*10+rem
	n=n/10
if(temp==rev):
	print("pallindrome")
else:
	print("not")