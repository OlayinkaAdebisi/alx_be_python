"""Exercise 2: Multiple Inheritance Instruction:

Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods"""
class bird:
    def __init__(self):
        pass
    def fly(self):
        print("Birds can fly")
class mammal:
    def __init__(self):
        pass
    def run(self):
        print("Mammals run")
class bat(bird, mammal):
    print("I am a bat")
    def fly(self):
        print("Bats can fly")
    def run(self):
        print("Bats run")
    pass
hi = bat()
hi.fly()
hi.run()
