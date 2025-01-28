'''  Accessing Variable  '''

class A:
    def __init__(self):
        self.x=100
    
    def test(self):
        print(self.x)
    
class B(A):
    def test1(self):
        print(self.x)

a=A()
a.test()
b=B()
b.test1()
a=A()
print(a.x)


'''  Accessing Methods  '''

class A:
    def m1(self):
        print("m1 Method")

    def test(self):
        self.m1()

class B(A):
    def new_test(self):
        self.m1()

a=A()
a.test()

b=B()
b.new_test()

a.m1()