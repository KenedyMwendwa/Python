#using for loop in strings
for letter in "Kiongozi Academy":
    print(letter)
#using for loop in Arrays
courses = ["programming", "scripting", "DBMS", "Networking"]
for course in courses:
    print(course)
#printing all numbers between ""
for index in range(1, 5):
    print(index)

#use for loop for specifying what happens in first iteration
for index in range(5):
    if index==0:
        print("first trial")
    else:
        print("not first trial")