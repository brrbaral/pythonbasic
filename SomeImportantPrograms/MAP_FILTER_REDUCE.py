from functools import reduce
list1=[1,2,3,4,5]

new_list=list(map(lambda x:x*2,list1))
print(new_list)

product=reduce((lambda x,y:x*y),list1)
print(product)
