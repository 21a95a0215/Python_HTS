# '''  Concreate Class Vs Abstract Class  '''

# class Test:
#     def m1(self):
#         pass
# t=Test()
# t.m1()


# '''  Abstract Class with Abstract Method  '''

# from abc import ABC , abstractmethod

# class test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass

# t=test()


# '''  Abstract Class without Abstract Method  '''

# from abc import ABC , abstractmethod

# class Test(ABC):
#     def m1(self):
#         pass

# t=Test()


# '''  Abstract Class with Abstract MEthod with implementation.  '''

# from abc import ABC , abstractmethod

# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass

# class Child(Test):
#     def m1(self):
#         print("Hello ")
        
# c=Child()
# c.m1()


# '''  Abstract Class with Abstract Method with implementation.  '''

# from abc import ABC , abstractmethod

# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass

# class Child(Test):
#     pass       # Here m1 method is not implemented then it gives error.

# c=Child()
# c.m1()