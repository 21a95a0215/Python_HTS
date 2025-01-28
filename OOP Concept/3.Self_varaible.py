# class Student:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def details(self):
#         print(f"My name is {self.n} and my age is {self.a}.")
# name=input("Enter Name : ")
# age=int(input("Enter Age : "))
# s1=Student(name,age)
# s1.details()


# class Student:
#     def __init__(self):
#         print(id(self))
#         self.n=input("Enter Name :")
#         self.a=int(input("Enter Age :"))
#     def details(self):
#         print(f"My name is {self.n} and My age is {self.a}")
        
# s1=Student()
# s1.details()


# class Student:
#     def __init__(self):
#          print(id(self))
         
# s1=Student()
# print(id(s1))


class Student:
    def __init__(x,name,age):
        x.n=name
        x.a=age
    def details(x):
        print(f"My name is {x.n} and my age is {x.a}.")
    
name=input("Enter Name : ")
age=int(input("Enter Age : "))
s1=Student(name,age)
s1.details()