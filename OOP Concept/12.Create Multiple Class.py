class Student:
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def Details(self):
        print('Person Information')
        print(f"Name is {self.n}")
        print(f"Age is {self.a}")
        print(30 * '=')

class Staff:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def details(self):
        print("Staff Informaton")
        print(f"Name is {self.n}")
        print(f"Age is {self.a}")
        
s1=Student("Ram",30)
s1.Details()

f1=Staff("Prof. Hema chandra",56)
f1.details()