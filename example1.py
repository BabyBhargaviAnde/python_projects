import time
import datetime
#import mysql.connector
import os
print(os.name)
#myconn=mysql.connector.connect(host="localhost",use="root",passwd="google")
#print(myconn)
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(datetime.datetime.now())
os.remove("ll.txt")