class Person(object):
    def set_age(self, val):
        self.age = val
    def get_age(self):
        return self.age
     
     
Me = Person()
You = Person()

Me.set_age(30)
You.set_age(20)

print(Me.get_age())
print(You.get_age())