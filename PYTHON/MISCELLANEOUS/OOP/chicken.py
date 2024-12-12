from dog import Dog
from animal import animal

class Chicken(animal):
    breed: "Broiler"
    colour: "White"
    leg_count: 2
    weight = 2 #kg

    #constructor
    def __init__(self, breed, colour, leg_count, weight):
        self.breed = breed
        self.colour = colour
        self.leg_count = leg_count
        self.weight = weight
        
    #accessor methods
    def get_breed(self):
        return self.breed
    
    def get_colour(self):
        return self.colour
    
    def get_leg_count(self):
        return self.leg_count
    
    def get_weight(self):
        return self.weight
    
    #mutator methods
    def set_breed(self, new_breed):
        self.breed = new_breed

    def set_colour(self, new_colour):
        self.colour = new_colour
    
    def set_leg_count(self, new_leg_count):
        self.leg_count = new_leg_count
    
    def set_weight(self, new_weight):
        self.weight = new_weight

    #behaviours
    def eggs(self):
        return "Hatch! Hatch!"
    
    def eat(self):
        return "Yummy! Yummy!"
