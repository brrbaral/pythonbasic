import asyncio
import time

#COROUTINE 1 TO DISPLAY TIME
async def display_time():
    start_time=time.time()

    while True:
        dur=int(time.time()-start_time)
        if dur % 3==0:
            print("{} seconds have passed".format(dur))
        await asyncio.sleep(1)

#COROUTINE 2 TO PRINT NUMBERS
async def print_num():
    num=1
    while True:
        print(num)
        num+=1
        await asyncio.sleep(0.1)

#CREATE TASK FOR MULTIPLE COROUTINE
async def main():
    task1=asyncio.create_task(display_time())
    task2=asyncio.create_task(print_num())
#USE GATHER TO MENTION THE NAMES OF COROUTINES
    await asyncio.gather(task1,task2)

asyncio.run(main())


