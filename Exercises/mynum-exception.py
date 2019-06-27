class MyNum(object):
    def __init__(self,value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value
    def increment_num(self):
        self.val += 1
        
i  = MyNum('hello')
j  = MyNum(100)
for k in range(10):
    i.increment_num()
    j.increment_num()
    
    print(i.val)
    print(j.val)