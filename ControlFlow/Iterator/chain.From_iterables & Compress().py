import itertools
import operator
lis1=[1,2,3,4,5]
lis2=[1,4,3,8,7]
lis3=[7,4,5,6,8]
lis4=[lis1,lis2,lis3]
print(lis4)
print(list(itertools.chain.from_iterable(lis4)))

print(list(itertools.compress('BiswaRaj Baral',[1,0,0,0,0,1,0,0,0,1,0,0,0,0])))
