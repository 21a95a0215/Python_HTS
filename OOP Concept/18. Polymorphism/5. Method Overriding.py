# '''  Method Overriding  '''


# class Parent:
#     def m1(self):
#         print('This is parent m1')
        
# class Child(Parent):
#     pass

# c=Child()
# c.m1()


# class Parent:
#     def m1(self):
#         print('This is parent m1')
        
# class Child(Parent):
#     def m1(self):
#         print('This is child m1')
        
# c=Child()
# c.m1()


# class Circle:
#     def area(self,r):
#         print(3.14*r*r)
        
# class Triangle(Circle):
#     def area(self,b,h):
#         print(0.5*b*h)
        
# class Square(Circle):
#     def area(self, s):
#         print(s*s)
        
# t=Triangle()
# t.area(2.3,5.6)


# class Animal:
#     def sound(self):
#         print("Animal make different sounds")
        
# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks!")
        
# class Cat(Animal):
#     def sound(self):
#         print("Cat Meows!")
        
# if __name__=="__main__":
#     d=Dog()
#     d.sound()