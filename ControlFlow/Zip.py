questions=['name','address','age']
answers=['Bishow','Pokhara',26]

for i,j in zip(questions, answers):
    print("What is your {0}? Its {1}".format(i,j))