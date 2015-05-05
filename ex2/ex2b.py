#####################################################################
# FILE : ex2b.py
# WRITER : konstantin + guybrush + 30888377
# EXERCISE : intro2cs ex2 2014-2015
# DESCRIPTION:
# A program that recieves 2 numbers and an operand (+,-,*,/,%)
# and prints the result on the display like a calculator
#####################################################################


#recieves the inputs from the user
num1 = int(input("num1:"))
num2 = int(input("num2:"))
operation = input("operation:")

if operation == '+':
    result = num1 + num2
    
    print(result)
    
elif operation == '-':
    result = num1 - num2
    
    print(result)
    
elif operation == '*':
    result = num1 * num2
    
    print(result)

elif operation == '/':
    if num2 == 0:
        print("Can't divide by 0")
    else:
        result = num1 // num2
    
        print(result)

elif operation == '%':
    if num2 == 0:
        print("Can't divide by 0")
    else:
        result = num1 % num2
    
        print(result)

else:
    print("Unknown operator")
