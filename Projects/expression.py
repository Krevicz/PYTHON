class expression:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def add(self):
        print(self.number1 + self.number2)
        
    def subtract(self):
        print(self.number1 - self.number2)
        
    def multiply(self):
        print(self.number1 * self.number2)
        
    def divide(self):
        print(self.number1/self.number2)
        
x = expression(100, 20)
x.add()
x.subtract()
x.multiply()
x.divide()