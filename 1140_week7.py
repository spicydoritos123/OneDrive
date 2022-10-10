# solution to the quiz

num1 = 1 # int(input("Please enter num 1"))
num2 = 2 # int(input("Please enter num 2"))
num3 = 3 # int(input("Please enter num 3"))
day = input("Please enter a day")


biggest = num1
if num2 > biggest:
    biggest = num2
if num3 > biggest:
    biggest = num3 

smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

if (num1 > 0 and num2 > 0) or (num2 > 0 and num3 > 0) or (num1 > 0 and num3 > 0):
    print("2 positive numbers")
elif (num1 < 0 and num2 < 0) or (num2 < 0 and num3 < 0) or (num1 < 0 and num3 < 0):
    print("2 negatives")
else:
    print("???")

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Day of the week ")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("???")

if day == "Sunday":
    avg = (num1 + num2 + num3) / 3
    print("Avg is:{:.2f}".format(avg))

if biggest >= 10 and day == "Monday":
    print("Smallest: ",smallest," Day : ",day)

if smallest % 2 ==0 and smallest <50 and (day == "Wednesday" or "Thursday"):
    print("Biggest: ",biggest, " Day: ",day)

















































