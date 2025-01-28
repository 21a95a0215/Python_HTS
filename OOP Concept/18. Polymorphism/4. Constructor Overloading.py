# '''  Constructor Overloading Which is not possible  '''


# class Test:
#     def __init__(self,a):
#         print(a)
        
#     def __init__(self,a,b):
#         print(a,b)
        
# t=Test(10)


# '''  Constructor Overloading using Multidispatch Module  '''


# from multipledispatch import dispatch
# class Test:
#     @dispatch(int)
#     def __init__(self,a):
#         print(a)
        
#     @dispatch
#     def __init__(self,a,b):
#         print(a,b)
        
# t=Test(10)
# t1=Test(10,20)