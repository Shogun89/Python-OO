class InstanceCounter(object):
    count = 0
    def __init__(self, value):
        self.val = value
        InstanceCounter.count +=1
    def set_value(self, new_value):
        self.val = new_value
    def get_value(self):
        return self.val
    def get_count(self):
        return InstanceCounter.count
    
a = InstanceCounter(6)
b = InstanceCounter(21)
c = InstanceCounter(17)

for obj in [a,b,c]:
    print("Val of Object: {val}".format(val = obj.get_value()))
