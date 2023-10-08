import math

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

input = input("Enter Name :")

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


#-----Identity Operands--------


# is #checks if the two variables are the same

# is not #checks if the two variables are not the same


#-----Membership Operands--------


# in #checks if the value is in the list

# not in #checks if the value is not in the list


#-----Bitwise Operands-------




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


