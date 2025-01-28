'''  Single Inheritance  '''


class A:
    def Method1(self):
        self.x=10
        self.y=20
        print(f"Value of X is {self.x}")
        print(f"Value of Y is {self.y}")
    def Method2(self):
        self.z=30
        print(f"Value of z is {self.z}")

class B(A):
    pass
b=B()
b.Method1()
b.Method2()

'''  Parent Class can only access of there own properties but child class can access both parent and it's own properties. '''


class A:
    def method1(self):
        print("A Class Method1")
    def method2(self):
        print("A Class Method2")
class B(A):
    def method3(self):
        print("B Class Method3")
a=A()
a.method1()
a.method2()

b=B()
b.method3()
b.method1()
b.method2()

'''  Child Class can access constructor, instance method, Staticmethod, Classmethod.'''


class A:
    a=10
    print(f"Value of a is {a}")
    
    def __init__(self):
        self.b=15
        print(f"Value of b is {self.b}")
        
    def method1(self):
        y=20
        self.x=30
        print(f"Value of x is {self.x}")
        print(f"Value of y is {y}")
        
    @classmethod
    def cm(cls):
        cls.cmv=40
        print(f"Value of CMV is {cls.cmv}")
        
    @staticmethod
    def sm():
        smv=50
        print(f"Value of SMV is {smv}")

class B(A):
    pass

b=B()
b.method1()
b.cm()
b.sm()