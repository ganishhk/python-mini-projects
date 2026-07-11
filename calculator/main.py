def user_data():
    number_one  = int(input("enter your number : "))
    number_two = int(input("enter your number : "))
    return number_one , number_two

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if a == 0 or b == 0:
        return "cannot divided by 0"
    else:
        return a/b


def opration(num):
    a, b = num
    operator = input("What you want to do add, subtract, multiply or divide ").lower()
    if operator == "add" or operator == "+":
        return add(a,b)
    elif operator == "subtract" or operator == "-":
        return subtract(a,b)
    elif operator == "divide" or operator == "/":
        return divide(a,b)
    elif operator == "multiply" or operator == "*":
        return multiply(a,b)
    else:
        return "not an operator"
    
calculator = user_data()

print(opration(calculator))