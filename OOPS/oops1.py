class place:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp
    def display(self):
        return f"{self.name} recorded {self.temp} °C"
    
p1 = place("Chennai", 40)
print(p1.display())

p2 = place("Sydney", 25)
print(p2.display())

