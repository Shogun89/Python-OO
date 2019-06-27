class MaxSizeList(object):
    
    def __init__(self, max_size):
        self.max = max_size
        self.main_list = []
        
    def push(self,val):
        self.main_list.append(val)
        my_len = len(self.main_list)
        if (my_len > self.max):
            self.main_list.pop(0)
    def get_list(self):
        return self.main_list

i = MaxSizeList(3)
j = MaxSizeList(1)

for k in ["hello","there",'guy', "here"]:
    i.push(k)
    j.push(k)
    print(i.get_list())
    print(j.get_list())