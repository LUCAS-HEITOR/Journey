import math

"""Type HintsType 
hints are a way to indicate the expected data
types of function arguments and return values"""
def sum(a: float, b:float) -> float:
    return a + b

def sub(a: float, b:float) -> float:
    return a - b

def div(a: float, b:float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Division By Zero Dont Work")
    
def mul(a: float, b:float) -> float:
    return a * b

def Calculate(num1 , num2, choice):
    if choice == 1:
        return sum(num1, num2)
    elif choice == 2:
        return sub(num1, num2)
    elif choice == 3:
        return div(num1, num2)
    elif choice == 4:
        return mul(num1, num2)    

while True:
    choice2 = int(input("Wanna Calculate? \n1-Yes\n2-No\n"))
    if choice2 == 2:
        break
    if choice2 == 1:
        num1 = int(input("Put First Number\n"))
        num2 = int(input("Put Second Number\n"))
        choice3 = int(input("Select Your Choice! \n 1- Sum, \n 2-Subtraction, \n 3-Division, \n 4-Multiply\n"))
        print(Calculate(num1, num2, choice3))
        break
    
