import itertools
import operator
lis1=[1,2,3,4,5]
lis2=[1,4,3,8,7]
lis3=[7,4,5,6,8]
#THIS WILL PERFORM ADDITION IN EACH ITERATION
print(list(itertools.accumulate(lis1)))

#THIS WILL PERFORM MULTIPLICATION IN EACH ITERATION
print(list(itertools.accumulate(lis1,operator.mul)))

#USING CHAIN TO PRINT ALL THER ELEMENTS OF THE ABOUVE 3 LISTS
print("All the elements of the three lsits are:")
print(list(itertools.chain(lis1,lis2,lis3)))
