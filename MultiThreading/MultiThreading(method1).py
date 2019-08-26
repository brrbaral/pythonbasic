import time
import threading
def calcSquare(numbers):
    print("Calculating Squares:'")
    for n in numbers:
        time.sleep(1)
        print("Squares:",n*n)

def calcCube(numbers):
    print("Calculating Cubes:'")
    for n in numbers:
        time.sleep(1)
        print("Cubes:",n*n*n)

arr=[1,2,3,4,5]
t=time.time()
t1=threading.Thread(target=calcSquare, args=(arr,))
t2=threading.Thread(target=calcCube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Finished in:",time.time()-t,"seconds")
