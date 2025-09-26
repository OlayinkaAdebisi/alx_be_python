FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    fahrenheit: float
    return (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    celsius: float
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
temp = float(input("Enter the temperature to convert: "))
scale = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower())
if scale == "c" or scale == "celcius":
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
elif scale == "f" or scale == "fahrenheit":
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")