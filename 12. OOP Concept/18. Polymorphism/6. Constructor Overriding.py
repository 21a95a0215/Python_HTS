# '''  Constructor Overriding  '''


# class Parent:
#     def __init__(self):
#         print("This is Parent m1")
        
# class Child(Parent):
#     pass

# c=Child()



# class Parent:
#     def __init__(self):
#         print("This is Parent m1")
        
# class Child(Parent):
#     def __init__(self):
#         print("This is Child m1")
        
# c=Child()



# '''  Problem without Constructor Overriding  '''

# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def details(self):
#         print(f"My name is {self.name}")
#         print(f"My age is {self.age}")
        
# class Student:
#     def __init__(self,name,age,course,college):
#         self.name=name
#         self.age=age
#         self.course=course
#         self.college=college
        
#     def details(self):
#         print(f"My name is {self.name}")
#         print(f"My age is {self.age}")
#         print(f"My course is {self.course}")
#         print(f"My college is {self.college}")
        
# class Employee:
#     def __init__(self,name,age,dep,company):
#         self.name=name
#         self.age=age
#         self.dep=dep
#         self.company=company
        
#     def details(self):
#         print(f"My name is {self.name}")
#         print(f"My age is {self.age}")
#         print(f"My department is {self.dep}")
#         print(f"My Company is {self.company}")
        
# e=Employee("Ram",30,"IT","Wipro")
# e.details()



'''  Problem Overcome With Constructor Overriding  '''

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        
class Student(Human):
    def __init__(self,name,age,course,college):
        super().__init__(name,age)
        self.course=course
        self.college=college
        
    def details(self):
        super().details()
        print(f"My course is {self.course}")
        print(f"My college is {self.college}")
        
class Employee(Human):
    def __init__(self,name,age,dep,company):
        super().__init__(name,age)
        self.dep=dep
        self.company=company
        
    def details(self):
        super().details()
        print(f"My department is {self.dep}")
        print(f"My Company is {self.company}")
        
e=Employee("Ram",30,"IT","Wipro")
e.details()