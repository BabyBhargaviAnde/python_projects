import os
#def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
with open("192_223_128_35.html") as f:
	with open("markword.html","w") as f1:
		for line in f.readlines():
			f1.write(line.replace("Version","<mark>Version</mark>"))
			