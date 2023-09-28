
# def myFunction(input,x):
#     print("my function")
#     print(input)

# print("hey")

# list = [1,2,3,4]

# print(list[0])

# print(list[1])

#len(list) comments are #

print("hello\tworld")
print("hello\b3world")


# myFunction("hello", 1)

# for i in range(0,list[3]):
#     print(i)



#-----------------------------------------------
#printing variables



age = 24
# int age = 21; in Java 

float_test = 1.2
# float float_test = 1.2; in Java

name = "John"
# String name = "John"; in Java

print(f"\nhey my name is {name} and im {age} years old\n") # f string

state = True
# boolean state = True; in Java

if state == True:
    print("state is true")
    print(f"state is not {not state}")

# not = ! in Java

#-----------------------------------------------
# multiple assignments

a,b,c = 1,2,3
print(a,b,c)

#-----------------------------------------------


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