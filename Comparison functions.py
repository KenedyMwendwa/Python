#python functions can be used to compare different variables
def maxNum(num1, num2, num3):
    if num1>= num2 and num1>=num3:
        return num1
    elif num2>= num1 and num2>=num3:
        return num2
    else:
        return num3
print(maxNum(300,49,500))
#reached (2:00:43)


