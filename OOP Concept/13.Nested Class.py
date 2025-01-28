'''  Nested Class  '''



class Outer:
    def __init__(self):
        print("Outer Class")

    class Inner:
        print("Inner Class")
        
o=Outer()

i=o.Inner()
i1=Outer.Inner()
i2=Outer().Inner()



'''  Object creation inside outer class  '''

class Outer:
    def __init__(self):
        print("Outer Class")
    class Inner:
        def __init__(self):
            print("Inner Class")
    i= Inner()
o=Outer()



'''  Object Creation inside Inner Class  '''



class Outer:
    def __init__(self):
        print("Outer Class")
    class Inner:
        def __init__(self):
            print("Inner Class")
        class Inner1:
            def __init__(self):
                print("Inner Class in Inner")
        
o=Outer()
i=o.Inner()
i1=i.Inner1()