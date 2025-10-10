class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(name,age):
        print(f"{name} is {age}")
    def __del__(self):
        print("Object deleted")
person("yin","6")