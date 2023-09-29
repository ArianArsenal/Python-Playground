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





#------------Lists----------------



