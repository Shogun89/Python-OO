class Animal(object):
    def __init__(self, name):
        self.name = name
    def eatting(self, food):
        print("{name} is eating {food}".format(name = self.name, food =food))
    
class Dog(Animal):
    
    def fetch(self, item):
        print("{name} is fetching the {this}".format(name = self.name, this = item))
    
class Cat(Animal):
    
    def shred(self, item):
        print("{name} is shredding the {this}".format(name = self.name, this = item))
    
a = Dog("Rover")
b = Cat("Fluff Ball")

a.eatting("trash")
a.fetch("ball")

b.shred("couch")