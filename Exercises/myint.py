class MyInt(object):
    def set_value(self, val):
        try:
            val = int(val)
        except ValueError:
            return 
        self.val = val
    
    def get_value(self):
        return self.val
    def increment_value(self):
        self.val += 1
    
i = MyInt()
i.set_value(23)
print(i.get_value())
i.increment_value()
print(i.get_value())
