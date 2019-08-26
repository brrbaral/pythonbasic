import urllib
from urllib import *
import urllib.request

#print(dir(urllib))


req=urllib.request.urlopen('http://python.org')
print(req.readlines())