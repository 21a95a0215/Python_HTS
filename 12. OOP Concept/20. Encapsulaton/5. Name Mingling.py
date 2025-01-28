'''  Accessing Variable Outside the Class  '''
class A:
    def __init__(self):
        self.__x=100

a=A()
print(a._A__x)