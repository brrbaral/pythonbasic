from struct import *
packed_data=pack('iif',5,10,15.3)
print(packed_data)

tup=unpack('iif',packed_data)
print(tup)