# '''  Accessing Variable  '''

# class A:
#     def __init__(self):
#         self._x=100
    
#     def test(self):
#         print(self._x)

# class B(A):
#     def test1(self):
#         print(self._x)

# a=A()
# a.test()

# b=B()
# b.test1()

# a=A()
# print(a._x)


# '''  Accessing Methods  '''

# class A:
#     def _m1(self):
#         print("m1 Method")

#     def test(self):
#         self._m1()

# class B(A):
#     def new_test(self):
#         self._m1()

# a=A()
# a.test()

# b=B()
# b.new_test()

# a._m1()