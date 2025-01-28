# # # x = "a", "b", "c"
# # # print(x)
# # # print(type(x))

# x = "awesome"
# def myfunc():
#     global x 
#     x="fantastic"
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)

# name,place=input("Enter name,place : ").split()
# print(f"My name is {name.strip()} and i'm from {place}")

# # print(help())

# # lst=[i for i in input("Enter inputs : ").split(",")]
# # print(lst)
# # print(type(lst))

# # lst=[input("input : ") for i in range(6)]
# # print(lst)
# # print(type(lst))

'''Sum Game'''

# import os
# from random import randint
# count=0
# while 5==5:
#     os.system("cls")
#     a=randint(1,50)
#     b=randint(1,50)
#     c=a+b
#     question=randint(1,3)
#     print("Type your answer: ")
    
#     match question:
#         case 1 :
#             print(f"? + {b} = {c}")
#             correct_answer=a
#         case 2 :
#             print(f"{a} + ? = {c}")
#             correct_answer=b
#         case 3 :
#             print(f"{a} + {b} = ?")
#             correct_answer=c
            
#     while True:
#         try:
#             your_answer = int(input())
#             break
#         except:
#             print("Please enterthe number only.")
        
#     if your_answer==correct_answer:
#         print("Correct. Press Enter to continue...")
#         count=count+1
#         input()
#     else:
#         print("Not Correct.")
#         break
# print(f"You have answeres {count} questions Correctly")

'''.'''

# import random
# print(random.randint(1,10))


# l=[3,2,1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
#             print(f"1- {l}")
#         print(f"2- {l}")
#     print(f"3- {l}")
# print(f"4- {l}")