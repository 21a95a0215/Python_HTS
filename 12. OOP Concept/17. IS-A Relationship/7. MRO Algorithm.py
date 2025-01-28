'''  Method Resolution Order (MRO) Algorithm / C3 Linearization  '''


class Myclass:
    pass

print(issubclass(Myclass,object))

a=Myclass()
print(isinstance(a,object))

'''==============================='''


class Parent:
    pass
class Child(Parent):
    pass

print(issubclass(Parent,object))
print(issubclass(Child,object))
print(issubclass(Child,Parent))


'''  MRO Algorithm  '''


class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(C):
    pass
class F(D,E):
    pass

print(A.__mro__)
print(D.__mro__)
print(F.__mro__)

'''==============================='''



class A:
    def m1(self):
        print("A of m1 Method")
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(C):
    pass
class F(D,E):
    pass

f=F()
f.m1()
print(F.__mro__)