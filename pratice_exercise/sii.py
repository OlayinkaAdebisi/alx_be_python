"""class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

lassie = Dog("Lassie")
lassie.make_sound()  # Output: Woof!"""
class shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        print(f"Area = {self.length * self.breadth}")
hi = shape(5,4)
hi.calculate_area()
class recctangle(shape):
    def area(self):
        print(f"The area is = {self.length * self.breadth}")
hii = recctangle(3,6)
hii.area()
