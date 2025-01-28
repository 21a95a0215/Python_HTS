'''  Passing one class members to another class  '''


class Student:
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def Details(self):
        print(f"Name is {self.n}")
        print(f"Age is {self.a}")

class Staff:
    @staticmethod
    def Modify(x):
        x.a=30

s1=Student("Ram",25)
s1.Details()
Staff.Modify(s1)
s1.Details()



'''  Here we are passing only one object from one class to another class  '''

class Student:
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def Details(self):
        print(f"Name is {self.n}")
        print(f"Age is {self.a}")

class Staff:
    @staticmethod
    def modify_age(x):
        print(x)

s1=Student("Ram",30)
Staff.modify_age(s1.a)