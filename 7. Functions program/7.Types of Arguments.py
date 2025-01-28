'''  Types of Arguments  '''

'''
    1. Default Arguments
    2. KeyWord Arguments
    3. Required or Positional Arguments
    4. Vaeiable-Length Arguments        '''
    
''' 1. Positional Arguments'''

# def sample(a,b,c):
#     return a,b,c
# print(sample(10,20))

# def sample(a,b):
#     return "Name is :",a,"My age is :",b
# print(sample(30, "Rama Krishna"))

''' 2. Keyword Arguments'''

# def sai(name,age,dep):
#     print("name:",name)
#     print("Age:",age)
#     print("Dep:",dep)
# sai(age=30,name="SaiRam",dep=120)

# def func(name1,message,name2):
#     print("printing the message with",name1,",",message,",and",name2)
# func("John",message="hello",name2="David")

'''Default Arguments'''

# def sample(a,b,c=30):
#     print("Value of a is:",a,"The value of b is:",b,"The value of c is:",c)
# sample(10,20)

# def sample(a,b,c=30):
#     print("Value of a is:",a,"The value of b is:",b,"The value of c is:",c)
# sample(10,20,40)

# def sample(name,age=30):
#     print(name,age)
# sample(name="Rama krishna")
# sample(age=25,name="Rama Raju")
# sample(25,"Alisha")


'''Length Arguments
     (*args)
    (**kwargs)'''
    
# def sample(*a):
#     print(a)
# sample(10,20.5,"Alisha")
    
# def sample(**a):
#     print(a)
# sample(num=10,f=20.5,name="Alisha")

# def sample(*x):
#     for i in x:
#         print(i,end=" ")
# x=eval(input("Enter X Values :"))
# sample(x)

# def sample(**a):
#     print(a)
# a=eval(input("Enter Values :"))
# sample(**a)

