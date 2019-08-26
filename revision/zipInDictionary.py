import operator
classmates={'Roshan':'Always Smiles','Abhiyan':'Always boka','Jolly':'always thula kura'}
print(sorted(zip(classmates.keys(),classmates.values())))
print("################################################")

sorted_classmates=sorted(classmates, key=operator.itemgetter(1), reverse=False)
print(sorted_classmates)