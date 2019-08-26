import threading
import time
def sleeper(n, name):
    print('Hi, I am {}.Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} hs woken up from sleep \n'.format(name))

t=threading.Thread(target=sleeper, name='thread',args=(5,'thread1'))#name=thread is name of thread it may be any like thread1234 etc
t.start()
t.join()
print("done")