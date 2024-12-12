class animal():
    _name = None
    _age = None
    _species = None

    #constructor
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        def get_name(self):
            return self.name

        #accessor methods
        def get_age(self):
            return self.age

        def get_species(self):
            return self.species

        #mutator methods
        def set_name(self, name):
            self.name = name

        def set_age(self, age):
            self.age = age

        def set_species(self, species):
            self.species = species
        
        #behaviors
        def live(self):
            return "I am a living animal!"
        