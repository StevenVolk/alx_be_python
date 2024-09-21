n = int(input("Enter a number to see its multiplication table: "))
for number in range(1, 11):
    print(str(n) + " * " + str(number) + " = " + str(number * n))
