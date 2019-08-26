def AND(a,b):
    if a==1 and b==1: #&&
        return True
    else:
        return False
if __name__=="__main__":
    print(AND(1,1))
print("----------------------------------")

print("|AND TRUTH TABLE|     RESUTL|")
print("A=0 , B=0       |A and B=",AND(0,0))
print("A=0 , B=1       |A and B=",AND(0,1))
print("A=1 , B=0       |A and B=",AND(1,0))
print("A=1 , B=1       |A and B=",AND(1,1))
