

for row in range(6):
    print("#",end="")
    #print some spaces
    for spaces in range(row):
        print(" ",end="")
    print("#")

#we nested a loop and the inside loop was dependant on the outer loop 
#doing the same problem in while loops
row = 0 
while row < 6: # range(6):
    print("#",end="")
    #print some spaces
    spaces = 0
    while spaces < row:
        print(" ",end="")
        spaces += 1
    print("#")
    row += 1    
 

