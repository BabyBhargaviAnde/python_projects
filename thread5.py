from threading import *
class ex:
	def myfunc(self):
		for x in range(7):
			print("child")
myjob=ex()
thread1=Thread(target=myjob.myfunc)
thread1.start()
thread.join()
print("done")