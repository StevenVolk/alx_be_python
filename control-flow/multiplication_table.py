#!/usr/bin/env python3
number = int(input("Enter a number to see its multiplication table: "))
for Y in range(1, 11):
    Z = number * Y
    print(str(number) + " * " + str(Y) + " = " + str(Z))
