# Temp Calculator

temp = float(input("Enter temperature: "))
unit = input("Enter Unit(C/F):").upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print("Fahrenheit: ",fahrenheit)

elif unit =="F":
    celsius = (temp - 32) * 5/9
    print("Celsius :",celsius)

else:
    print("Invalid unit")



