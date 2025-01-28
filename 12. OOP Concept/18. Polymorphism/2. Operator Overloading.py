# '''  Operator Overloading  '''


# print(10+20)
# print('Ram ' + 'Krishna')


# ''' Without Magic Method '''
# class Employee:
#     def __init__(self,salary):
#         self.salary = salary
# class Student:
#     def __init__(self, stipend):
#         self.stipend = stipend
        
# e=Employee(10000)
# s=Student(5000)
# print(e+s)


'''  With Magic Method  '''
class Employee:
    def __init__(self, salary):
        self.salary=salary
    
    def __add__(self,other):
        return self.salary+other.stipend
    
class Student:
    def __init__(self,stipend):
        self.stipend=stipend
        
e=Employee(10000)
s=Student(5000)

print(e+s)