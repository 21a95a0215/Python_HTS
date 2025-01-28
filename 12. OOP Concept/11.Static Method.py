'''  Static Method  '''


from re import sub


class Calculator:
    @staticmethod
    def add(a=10,b=20):
        print(f"Addition result is {a+b}")

    def sub(a,b):
        print(f"Subtraction result is {a-b}")

Calculator.add()
c1=Calculator()
c1.add()


'''  Calling Static method inside the class  '''



class Calculator:
    @staticmethod
    def add(a=10,b=20):
        print(f"Addition result is {a+b}")
        Calculator.sub(30,40)

    def sub(a,b):
        print(f"Subtraction result is {a-b}")


Calculator.add()