"""
TODO Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000
print(a // b)  # Floor Division: 3

Comparison Operators
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

Logical Operators
x = True
y = False
print(x and y) # Logical AND: False
print(x or y)  # Logical OR: True
print(not x)   # Logical NOT: False
"""
# Code a Calculator for basic Mathematics Problem with User input

a = input("Enter your First number :")
b = input("Enter your Second number :")
operation = input ("Choose your Operation (+,-,*,/,%) :")
def Calculator(a, b, operation):
    if operation == "+":
        print(int(a) + int(b))
    elif operation == "-":
        print(int(a) - int(b))
    elif operation == "*":
        print(int(a) * int(b))
    elif operation == "/":
        print(int(a) / int(b))
    elif operation == "%":
        print(int(a) % int(b))
    else :
        print(" Invalid Value ")
Calculator(a, b, operation)