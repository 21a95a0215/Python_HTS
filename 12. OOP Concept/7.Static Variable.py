'''  Static Variable  '''

'''  Creation of Static Variable Inside the class  '''

# class Person:
#     school_name = "Sri Chaitanya"
# print(Person.school_name)
# p1=Person()
# print(p1.school_name)
# print(Person.__dict__)
# print(p1.__dict__)



'''  Creation of Static Variable OutSide the class  '''

# class Person:
#     pass 
# p1=Person()
# Person.school_name = "Sri Chaitanya"
# print(Person.__dict__)



'''  Creation of Static Variable Inside the Constractor  '''

# class Person:
#     def __init__(self):
#         Person.school_name = "Sri Chaitanya"
# p1=Person()
# print(Person.__dict__)



'''  Creation of Static Variable Inside the Instance Method  '''


# class Person:
#     def details(self):
#         Person.school_name = "Sri Chaitanya"
# p1=Person()
# p1.details()
# print(Person.__dict__)



'''  Creation of Static Variable Inside the Class Method by using Class Name  '''

# class Person:
#     @classmethod
#     def class_method(cls):
#         Person.school_name="Sri Chaitanya"
# Person.class_method()
# print(Person.__dict__)



'''  Creation of Static Variable Inside the Class Method by using cls Variable  '''

# class Person:
#     @classmethod
#     def class_method(cls):
#         cls.school_name = "Sri Chaithanya"
    
# Person.class_method()
# print(Person.__dict__)



'''  Creation of Static Variable Inside the Class Method by using Class Name  '''

# class Person:
#     @staticmethod
#     def static_method():
#         Person.school_name = "Sri Chaitanya"
        
# Person.static_method()
# print(Person.__dict__)



'''  Accessing the Static Variable  '''

'''  Accessing the Static Variable Outside the Class  '''

# class Person:
#     school_name ="Sri Chaitanya"
# print(Person.school_name)



'''  Accessing the Static Variable Inside the constructor  '''

# class Person:
#     school_name = "Sri Chaitanya"
    
#     def __init__(self):
#         print(Person.school_name)
# p1=Person()



'''  Accessing the Static Variable Inside the Instance Method  '''

# class Person:
#     school_name = "Sri Chaitanya"
#     def __init__(self):
#         print(Person.school_name)
# p1=Person()
    
    
    
'''  Accessing the Static Variable Inside the Class Method  '''
# class Person:
#     school_name = "Sri Chaitanya"
#     @classmethod
#     def class_method(cls):
#         print(Person.school_name)
        
# Person.class_method()



'''  Accessing the Static Variable Inside the Static Method  '''
# class Person:
#     school_name="Sri Chaitanya"
#     @classmethod
#     def static_method(cls):
#         print(Person.school_name)
# Person.static_method()



'''  Modify static variable  '''

'''  Modify the Static Variable Outside the class  '''

# class Person:
#     school_name="Sri Chaitanya"
# print(Person.school_name)
# Person.school_name="Modified Sri Chaitanya"
# print(Person.school_name)



'''  Modify the static variable inside the class and inside the constructor  '''

# class Person:
#     school_name="Sri Chaitanya"
#     def __init__(self):
#         Person.school_name = "Modified Sri Chaitanya"

# print(Person.school_name)
# p1=Person()
# print(Person.school_name)

