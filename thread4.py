from threading import *
print(current_thread().getName())
def mt():
	print("Child Thread")
	child=Thread(target=mt)
	child.start()
	print("Executing thread name:",current_thread().getName())