class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_student(self):
        print(f"Student name: {self.name} Student age: {self.age}")
student1 = student(name ="yinka",age = 19)
print(f"{student1.name} is {student1.age}")