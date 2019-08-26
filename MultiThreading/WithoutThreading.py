import time
def calcSquare(numbers):
    print("Calculating Squares")
    for n in numbers:
        time.sleep(0.2)
        print("Square", n*n)

def calcCube(numbers):
    print("Calculating Cubes")
    for n in numbers:
        time.sleep(0.2)
        print("cubes:", n*n*n)

t=time.time()
arr=[1,2,3,4,5]
calcSquare(arr)
calcCube(arr)
print("done in:", time.time()-t,"secs")
print(time.time())
