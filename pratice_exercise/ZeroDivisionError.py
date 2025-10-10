num1=None
num2=None
while num2 != 0:
    try:
        num1 = float(input("Input first number: "))
        num2 = float(input("Input secpnd number: "))
        ans = float(num1/num2)
        
    except ZeroDivisionError:
        print("You cant divide by zero, please input another number")
    else:
        print(f"{num1}/{num2} is {ans}")
        break