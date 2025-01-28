'''  HAS - A Relationship  '''


class Car:
    def __init__(self):
        self.Cname="Thar"
        self.Ccolor="Black"
        self.Cprice="20 lac"
    def Car_Details(self):
        print(f"Car Name is {self.Cname}")
        print(f"Car color is {self.Ccolor}")
        print(f"Car price is {self.Cprice}")
        print("* " * 20)
        
class Laptop:
    def __init__(self):
        self.Lname="HP"
        self.Lcolor="White"
        self.Lprice="60 k"
    def Laptop_Details(self):
        print(f"Laptop name is {self.Lname}")
        print(f"Laptop color is {self.Lcolor}")
        print(f"Laptop price is {self.Lprice}")
        
        
class Employee:
    def __init__(self):
        self.Ename="Alisha"
        self.Eid="21A95A0215"
        self.Ecompany="Diloite"
        self.c=Car()
        self.l=Laptop()
    def Emp_Details(self):
        print(f"Emp name is {self.Ename}")
        print(f"Emp Id is {self.Eid}")
        print(f"Emp Company is {self.Ecompany}")
        print("* " * 20)
        self.c.Car_Details()
        self.l.Laptop_Details()
        
e=Employee()
e.Emp_Details()