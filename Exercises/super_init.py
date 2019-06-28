import random

class Animal(object):
    
    def __init__(self, name):
        self.name = name
        
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.breed = random.choice(['Beagle','Dachsund','German Shepard'])
    
    def fetch(self,thing):
        print("{0} goes after the {1}".format(self.name, thing))
        
D = Dog("Max")

print(D.name)
print(D.breed)