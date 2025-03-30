# write a python program using functions to convert Celsius to Fahrenheit

def celsiusToFahrenheit(temp):
    return 5*(temp-32)/9

val = int(input("enter celsius:"))

fah = celsiusToFahrenheit(val)

print(f"Celsius conversion of {val} is {fah}")
