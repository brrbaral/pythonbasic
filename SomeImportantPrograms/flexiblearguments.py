def multiply(*args):
    z=1
    for num in args:
        z=z*num
    print("the multiplication is:",z)

multiply(4,5)
multiply(4,5,6)
multiply(4,5,7,8,9,9)