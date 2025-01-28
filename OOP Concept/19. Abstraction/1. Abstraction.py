# '''  Example of Using abc Module and ABC Class  '''
# from abc import ABC , abstractmethod 

# '''  Animal Class is Child Class of ABC  '''
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
    
#     def sleep(self):
#         print("This animal is sleeping.")
        
# class Dog(Animal):
#     def sound(self):
#         print("Woof! Woof!!")
     
# # animal = Animal()  # This will raise an error because Animal is abstract. 
# dog=Dog()
# dog.sound()
# dog.sleep()


# '''  Use of Abstract Class  '''

# from abc import ABC , abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def Color(self):
#         pass 
#     @abstractmethod
#     def Model(self):
#         pass
    
# class Car(Vehicle):
#     def __init__(self,company):
#         self.company = company
        
#     def Color(self,colr):
#         print(f"My Car company is {self.company} and the color is {colr}")
        
#     def Model(self,mdl):
#         print(f"My {self.company} car belongs to {mdl}")
        
# c = Car("Suzuki")
# c.Color("Red")
# c.Model(2020)