#!/usr/bin/env python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
if operation == "+":
    print("The result is " + str(num1 + num2) + ".")
elif operation == "-":
    print("The result is " + str(num1 - num2) + ".")
elif operation == "*":
    print("The result is " + str(num1 * num2) + ".")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print("The result is " + str(num1 /num2) + ".")
