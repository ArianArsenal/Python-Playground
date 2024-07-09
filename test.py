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

print("Time's Up")

#----------------------
#Lists

#list is a collection of items in a particular order

#list is mutable

#list can contain different types of data

#list is defined by []

#list can be accessed by index

food = ["pizza","ghorme","doogh"]

# for x in range(len(food)):
#     print(food[x])


food[0] = "kabab"
print(food)

food.append("kale pache")
print(food)

food.sort()
print(food)

food.remove("kale pache")
print(food)

food.pop(1)
print(food)

del food[0]
print(food)

food.clear()
print(food)

food = ["pizza","ghorme","doogh"]

for x in food:
    print(x)

food.insert(1,"kabab")


print(food.count("kabab"))


food2 = food.copy()
print(food2)

food.extend(food2)
print(food)

food.reverse()
print(food)

food.sort(reverse=True)
print(food)


food = ["pizza","ghorme","doogh"]

food.sort(key = str.lower)
print(food)

def myFunc(e):
    return len(e)

food.sort(key = myFunc)
print(food)

food.sort(reverse = True, key = myFunc)
print(food)

# food = ["pizza","ghorme","doogh"]

# food.sort(reverse = True, key = lambda x: len(x))

# print(food)

# food = ["pizza","ghorme","doogh"]




#----------------------
#multi dimensional lists

#list inside a list

drinks = ["coffee","tea","juice"]
foods = ["pizza","fries","hotdog"]
desserts = ["cake","pie","cookie"]

menu = [drinks,foods,desserts]

print(menu)

# for x in menu:
#     for y in x:
#         print(y)

print(menu[1][1])

#---------------------
#tuples


#tuples are immutable

#tuples are defined by ()

#tuples can contain different types of data

#tuples can be accessed by index

#tuples are ordered and faster than lists

tuple = ("salam",8)

print(tuple)

print(tuple[0])

tuple[0] = 1.5 #! not allowed because tuples are immutable (can't change them)

print(tuple[0])

for x in tuple:
    print(x)

print(tuple.count("salam"))
print(tuple.index(8))


#---------------------

#sets

#sets are unordered and unindexed
#sets are defined by {}
#sets can contain different types of data
#sets are mutable
#sets can't have duplicates
#is faster than lists

set = {"fork","spoon","knife"}

print(set)

for x in set:
    print(x)

set.add("arian")
print(set)

set.remove("arian") #if doesnt exist it throws an error
print(set)


set.update(["salam","arian","arian"])
print(set)

print(set.difference({"arian","salam"}))

set.discard("arian") #if doesnt exist it doesnt throw an error
print(set)




#---------------------

#dictionaries

#dictionaries are unordered and mutable
#dictionaries are defined by {}
#dictionaries can contain different types of data
#dictionaries are indexed by keys
#dictionaries can't have duplicates
#key-value (like hashmaps)
#fast because it uses hashing

capitals = {'IRAN':'Tehran',
            'USA':'Washington',
            'UK':'London',
            'Russia':'Moscow'}

print(capitals)

print(capitals['IRAN']) #access by key but if the key doesnt exist it throws an error
print(capitals.get('Germany')) #same as above but if the key doesnt exist it returns None not error

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)

for value in capitals.values():
    print(value)

capitals.update({'Germany':'Berlin'})
print(capitals)


capitals['Germany'] = 'Bonn'
print(capitals)

capitals.pop('Germany') #removes the key and value
print(capitals)


capitals.clear()
print(capitals)


#---------------------
#indexing for strings , lists , tuples

# [start : stop : step]

name = "Arian Mohseni"

if(name[0].islower()):
    print("yes")
else:
    print("no")

first_name = name[:5]
last_name = name[-7:]

print(first_name , last_name)

print(name[-13]== name[0]) #True

print(name[0:]) #whole string
print(name[::-1]) #reverse the string

#---------------------
#functions

def function_name():
    print("Hello World")


function_name()

for x in range(1,11):
    function_name()


def function_name_with_parameter(name):
    print("Hello " + name)

function_name_with_parameter("arian")

#strings , integeres , floats , tuples are immutable so their original value wont be changed when passed to functions
#call by object reference

def function_changes(name):
    name += "changed"
    return name


name = "arian"
print(name)

result = function_changes(name)

print(name)
print(result)

def function_number(age):
    print(type(age))

function_number(21)


def function_default(name = "arian"):
    print(name)


#---------------------

#keyword arguments


def function_keyword(name,age):

    print(f"Name : {name} Age : {age}")


function_keyword(age= 21,name= "arian")

#---------------------

#nested functions

def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    inner_function()

outer_function()

#---------------------

#lambda functions

#small anonymous functions

#can take any number of arguments but only one expression

#used for small functions

#lambda arguments : expression

x = lambda a : a + 10

print(x(5))

x = lambda a,b : a * b

print(x(5,6))

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)

print(myDoubler(11))

#---------------------

#args and kwargs

#*args = parameter that will pack all arguments into a Tuple so that a function can accept a varying amount of positionl arguments



def function_args(*args):
    sum = 0

    for i in args:
        sum += i
    return sum

print(function_args(2,54,78,53,2,5,7))

print(function_args(9.6,7))


#**kwargs = parameter that will pack all arguments into a dictoinary so that a function can accept a varying amount of keyword arguemnts

def example_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
example_kwargs(name="Alice", age=30, city="Wonderland")




#all combined

def example_combined(arg1, *args, **kwargs):
    print("First argument:", arg1)
    
    print("\nNon-keyword arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with a mix of positional and keyword arguments
example_combined(10, 20, 30, name="Alice", age=30, city="Wonderland")


#---------------------
#String format 

var = "ali"
name = "Arian"
age = 20

print("Hello My name is "+ name +"and im"+ age +" years old and"+ var +"is my friend") #beginner (not recommended because of the type casting and spaces between variables)

print("Hello My name is {} and im {} years old and {} is my friend".format("Arian",20,var))#default

print("Hello My name is {1} and im {2} years old and {0} is my friend".format("Arian",20,var)) #positional argument based

print("Hello My name is {name} and im {age} years old and {friend} is my friend".format(name="Arian",age=20,friend=var)) #keyword argument based

print(f"Hello My name is {name} and im {age} years old and {var} is my friend") #f string

text = "Hello My name is {name} and im {age} years old and {friend} is my friend"
print(text.format(name="Arian",age=20,friend=var)) #format string


name = "Arian"

print("Hello, my name is {} nice to meet you".format(name)) #default
print("Hello, my name is {:10} nice to meet you".format(name)) #allocate 10 spaces



#---------------------
