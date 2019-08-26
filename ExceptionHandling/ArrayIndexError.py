a=[1,2,3]
b=5
try:
    print("second element is: %d"%(a[1]))
    print("fourth element is :%d"%(a[3]))

except IndexError:
    print("an error occured")