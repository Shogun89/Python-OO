class A(object):
    def do_something(self):
        print("Doing something in A")
        
class B(A):
    pass

class C(A):
    
    def do_something(self):
        print("Doing something in C")
        
class D(B,C):
    
    pass

d_instance = D()
d_instance.do_something()
print(D.mro())