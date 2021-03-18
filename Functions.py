#create a function
def mulila():
    print("Developer and innovator")
#printing whatever the function is required to do, we have to call it
mulila()

#we can still pass parameters to the function
def innovator(name):
    print(name + " is a Developer")
innovator("Kenedy")
innovator("Annah")
innovator("Steve")
#Return keyword- returns information from a function
#using return statement for cubic functions
def cube(num):
    return num*num*num
print(cube(4))
#we can as value to a variable
def cube(namba):
    return namba*namba*namba
result=cube(3)
print(result)
#if statement- it executes given conditions and returns a resposne depending on what is passed
#check using a boolean
is_male= True
if is_male:
    print("you are male")
else:
    print("you are a female")

#another example
is_male= False
if is_male:
    print("you are male")
else:
    print("you are a female")

#we can also pass two conditions in the if statement using either or, and
is_male= True
is_tall= True
if is_male or is_tall:
    print("you are eitehr male or tall")
else:
    print("you are neither tall nor male or both")
#using the and statement
is_male= True
is_tall= False
if is_male and is_tall:
    print("you are male and tall")
else:
    print("one condition or both of them is false")
#we can also use the elif statement to check other condititions with if statement
is_male= True
is_tall= False
if is_male and is_tall:
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("you are a female")
#example 2
is_male= False
is_tall= False
if is_male and is_tall:
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a male and not a female")
#example 3
is_male= False
is_tall= True
if is_male and is_tall:
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("you are a female")

