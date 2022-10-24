# Create a Python module that implements the 4 functions needed for a simple calculator.
#  The functions required are:

# Add - This function takes 2 numbers and returns the result of the operation




def Add(num1,num2):
    result = num1 + num2
    return result

# Subtract - This function takes 2 numbers and returns the result of the operation
def Subtract(num1,num2):
    result = num1 - num2
    return result


# Multiply - This function takes 2 numbers and returns the result of the operation
def Multiply(num1,num2):
    result = num1 * num2
    return result



# Divide - This function takes 2 numbers and returns the result of the operation
def Divide(num1,num2):
    result = num1 / num2
    return result


# Welcome - This function welcomes the user to the program
def Welcome(num_stars):
    print("*" * num_stars)
    print("***Welcome to my calculator program***")
    print("*"*num_stars)
    print()


# main - This is a glue function that connects the other functions and variables together
def main():

    Welcome(20)

    while True:
        prompt = input("What operation would you like to perform?(A, S, M, D or Q to quit): ")
        if prompt == "Q":
            break
        #Add function
        if prompt =="A":
            num1 = int(input("Please enter number 1"))
            num2 = int(input("Please enter number 2 "))
            result = Add(num1,num2)
            print("The result of the ADD operation is: ",result)
        #subtraction functioon
        elif prompt == "S":
             num1 = int(input("Please enter number 1"))
             num2 = int(input("Please enter number 2 "))
             result = Subtract(num1,num2)
             print("The result of the Subtract operation is: ",result)
        elif prompt == "M":
            num1 = int(input("Please enter number 1"))
            num2 = int(input("Please enter number 2 "))
            result = Multiply(num1,num2)
            print("The result of the MULTIPLY operation is: ",result)
        elif prompt == "D":
            num1 = int(input("Please enter number 1"))
            num2 = int(input("Please enter number 2 "))
            result = Divide(num1,num2)
            print("The result of the DIVIDE operation is: ",result)


#kick off the program 
main()

print("end of program")













