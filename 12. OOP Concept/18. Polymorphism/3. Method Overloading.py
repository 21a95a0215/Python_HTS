# '''  Method Overloading  '''


# class Test:
#     def m1(self,a):
#         print(a)
    
#     def m1(self,a,b):
#         print(a,b)
        
#     def m1(self,a,b,c):
#         print(a,b,c)
        
# t=Test()
# # t.m1(10)
# # t.m1(10,20)
# t.m1(10,20,30)


# '''  Method Overloading Using Variable Length Arguments.  '''


# class Test:
#     def m1(self, *a):
#         print(a)
        
# t=Test()
# t.m1(10)
# t.m1(10,20,30)


# '''  Method Overloading using Multipledispatch  '''

# from multipledispatch import dispatch
# class Test:
#     @dispatch(int,int)
#     def add(a,b):
#         print(a+b)
        
#     @dispatch(float,float)
#     def add(a,b):
#         print(a+b)
        
#     @dispatch(int,float)
#     def add(a,b):
#         print(a+b)
        
#     @dispatch(int,int,int)
#     def add(a,b,c):
#         print(a+b+c)
        
# t=Test()
# t.add(10,20)
# t.add(40,13.4)
# t.add(10,20,30)


