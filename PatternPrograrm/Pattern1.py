n=int(input("enter the number of rows you want to print"))#IT WILL STOTE THE VARIABLE AS STRING SO NEED TO CONVERT INTO INTEGER
for i in range(1,n+1):      #FOR ROWS
    for j in range(1,i+1):  #BECAUSE HERE IF WE TAKE ROW(i=5) THEN COLUMN =6(ie I+1; RANGE IS (1,6))
        print(j,end="")    #END="" MEANS I WANT ANOTHER NUMBER IMMEDIATELY WITHOUT ANY SPACE OF LINE
    print()   #THIS IS FOR NEW LINE

