''' IS-A Relationship / Inheritance  '''


class A:
    def method1(self):
        print("A Class Method1")
    def method2(self):
        print("A Class Method2")
class B:
    def Method3(self):
        print("B Class Method3")
        
b=B()
b.Method3()
b.method1()

'''========================'''


class A:
    def  method1(self):
        print("A Class Method1")
    def method2(self):
        print("A Class Method2")
class B(A):
    def method3(slef):
        print("B Class Method3")
        
b=B()
b.method3()
b.method1()

'''==========================='''


class A:
    def __init__(self):
        self.x=10
        self.y=20
        
class B(A):
    def Details(self):
        print(f"X Value is {self.x}")
        print(f"Y Value is {self.y}")
        
b=B()
b.Details()

'''  Without Inheritance  '''


class A:
    def __init__(self):
        self.x=10
        self.y=20
        
class B:
    def __init__(self):
        self.x=10
        self.y=20
    def Details(self):
        print(f"X Value is {self.x}")
        print(f"Y Value is {self.y}")
        
b=B()
b.Details()

'''==========================='''


class A:
    def m1(self):
        self.x=10
        print(f"X Value is {self.x}")
        
class B(A):
    pass
b=B()
b.m1()

'''=============================='''


class A:
    def m1(self):
        self.x=10
        print(f"X Value is {self.x}")
        
class B(A):
    def m2(self):
        self.x=20
        
b=B()
b.m1()