class robot:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age
    def display(self):
        return f"Hello, I am a robot. My name is {self.name}, and I am {self.colour}. I am {self.age} years old. "
    
obj1 = robot("James", "Red", 25)
print(obj1.display())