import random
class Person(object):
    def set_age(self):
        self.age = random.randint(1,10)
        print(self.age)
        
Me = Person()
Me.set_age()
Me.set_age()