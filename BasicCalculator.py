#Basic Calculator
import random
def basic_calculator():
    #choose operation
    #if the use wants sum, operation is 0
    print("For sum press 0.\nFor subtraction press 1\nFor multiplication press 2\nFor division press 3")
    operation = int(input("What kind of operation would you like to do ?"))
    if operation == 0:
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        result=x+y
        print(f"The sum of the 2 numbers is {result}.")
    if operation == 1:
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        result = x-y
        print(f"The subtraction of the 2 numbers is {result}.")
    if operation == 2:
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        result = x*y
        print(f"The multiplication of the 2 numbers is {result}.")
    if operation == 3:
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        if y == 0:
            print("Sorry! Cannot divide by 0!")
        elif y!=0:
            result = x/y
            print(f"The division of the 2 numbers is {result}.")
        
basic_calculator()