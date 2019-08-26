try:
    file=open('myname.txt','r')
    file.read()
except IOError:
    print("file cannot be located of read")

else:
    print("File read successfully")