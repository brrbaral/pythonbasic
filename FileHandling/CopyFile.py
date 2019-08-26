file1=open('name.txt','r')
file2=open('abc','w')
for data in file1:
    file2.write(data)