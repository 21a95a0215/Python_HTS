'''  Super Function  '''


'''  WithOut Super Function  '''


class Student:
    def __init__(self,name,Sid,age):
        self.n=name
        self.Sid=Sid
        self.a=age
    def Details(self):
        print(f"Name is {self.n}")
        print(f"Student iD is {self.Sid}")
        print(f"Age is {self.a}")
        
class Employee:
    def __init__(self,name,Eid,age):
        self.n=name
        self.Eid=Eid
        self.a=age
    def Details(self):
        print(f"Name is {self.n}")
        print(f"Employee ID is {self.Eid}")
        print(f"Age is {self.a}")

s1=Student("Alisha","21A95A0215",24)
s1.Details()


'''  With Super() Function  '''


class Person:
    def __init__(x,name,age):
        x.n=name
        x.a=age
    def Details(x):
        print(f"Name is {x.n}")
        print(f"Age is {x.a}")
        
class Employee(Person):
    def __init__(x, name,Eid,age):
        super().__init__(name,age)
        x.Eid=Eid
    def Details(x):
        super().Details()
        print(f"Employee ID is {x.Eid}")
        
class Student(Person):
    def __init__(x, name,Sid, age):
        super().__init__(name, age)
        x.Sid=Sid
    def Details(x):
        super().Details()
        print(f"Student Id is {x.Sid}")
        
e=Employee("Alisha",'5A0215',26)
e.Details()

s=Student('Alisha','21A95A0215',24)
s.Details()      