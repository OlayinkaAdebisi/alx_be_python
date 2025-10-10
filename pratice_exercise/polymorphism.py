"""Exercise 3: Polymorphism with Duck Typing Instruction:

Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically."""

class dog:
    def __init__(self):
        pass
    def make_sound(self):
        print("A dog barks whoof whoof")
class cat:
    def make_sound(self):
        print("A cat  meow meow")
class bird:
    def make_sound(self):
        print("A bird quack")
def let_them_speak(object):
    object.make_sound()
doggy = dog()
catty = cat()
birddy = bird()

let_them_speak(doggy)
let_them_speak(catty)
let_them_speak(birddy)
