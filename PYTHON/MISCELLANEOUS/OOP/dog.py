from animal import animal
class Dog(animal):
    breed = "Labrador"
    colour = "White"
    weight = 30  # kg
    leg_count = 4

    #constructor
    def __init__(self, name, age, species, breed, colour, weight, leg_count):
        self.breed = breed
        self.colour = colour
        self.weight = weight
        self.leg_count = leg_count
        super().__init__(name, age, species)

    #accessor methods
    def get_breed(self):
        return self.breed
    
    def get_colour(self):
        return self.colour
    
    def get_weight(self):
        return self.weight

    def get_leg_count(self):
        return self.leg_count
    
    #mutator methods
    def set_breed(self, new_breed):
        self.breed = new_breed
    
    def set_colour(self, new_colour):
        self.colour = new_colour
    
    def set_weight(self, new_weight):
        self.weight = new_weight
    
    def set_leg_count(self, new_leg_count):
        self.colour = new_leg_count
    
    #behaviors
    def bark(self):
        return "Woof! Woof!"
    
    def fetch(self):
        return "Run! Run!"
    
    def wag_tail(self):
        return "Happy! Happy!"


    