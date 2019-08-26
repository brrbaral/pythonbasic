fw=open('sample.txt','w')#here 'w'  for write
fw.write('this the first program in file handling in python\n')
fw.write('file handling is often an important mechanism in oop')
fw.close()

#file read
fr=open('sample.txt','r')
text=fr.read()
print(text)