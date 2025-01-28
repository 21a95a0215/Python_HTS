''' Class Method  '''


class Person:
    school_name = "Sri Chaitanya"

    @classmethod
    def cls_method(cls):
        school_locaton="Kakinada"
        print(f"My School name is {cls.school_name} and location is {school_locaton}")

Person.cls_method()
p1=Person()
p1.cls_method()


'''  Call class method inside another class method  '''

class Person:
    school_name = "Sri Chaitanya"

    @classmethod
    def cls_method(cls):
        print(f"My school name is {cls.school_name}")
        Person.another_cls_method()

    @classmethod
    def another_cls_method(cls):
        print(f"My school name is {cls.school_name}")

Person.cls_method()



'''  By using Class Method we can perform several operation to static variables  '''



class Test:
    a=10
    b=20

    @classmethod
    def access(cls):
        print(f"The value of a is {cls.a} and the value of b is {cls.b}")

    @classmethod
    def update(cls,x,y):
        cls.a=x
        cls.b=y

    @classmethod
    def delete(cls):
        del cls.a
Test.access()
Test.update(30,40)
Test.access()
Test.delete()
print(Test.__dict__)
