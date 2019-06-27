class MyNum(object):
    def __init__(self,value):
        self.val = value
    def increment_num(self):
        self.val += 1
        
i  = MyNum(10)

for j in range(10):
    i.increment_num()
    print(i.val)