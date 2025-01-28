'''  Instance __dict__  '''

class MyClass:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
        
obj = MyClass("Alice", 30)
print(obj.__dict__)


'''  Class __dict__  '''

class MyClass:
    class_var = "I am a class variable"
    
    def method(self):
        print("This is a method.")
print(MyClass.__dict__)