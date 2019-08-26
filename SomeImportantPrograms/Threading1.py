import time
import threading
def calc_square(numbers):
    for n in numbers:
        print('calculate squares:')
        print('square:',n*n)

def calc_cube(numbers):
    for n in numbers:
        print('calculating cubes:')
        print('cube:',n*n*n)


arr=[1,2,3,4,5]
t=time.time()

t1=threading.Thread(target=calc_square, args=(arr,))
t2=threading.Thread(target=calc_cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
