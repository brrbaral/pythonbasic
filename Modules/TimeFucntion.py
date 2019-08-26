import time
print(time.time())
print("--------------------")
print(time.gmtime(86400))
########################3
t1=time.gmtime(864000)
print(time.asctime(t1))

print(time.ctime())