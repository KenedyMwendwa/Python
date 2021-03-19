#this calculator will be able to get inputs from the user
#Allow users to insert operations depending on their choices
#then the calculator will return the answer
#Allows practical usage of if, elif and else statements
num1=float(input("Enter first number: "))
op=input("Enter operator: ")
num2=float(input("Enter first number: "))
#communicate more about the operations
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
else:
    print("inavlid operator")