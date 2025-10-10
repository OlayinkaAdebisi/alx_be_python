def area(length, breadth):
    result = length*breadth
    print(f"The area of the rectangle = {result}")
area(10,10)
area_rec = lambda length,breadth: length*breadth
result = area_rec(5,10)
print(f"The area is {result}")