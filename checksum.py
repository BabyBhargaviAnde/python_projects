import hashlib
a=hashlib.md5(open('example1.py','rb').read()).hexdigest()
print(a)
b=hashlib.sha256(open("file2.txt",'rb').read()).hexdigest()
print(b)
c=hashlib.sha1(open("file2.txt",'rb').read()).hexdigest()
print(c)
d=hashlib.sha512(open("file2.txt").read()).hexdigest()
print(d)