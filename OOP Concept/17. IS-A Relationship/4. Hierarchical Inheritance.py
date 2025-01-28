'''  Heirarchical Inheritance  '''


class A:
    def method1(self):
        print("Parent Class Method1")
        
class B(A):
    def method2(self):
        print("Child Class Method2")
        
class C(A):
    def method3(self):
        print("Child Class Method3")
        
b=B()
b.method1()
b.method2()

c=C()
c.method1()
c.method3()