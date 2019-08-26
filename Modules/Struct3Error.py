from struct import *
try:
    packed_data=pack('iii',1.4,4.1,0.9)

except error as e:
    print(e)
