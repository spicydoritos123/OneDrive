# Using letters as the telephone number is frequently used. 
# So, for instance the words GOT-MILK can be converted to the phone number 468-6455. 
# Write a Python program that asks the user to enter a 
# telephone number as letters and then outputs the corresponding telephone number in digits.
# The program should output the '-' after the third digit.
# The program should accept both upper- and lower-case letters, and spaces.
 

telephone_num = input("Please the phone number phrase:")
while len(telephone_num) != 8:
    print("INVALID TELEPHONE NUMBER")
    telephone_num = input("Please the phone number phrase:")

telephone_num = telephone_num.lower()
# store the phone number 
number_phrase = "" 

for letter in telephone_num:
    print(letter)
    letter = letter.lower()
    if letter >= "a" and letter <= "c":
        number_phrase += "2"
    elif letter >= "d" and letter <= "f":
        number_phrase += "3"
    elif letter >= "g" and letter <= "i":
        number_phrase += "4"
    elif letter >= "j" and letter <= "l":
        number_phrase += "5"
    elif letter >= "m" and letter <= "o":
        number_phrase += "6"    
    elif letter >= "p" and letter <= "s":
        number_phrase += "7"
    elif letter >= "t" and letter <= "v":
        number_phrase += "8"
    elif letter >= "w" and letter <= "z":
        number_phrase += "9"
    elif letter == "-":
        number_phrase += "-"
    else:
        print("some other character that wasnt a dash was entered")
print("The phone number is : ",number_phrase)


















print("end of program")


