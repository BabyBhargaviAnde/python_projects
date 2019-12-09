import statistics    
# list of positive integer numbers   
datasets = [5, 2, 7, 4, 2, 6, 8]     
x = statistics.mean(datasets)    
# Printing the mean   
print("Mean is :", x)
def myfun():
	x=300
	def myinnerfunc():
		print(x)
	myinnerfunc()
myfun()
# def myfunc():
# 	global x
# 	x=300
# myfunc()
# print(x)
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)
# import platform
# x = platform.system()
# print(x)
# import platform
# x = dir(platform)
# print(x)