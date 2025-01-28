# class Person:
#     def __init__(self):
#         self.n=input("Enter Name: ")
#         self.a=int(input("Enter Age: "))
        
        
# p1=Person()
# p2=Person()

# print(p1.__dict__)
# print(p2.__dict__)
    
    
    
# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
        
        
# p1=Person()
# p1.details(input("Enter Name: "),input("Enter Age: "))
# p2=Person()
# p2.details(input("Enter Name: "),input("Enter Age: "))

# print(p1.__dict__)
# print(p2.__dict__)
    
    
    
    
# class Person:
#     school_name="Sri chaitanya"
#     def Details(self):
#         self.n=input("Enter Name: ")
#         self.a=int(input("Enter age: "))
        
# print(Person.school_name)
# p1=Person()
# p1.Details()
# p2=Person()
# p2.Details()

# print(p1.__dict__)
# print(p2.__dict__)



# class Person:
#     def __init__(self,name):
#         self.n=name
# p1=Person("Ram")
# print(p1.__dict__)
# p1.age=30
# print(p1.__dict__)



'''  Accessing Instance Variable  '''


# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#         print(f"My Name is {self.n} and my Age is {self.a}.")
# p1=Person("Ram",30)


# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# p1=Person("Ram",30)
# print(f"My Name is {p1.n} and my age is {p1.a}")



'''  Delete Instance Variable  '''


# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def deleteDetails(self):
#         del self.a
# p1=Person("Ram",30)
# print(p1.__dict__)
# p1.deleteDetails()
# print(p1.__dict__)


# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#         del self.a 
# p1=Person("Ram",30)
# print(p1.__dict__)


# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# p1=Person("Ram",30)
# print(p1.__dict__)

# del p1.a
# print(p1.__dict__)