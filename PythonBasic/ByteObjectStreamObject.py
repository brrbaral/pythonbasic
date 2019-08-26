#INITIALIZING A STRING
a='geeksforgeeks'

#INITIALIZING A BYTE OBJECT
c=b'geeksforgeeks'

# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mapping
d=a.encode('ASCII')

if(d==c):
    print("Encoding successful")
else:
    print("Encoding unsuccessfull")