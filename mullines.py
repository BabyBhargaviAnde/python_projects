keywords = input("Please Enter keywords path as c:/example/ \n :")
keys = open((keywords), "r").readline()
with open("D:/python/sv.txt") as f:
    for line in f:
        if (keys) in line:
            print(line)