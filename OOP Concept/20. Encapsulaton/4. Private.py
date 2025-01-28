'''  Accessing Variable Inside the Class  '''

class A:
    def __init__(self):
        self.__x=100

    def test(self):
        print(self.__x)
a=A()
a.test()


'''  Accessing Variable Inside the Child Class  '''

class A:
    def __init__(self):
        self.__x=100

class B(A):
    def test(self):
        print(self.__x)

b=B()
b.test()


'''  Accessing Variable Outside the class  '''

class A:
    def __init__(self):
        self.__x=100
a=A()
print(a.__x)


'''  Accessing Methods inside the class  '''

class A:
    def _m1(self):
        print("m1 Method")

    def test(self):
        self._m1()

a=A()
a.test()


'''  Accessing Methods Inside the child class  '''

class A:
    def _m1(self):
        print("m1 Method")

class B(A):
    def new_test(self):
        self._m1()

b=B()
b.new_test()


'''  Accessing Methods outside the Child Class  '''

class A:
    def _m1(self):
        print("m1 Method")

a=A()
a.__m1()