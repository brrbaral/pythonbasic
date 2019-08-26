from struct import *
packetd_data=pack('iif',6,9,14.3)
print(packetd_data)
print("###################")
print(calcsize('i'))
print(calcsize("f"))
print(calcsize("iif"))
original_data=unpack('iif',packetd_data)
print(original_data)

print(unpack('iif',b'\x06\x00\x00\x00\t\x00\x00\x00\xcd\xccdA'))