# '''  Handling Errors with Try and Except  '''

# print('1')
# print('2')
# try :
#     print(3/'3')
# except Exception as e:
#     print(e)
# print('4')


# ''''''

# l=[10,20,30]
# try:
#     print(l[6])
# except Exception as e:
#     print(e)
    

# '''  Customised Exception Message  '''

# l=[10,20,30]
# try:
#     print(l[6])
# except Exception as e:
#     print(e)
#     print('The list index value we called is out of range')


# '''  Exception of Multiple Erroes  '''

# l = [10,20,30]
# try:
#     print(l[6])
#     print(100/0)
# except ZeroDivisionError as z:
#     print(z)
# except IndexError as i:
#     print(i)
    
    
# '''  ZeroDivision Error  '''

# a=int(input("Enter a Value: "))
# b=int(input("Enter b Value: "))
# try:
#     print(a//b)
# except ZeroDivisionError as z:
#     print(z)
    

# '''  Handling Error with alternate handling code  '''

# a=int(input("Enter a Value: "))
# b=int(input("Enter b Value: "))
# try:
#     print(a//b)
# except ZeroDivisionError:
#     print(a+b)


# ''' Name Error  '''



# a=int(input("Enter a Value: "))
# b=int(input("Enter b Value: "))
# try :
#     print(a+c)
# except NameError as n:
#     print(n)


# '''  Type Error  '''

# a=int(input("Enter a Value: "))
# b=int(input("Enter b Value: "))
# try:
#     result = a+b
# except TypeError as t:
#     print(t)
    
    
# a=int(input("Enter a Value: "))
# b=int(input("Enter b Value: "))
# try:
#     result = a+b
# except TypeError :
#     print(TypeError)


# '''  Index Error   '''

# l=[10,20,30,40]
# print(l[18])


# l=[10,20,30,40]
# try :
#     print(l[int(input("Enter the list Index: "))])
# except IndexError as i:
#     print(i)
    

# ''' Key Error  '''

# d={1:"Ram",2:"Seetha"}
# print(d[3])


# d={1:"Ram",2:"Seetha"}
# try:
#     print(d[3])
# except KeyError as K:
#     print(K)


# '''  FileNotFound  '''

# try :
#     f=open('abc.txt')
# except FileNotFoundError as f:
#     print(f)


# '''  ModuleNotFoundError  '''

# import pyqt5


'''  OverFlowError  '''

import math
print(math.factorial(64521354534534546))
