'''  Instance Method  '''


class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        result=self.a+self.b
        print(f"adding result is {result}")

    def sub(self):
        result=self.a-self.b
        print(f"Subtraction result is {result}")

c1=Calculator(10,20)
c1.add()
c1.sub()



'''call instance method inside another method'''


class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        result=self.a+self.b
        print(f"Adding result is {result}")
        self.sub()

    def sub(self):
        result=self.a-self.b
        print(f"Subtraction result is {result}")

c1=Calculator(10,20)
c1.add()


'''  By using instance method we can perform various operations  '''


class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def access(self):
        print(f"The value of a is {self.a} and tghe value of b is {self.b}")

    def update(self,x,y):
        self.a=x
        self.b=y

    def delete(self):
        del self.a

t1=Test(10,20)
print(t1.__dict__)
t1.access()
t1.update(30,40)
t1.access()
t1.delete()
print(t1.__dict__)