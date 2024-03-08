import math
import os

#-------------Escape Sequences-------------------------

print("Hello World\n")
print("Hello\tWorld")
print("Hello\bWorld")
print("Hello\rWorld")
print("Hello\fWorld")
print("Hello\'World")
print("Hello\"World")
print("Hello\\World")

#------------variables------------------

age = 24
# int age = 21; in Java 

float_test = 1.2
# float float_test = 1.2; in Java

name = "John"
# String name = "John"; in Java

state = True
# boolean state = True; in Java

#f string usage

print(f"\nHey my name is {name} and im {age} years old\n") # f string

if state == True:
    print("state is true")
    print(f"state is not {not state}")

# not = ! in Java

#---------------multiple assignments------------------

a,b,c = 1,2,3
print(a,b,c)

#--------------else if statements----------------

print(type(age))  # says the type of the variable

if age > 21:

    print("you can drink you're " + str(age) + " years old")   # should be casted to string
    print("you can drink you're",age,"years old")  # automatically adds spaces between variables
    print(f"you can drink you're {age} years old") # f string
    print("you can drink you're {} years old".format(age)) # format string
    print("you can drink you're %d years old" % age) # format string

elif age == 21:
    print("you can drink")
else:
    print("you can't drink")

#print(21 + 23 + "hello")  doesnt work

#---------------user input---------------------
# user input is always string so it should be casted to int or float if needed

name = input("what is your name? ")

print(f"hello {name}")

# it can be both ways , 1- with typing the question in the input() and 2- with print() and input() seperately

print("what is your age? ")
age = input()

print(age)

#-------String methods--------------


#/@ Split method
input = input("Enter Name :")

input.split() #splits the string (a sentence )into a list of strings(list of words) by the given character (default is space)


sentence = "This is a sample sentence"
sentence.split(maxsplit=2) #splits the string by the given character and the maxsplit is the number of splits allowed



#split string by index

string = input("Enter a string : ")
ind = int(input("Enter the index : "))
#split the string by the index

#first part
first_part = string[:ind]
#second part
second_part = string[ind:]

print(f"First part : {first_part}")
print(f"Second part : {second_part}")





lenght = len(input) #lenght of the string

print(lenght)

print(input.upper()) #upper case

print(input.lower()) #lower case

print(input.capitalize()) #capitalize the first letter

print(input.find("E"))  #first occurrence

print(input.rfind("E")) #last occurrence if cant find returns -1

result = input.isdigit() #returns a boolean , if the string only contains numbers True if not False

print(result)

print(input.isalpha()) #if the string has only characters not space or numbers

phone_number = input("Enter Phone Number : ")

print(phone_number.count("-"))  #counts the number of occurrence of the given character 

print(phone_number.replace("-"," ")) #replace the characters you want 

print(help(str)) #more functions 

#----------------------
#String Indexing

# [start : stop : step]



name = "Arian Mohseni"

print(name[0]) #first character

print(name[-1]) #last character

print(name[0:5]) #first 5 characters

print(name[6:]) #from 6th character to the end

print(name[:5]) #from the beginning to the 5th character

print(name[0:10:2]) #from the beginning to the 10th character with a step of 2

print(name[::-1]) #reverse the string


#last 4 characters
last_name = name[-4:]
print(last_name)

#----------------------
#exercise  : email slicer
import os
os.system("cls")

email = input("Please Enter Your Email :")

part = email.split("@")
#the result returns a list of strings

print(f"Username (pre @ ) : {part[0]}")

provider = part[1].split(".")

print(f"Provider (post @ ) : {provider[0]}")

print(f"Domain (post . ) : {provider[1]}")

#print(part[1])

print("-------------------------")
#all parts
print(f"{part} {provider}")

#we could use the index function for finding the @ too




#----------------------
#format specifiers

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

number = 23.45656

print(f"Your Number : {number:.2f}")
print(f"Your Number : {number:10}")
print(f"Your Number : {number:03}")



#--------------------------------
#while loop

name = input("enter name : ")

while name == "":
    print("Enter sth bruh")
    name = input("enter name : ")


print(f"hello {name}")

#---------------------------------
#intrest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter Principle : "))
    if principle <= 0:
        print("Principle Can't be that")
while rate <= 0:
    rate = float(input("Enter Rate : "))
    if rate <= 0:
        print("Rate Can't be that")
while time <= 0:
    time = float(input("Enter Time : "))
    if time <= 0:
        print("Time Can't be that")

interest = principle * pow((1 +  rate  / 100 ),time)

print(f"Your Interest is {interest:.2f}$ after {time} years")





#---------Math--------------------
#library math

number = 25 

number = number ** 2 #power
number = pow(number , 3)

result = max(3,5,6,7)
print(result)
result = min(3,5,6,7)

number = number % 2 #remainder

number = number // 2 #floor division

number = abs(number)

number = math.sqrt(number) #square root 

number = math.ceil(number) #round up a floating point number

number = math.floor(number) #round down a floating point number

number = round(number,2) #round a floating point number to the digit you give

number = math.pi #pi
number = math.e


print(number)

#-----Logical Operands--------


# and #&& in Java

# or #|| in Java

# not #! in Java


#-----Comparison Operands--------


# == #equals to

# != #not equals to

# > #greater than

# < #less than

# >= #greater than or equals to

# <= #less than or equals to


#-----Object Identity Operands--------


# is is for checking if two variables in the memory refers to the same object

# is not is for checking if two variables in the memory refers to the different object




#-----Membership Operands--------


# in checks if the value is in the list

# not in checks if the value is not in the list


#-----Bitwise Operands-------

# & performs a bitwise AND operation. on each bit
# | performs a bitwise OR operation. on each bit
# ^ performs a bitwise XOR (exclusive OR) operation. on each bit
# ~ performs a bitwise NOT operation (inverts the bits). on each bit
# << performs a bitwise left shift (shifts bits to the left).
# >> performs a bitwise right shift (shifts bits to the right).


#------------Colorful Terminal----------------

#ANSI escape codes

#Text Color:

# "\033[30m" - Black
# "\033[31m" - Red
# "\033[32m" - Green
# "\033[33m" - Yellow
# "\033[34m" - Blue
# "\033[35m" - Magenta
# "\033[36m" - Cyan
# "\033[37m" - White

#Background Color:

# "\033[40m" - Black
# "\033[41m" - Red
# "\033[42m" - Green
# "\033[43m" - Yellow
# "\033[44m" - Blue
# "\033[45m" - Magenta
# "\033[46m" - Cyan
# "\033[47m" - White

#Text Style:

# "\033[1m" - Bold
# "\033[2m" - Faint (not widely supported)
# "\033[3m" - Italic (not widely supported)
# "\033[4m" - Underline
# "\033[5m" - Slow Blink (not widely supported)
# "\033[6m" - Rapid Blink (not widely supported)
# "\033[7m" - Reverse Video (swap foreground and background colors)
# "\033[8m" - Conceal (not widely supported)
# "\033[9m" - Crossed Out (not widely supported)
# "\033[22m" - Normal (removes bold, italic, and underline)

#Reset:

# "\033[0m" - Reset all formatting


formatted_text = "\033[1;31;43mBold Red Text on Yellow Background\033[0m"
print(formatted_text)

#-------------------------
#for loops 

for i in range(1,11,3): #range function (start,stop,steps)
    print(i)

#count backward
for counter in reversed(range(1,11)):
    if counter == 4:
        continue
    print(counter)

#iterate through a string
test_string = "This is a Test String"

for x in test_string:
    if x == 'a' :
        break
    print(x)

for y in range(1,11):
    print(y,end="") #in print the end= specify how the print should end 
#--------------------------
import time

print("1")

time.sleep(3) # wait for 3 seconds

print("2")

#----------------------
#&countdown timer

import time,os
user_time = int(input("Enter time in seconds: "))

for x in range(user_time , 0 , -1):
    seconds = x % 60
    minutes = int(x/60) %60
    hours = int(x/3600)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
    os.system("cls")
    