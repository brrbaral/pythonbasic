def double(n):
    return n*2

list1=[1,2,3,4,5]
list2=list(map(double,list1))
print(list1)
print(list2)

#USING LAMBDA FUCNTION
list3=[6,7,8,9,10]
list4=list(map(lambda x:x*2,list3))
print("###################")
print(list3)
print(list4)

#EXAMPLE 3
list5=[1,3,5,7,9]
list5_new=list(map(lambda x:x**2,list5))
print("###################")
print(list5)
print(list5_new)

#EXAMPLE 4
list6=[1,2,3,4,5,6]
list6_new=list(map(lambda x:x**3,list6))
print("###################")
print(list6)
print(list6_new)