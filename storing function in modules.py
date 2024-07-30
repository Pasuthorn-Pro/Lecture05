def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error Division by zero"
    return a / b

num1 = 5
num2 = 4
print(f"{num1} - {num2} = {subtract(num1, num2)}")