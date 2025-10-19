class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        # self.make_sound()
    def make_sound(self):
        print("Sound made by animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed=breed

    def make_sound(self):
        print("Bark!")
        
d = Dog("Dog", "Doggerman")
d.make_sound()
a = Animal("Dog", "Dog")
a.make_sound()