import threading
def loop1():
	for i in range(20,30):
		print(i)
def loop2():
	for i in range(0,5):
		print(i)
if __name__=="__main__":
	t1=threading.Thread(loop1())
	t2=threading.Thread(loop2())
	t1.start()
	t2.start()
	t1.join()
	t2.join()
