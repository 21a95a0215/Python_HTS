'''  Assertions  '''

a=100
print(1)
print(2)
assert a==100
print(3)
print(4)



a=100
print(1)
a=20
print(2)
assert a==100
print(3)
print(4)



a=100
print(1)
a=20
print(2)
assert a==100, "a value is updated."
print(3)
print(4)



x=0
assert x>0, "X should be Positive"
assert x<3, "X should be less than 3"



l=["Ram", "Gopi", "Seetha"]
assert input("Enter Name: ") in l, "This name is not present."
print(l)




l = ["Ram", "Gopi", "Seetha"]
try:
    assert input("Enter Name: ") in l, "This name is not present."
except AssertionError as a:
    print(a)
print(l)



'''  Example: Without Assert  '''

def prime_number(n):
    if n>1:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            return "Given number is a Prime number."
        else:
            return "Given number is Not a Prime number."
    else:
        return "Prime number only above one not less than or negative number."
print(prime_number(5))
print(prime_number(4))
print(prime_number(0))



'''  Example: With Assertion  '''

def prime_number(n):
    assert n>1, "Prime number only above one not less than or negative numbers."
    counter=0
    for i in range(1,n+1):
        if n%i==0:
            counter+=1
    if counter == 2:
        return "Given number is Prime Number."
    else:
        return "Given number is Not a Prime Number."
print(prime_number(5))
print(prime_number(4))
print(prime_number(0))



'''  1. Simple Assertion  '''
age = 25
assert age >= 18, "Age must be 18 or Older."



'''  2. Checking List Length  '''
names = ["Alice", "Bob", "Charlie"]
assert len(names) == 3, "List must contain exactly 3 names"



'''  3. Type Checking  '''
value = 10.5
assert isinstance(value, float), "Value should be a float"



'''  4. Check for Non-empty String  '''
username = "john_doe"
assert username, "Username cannot be empty"



'''  5. Dividing by Zero Prevention  '''
denominator = 5
assert denominator != 0, "Denominator cannot be zero"
result = 10 / denominator
print(result)



'''  6. Complex Condition  '''
score = 85
assert 0 <= score <= 100, "Score must be between 0 and 100"



'''  7. Using Assertions in Functions  '''
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

result = divide(10, 2)



'''  8. Using Assertions in Loops  '''
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    assert num > 0, f"Invalid number: {num}, it must be positive"



'''  9. Testing Complex Data Structures  '''
user_data = {"name": "Alice", "age": 30}
assert "name" in user_data, "Name is missing"
assert user_data["age"] >= 18, "Age must be 18 or older"



'''  10. Using Assertions with Custom Objects  '''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        assert self.price >= 0, "Price cannot be negative"
        self.price *= 0.9 

product = Product("Laptop", 1000)
product.apply_discount()