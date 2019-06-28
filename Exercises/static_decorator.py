class InstanceCounter(object):
    count = 0
    def __init__(self, value):
        self.val = self.filter_int(value)
        InstanceCounter.count +=1
    @staticmethod
    def filter_int(value):
        if not isinstance(value, int):
            return 0
        else:
            return value
    
a = InstanceCounter(6)
b = InstanceCounter(21)
c = InstanceCounter(17)

for obj in [a,b,c]:
    print("Val of Object: {val}".format(val = obj.val))