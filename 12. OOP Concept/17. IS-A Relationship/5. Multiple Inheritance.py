'''  Multiple Inheritance  '''

'''  Multiple parents have one child class.  '''

class A:
    def method1(self):
        print("A class Method1")
    
class B:
    def method2(self):
        print("B Class Method2")
        
class C(A,B):
    def method3(self):
        print("C Class Method3")
        
c=C()
c.method1()
c.method2()
c.method3()


'''  If both parents have same methods  '''


class A:
    def method1(self):
        print("A class method1")
class B:
    def method1(self):
        print('B Class Method1')
class C(A,B):
    pass

c=C()
c.method1()