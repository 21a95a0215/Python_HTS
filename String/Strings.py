'''String '''
# s1='Welcome to python Programming'
# print(s1)

# d="alisha"
# print(d)

# address="""
# 7-2,
# Ramalaya street,
# Vinukonda,
# Guntur,
# Andhra pradesh"""
# print(address)

# s1="Welcome to 'python programming'"
# s2='welcome to "python programming"'
# print(s1)
# print(s2)
 
 
'''Doc string'''

# def sample():
#     """The above 
#     line gives s1 data"""
    
#     s1="hello world"
#     return s1
# print(sample.__doc__)
# print(sample())

# import random as ran
# print(ran.randint)

# from random import *
# print(randint.__doc__)
# print(randrange.__doc__)

'''Index'''

# s1="Welcome to python"
# print(s1[3])
# print(s1[7])
# print(s1[8])
# print(s1[-1])


'''Slice Operator'''

# s1="Welcome to python"
# print(s1[1:5])
# print(s1[0:10:2])
# print(s1[::])
# print(s1[::2])
#print(s1[:8:2])

# print(s1[-5:-1])
# print(s1[-10:-1:2])
# print(s1[::])
# print(s1[::-2])
# print(s1[:-8:-2])

'''String Method'''

# s1="welcome to python"
# print(s1.startswith("welcome"))
# print(s1.startswith("Welcome"))
# print(s1.endswith("python"))
# print(s1.endswith("Python"))
# print(s1.isalpha())

# s2="Welcometopython"
# print(s2.isalpha())

# s2="1Welcometopython"
# print(s2.isalnum())

# s3='1*2'
# print(s3.isalnum())

# s4="12"
# print(s4.isdigit())

# s5="1hello"
# print(s5.islower())

# s5="1HELLO"
# print(s5.isupper())

# s5="1Hello"
# print(s5.istitle())

# s5="1hEllo"
# print(s5.istitle())

# s5="  "
# print(s5.isspace())

'''Change Case Method'''

# s="Welcome to python"
# print(s.lower())

# print(s.upper())

# print(s.swapcase())

# print(s.title())

# print(s.capitalize())

'''Length of a string'''

# s1="Hello World"
# print(len(s1))
# print(s1.__len__())

'''Count of a Character'''

# s1="Hello World"
# print(s1.count('o'))
# print(s1.count('o',6))

'''replace a word'''

# s1="Hello World"
# print(s1.replace(" ", "Rk"))
# print(s1)

'''Split Method'''

# s1="Hello World"
# print(s1.split( ))
# print(s1.split('r'))

'''Join Method'''

# s1="Hello World"
# print('*'.join(s1))

# s1=["Hello ", "World"]
# print('*'.join(s1))

# s1="Hello World"
# print('.'.join(s1))

'''Strip Method'''

# s1="  Ramaraju  "
# print(len(s1))
# print(len(s1.strip()))
# print(s1.strip())

'''Fill Method'''

# s1="Rama"
# print(s1.zfill(12))

'''rjust method'''

# s1="Rama"
# print(s1.rjust(8))

# s1="Rama"
# print(s1.rjust(8, "?"))

# s1="Rama"
# print(s1.ljust(8, "*"))

'''Center Method'''

# s1="Rama"
# print(s1.center(8))

# s1="Rama"
# print(s1.center(12, "*"))

'''Enumerate Method'''

# s1="Rama"
# for i in enumerate(s1):
#     print(i)
    
    
    
