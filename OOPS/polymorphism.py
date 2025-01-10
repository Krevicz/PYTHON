class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old")
        
    def make_sound(self):
        print("Meow")
        
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old")
    
    def make_sound(self):
        print("Bark")

x = Cat("Sally", "15")
x.info()
x.make_sound()
b = Dog("James", 65)
b.info()
b.make_sound()