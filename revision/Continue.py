#JUMPS THE LOOP
numberTaken=[2,4,6,8,10]
print("there are still the other numbers thata re available")
for n in range(1,20):
    if n in numberTaken:
        continue
    print(n)