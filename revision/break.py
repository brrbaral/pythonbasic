#STOPS THE LOOP
magicNumber=15
for n in range(1,20):
    if n is magicNumber:
        print(n, "is a magic number")
        break
    else:
        print(n)