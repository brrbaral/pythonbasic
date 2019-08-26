import threading
x=0
countt=100000

def adding_2():
    global x
    for i in range(countt):
        x+=2

def adding_3():
    global x
    for i in range(countt):
        x+=3

def subtracting_4():
    global x
    for i in range(countt):
        x-=4

def subtracting_1():
    global x
    for i in range(countt):
        x-=1

t1=threading.Thread(target=adding_2,)
t2=threading.Thread(target=adding_3,)
t3=threading.Thread(target=subtracting_1,)
t4=threading.Thread(target=subtracting_4)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(x)
