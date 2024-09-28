global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    in_c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if in_c_or_f == "C":
        print(str(temperature) + "°C is " + str(convert_to_fahrenheit(temperature)) + "°F")
    elif in_c_or_f == "F":
        print(str(temperature) + "°F is " + str(convert_to_celsius(temperature)) + "°C")

if __name__ == "__main__":
    main()
