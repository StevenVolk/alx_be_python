#!/usr/bin/env python3
integer = int(input("Enter the size of the pattern: "))
num = integer
while (integer > 0):
    for i in range(0, num):
        if i == num-1:
            print("*")
        else:
            print("*", end="")
    integer -= 1
