#!/usr/bin/env python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ")
if op == "+":
    operation = num1 + num2
    print("The result is " + str(operation) + ".")
elif op == "-":
    print("The result is " + str(num1 - num2) + ".")
elif op == "*":
    print("The result is " + str(num1 * num2) + ".")
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print("The result is " + str(num1 /num2) + ".")
