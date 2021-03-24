#creating 2D lists (Creating Grid structures)
# basically it is creating a list inside another one
new_grid= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#we can now prnt any element inside the lists
# the  square brackets represent row number and column number respecytively
print(new_grid[0][1])
#we can also print the entire row
print(new_grid[0])

#using a for loop to print elements stored in the lists in row form
for row in new_grid:
    print(row)

#again prnt all elements stored in the lists column wise
for row in new_grid:
    for col in row:
        print(col)