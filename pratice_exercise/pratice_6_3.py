class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def eat(self):
        print(f"{self.name} eats food")
    def sleep(self):
        print(f"{self.name} sleeps at night")
class dog(Animal):
    def __init__(self, bark):
        self.bark = bark
    def bark(self):
        print("whoof")
dog.eat(Animal("fish","fe"))
dog.bark(Animal)