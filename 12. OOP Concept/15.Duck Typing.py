'''    Duck Typing    '''



class A:
    def m1(self):
        print('A->m1')
class B:
    def m1(self):
        print('B->m1')
class C:
    def m1(self):
        print('C->m1')

def search(x):
    x.m1()

a=A()
search(a)

b=B()
search(b)






class Duck:
    def swim(self):
        print("Duck is Swimming")

    def fly(self):
        print("Duck is Flying")

class Whale:
    def swim(self):
        print("Whale is Swimming")

for i in [Duck(),Whale()]:
    i.swim()
    i.fly()