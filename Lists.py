#create a list of my favorite people
favorite= ["Big5", "uncle", "family", "business"]
creditNumbers= [2,3,4,5,6,7,8,9]
#to print all the subjects in my list
print(favorite)
#printing one favorite, we use the index values of the lists
print(favorite[0])
#to print a range of values, for instance beyond index 1
print(favorite[1:])
#elements between a set of range
print(favorite[1:3])
#modify values within a
favorite[1]="money"
print(favorite[1])
#to append two lists we use .extend function
favorite.extend(creditNumbers)
print(favorite)
#to a specific item
favorite.extend("love")
print(favorite)
#insert an element within a list, we use the index value
favorite.insert(1, "Mamaa")
print(favorite)
#remove elements
favorite.remove("business")
print(favorite)
#to remove all elements we use
#favorite.clear()
print(favorite)
#to count the number of times a variable is repeated in a list
print(favorite.count("family"))
#sort in ascending order
favorite.sort()
print(favorite)

