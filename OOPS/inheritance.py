class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lname = lname
    
    def printname(self):
        print(self.firstname, self.lname)
    

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
x = Student("Joey", "King", 2021)
x.printname()
print(x.graduationyear)