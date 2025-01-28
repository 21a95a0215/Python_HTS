'''  Hybrid Inheritance  '''


class A:
    def method1(self):
        print("A class Method1")
class B(A):
    def method2(self):
        print("B Class Method2")
class C(A):
    def method3(self):
        print("C Class Method3")
class D(B,C):
    def method4(self):
        print("D Class Method4")
        
d=D()
d.method1()
d.method2()
d.method3()
d.method4()