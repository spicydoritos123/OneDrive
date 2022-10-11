

for row in range(6):
    print("#",end="")
    #print some spaces
    for spaces in range(row):
        print(" ",end="")
    print("#")

# we nested a loop and the inside loop was dependant on the outer loop 
# doing the same problem in while loops
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
 

print("this is a test",666666,456,789,123,"hello world", end="12354567",sep="===")
print(44+55)

print("q",4)

