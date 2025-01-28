# '''  Examples of Operator Overriding  '''

# '''  1. Overloading the + Operator  '''

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
#     def __add__(self,other):
#             return Point(self.x + other.x, self.y + other.y)
    
#     def __repr__(self):
#          return f"Point({self.x}, {self.y})"
     
# p1 = Point(1,2)
# p2=Point(3,4)
# p3=p1+p2
# print(p3)


'''  Overloading the == Operator'''

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
p1 = Point(1,2)
p2 = Point(1,2)
p3 = Point(3,4)
print(p1 == p2)
print(p1 == p3)

