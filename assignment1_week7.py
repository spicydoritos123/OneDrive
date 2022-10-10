# The distance a vehicle travels can be calculated as follows:

# distance = speed × time
# For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles.

# Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. 

# As an example, for the following input:

# What is the speed of the vehicle in mph? 40
# How many hours has it traveled? 3 

# Here is an example of the desired output:

# Hour: 1, distance traveled:  40

# Hour: 2, distance traveled:  80

# Hour: 3, distance traveled:  120

# This table may be helpful.

# Hour	Distance Traveled
# 1	40
# 2	80
# 3	120

# from time import time
# from turtle import distance


speed = 40#int(input("Please enter the speed of the vehicle: "))
drive_time = 3#int(input("Please enter the number of hours driven: "))

distance = speed * drive_time

# for hour in range(drive_time):
#     distance = speed* hour
#     print(hour)

# for hour in range(1, drive_time +1):
#     distance = speed * hour
#     print("Hour: ",hour,"distasnce traveled: ",distance)

#while loop
hour = 1
while hour <= drive_time: 
    print(hour)
    hour += 1
    distance = speed * hour
    print("Hour: ",hour, "distance traveled: ", distance)















print("end of program")




print()

















































