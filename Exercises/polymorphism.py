class Animal(object):
    def __init__(self, name):
        self.name = name
    def eatting(self, food):
        print("{name} is eating {food}".format(name = self.name, food =food))
    
class Dog(Animal):
    
    def fetch(self, item):
        print("{name} is fetching the {this}".format(name = self.name, this = item))
        
    def show_affection(self):
        print("{0} wags tail".format(self.name))

        
class Cat(Animal):
    
    def shred(self, item):
        print("{name} is shredding the {this}".format(name = self.name, this = item))
    def show_affection(self):
        print("{0} purrs.".format(self.name))
    
a = Dog("Rover")
b = Cat("Fluff Ball")

a.eatting("trash")
a.fetch("ball")

b.shred("couch")

for obj in (a,b):
    obj.show_affection()
