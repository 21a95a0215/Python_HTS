# l=[]
# print(type(l))
# l2=list(1,2,4)
# print(l2)

# k=eval(input("enter values : "))
# print(k)
# # 0 1 2 3 4 5
# k=[2,4,5,6,8,9,9]
# # -6-5-4-3-2-1
# print(k)

# l=["apple",5,6.0]
# print(l[0])

'''using range in list'''


# j=list(range(1,20,2))
# print(j)
# 0(0,1,2),1{0,1,2},2[0,1,2]
# e=[(1,3,4),{1,3,8},[1,2,8],{'name':"alisha"}]
# print(type(e))
# print(type(e[3]))

'''update the value'''

# lst=[8,3,7,9,5]
# lst[2:4]=99,858
# print(lst)

#print list by using for loop
# p=[8,9,8,4,3,"alisha"]
# for i in p:
#     print(i,end=" ")
    
# n=eval(input("enter values : "))
# i=0
# while i<len(n):
#     print(n[i])
#     i=i+1

'''to find -ve and +ve index'''
# e=[3,8,9,4,5]

# for i in range(len(e)):
#     print(f"{e[i]} is present in {i}/{i-len(e)}")
    
'''APPEND METHOD'''

# LIS=[8,7,5,9,2]
# LIS.append(77)
# print(LIS)

'''INSERT'''
# LIS1=[7,4,3,9,6]
# LIS1.insert(0,99)
# print(LIS1)
# LIS1.insert(-20,6)
# print(LIS1)
# LIS1.insert(20,10)
# print(LIS1)

'''MIN, MAX ,SUM'''
# LT=[9,6,5]
# B=min(LT)
# print(B) #OR print(min(LT))
# print(sum(LT))
# print(max(LT))


'''without using eval'''


# L=[]
# N=int(input("enter  : "))
# for i in range(0,N):
#     ELE=int(input("ELEMENTS : "))
#     L.append(ELE)
# print(L)
    
    
# l=[]
# for i in range(20):
#     l.append(0)
# print(l)


#count
# h=[1,2,2,5]
# #print(h.count(2))
# print(h.pop(2))
# print(h)

# l=[4,6,9]
# # l.extend([4])
# # print(l)
# d=[7,44,66]
# #l.extend(d)
# print(l)
# c=l+d
# c.remove(44)
# print(c)


# e=[5,"rama"]
# l=e.copy()
# print("it is copied into l",l)
# print(e)


# a=[55,88,99,3]
# print(a.index(99)) # we have give value so it tells index


# a=[4,88,6,99,3]
# a.sort()
# print(a)
#a=[44,88,99,55,55]
# #a.remove(55)
# print(a)


# a.pop(2)
# print(a)


# a.sort(reverse=True)
# print(a)


# s=[33,88,99]
# h=s*3
# print(h)



# l=eval(input("enter list values"))
# c=input("enter check value ")

# while True:
#     if c in l:
#         print("value is present in the list ")
#         break
#     else:
#         print("value is not present in the list ")
#         c=input("enter again check value")


'''Reverse the Number.'''

# lst=[4,1,3,5,6,2,88,12,6,3,]
# n=len(lst)-1
# while n>=0:
#     print(lst[n],end=" ")
#     n-=1


# lst=[4,1,3,5,6,2,88,12,6,3,]
# lst.sort(reverse=True)
# for i in lst:
#     print(i,end=" ")
    
# lst=[50,30,10,40,20]
# lst.sort()
# lst.reverse()
# print(lst)


# lst=[5,4,3,2,1]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
#             print(lst)
#     print(lst)
# print("\n Final List is : ")
# print(lst)


# lst=[20,15,6,3,11,2,13]
# min=lst[0]
# for i in lst:
#     if i<min:
#         min=i
#         print(min,end=" ")
#     print(min,end=" ")
# print("min is: ", min)


# lst=[10,20,30,40,50,30,20,30,40,30,10,20,30,40]
# i=0
# count=0
# search=int(input(f"Enter the value you want to see : "))


# while i<len(lst):
#     if search==lst[i]:
#         count+=1
#         print(f"the value of {search} is present in the list and index is {i}/{i-len(lst)}")
#     i+=1
# print(f"{search} is present {count} times.")


# l1={"hi ","hello "}
# l2={"ram", "banti", "seetha"}
# new_name=[ ]
# for i in l1:
#     for j in l2:
#         new_name.append(i + j)
# print(new_name)

# m=[4,9,55,66,77,88]
# for i in enumerate(m):
#     print(i)




# l=[[3,9,7],[55,77,44]]
# print(l[1][1])


# l=[5,9,77,55,99]
# a=[]
# for i in l:
#     a=i
#     print(i,end=" ")

# l=[]
# for i in range(11):
#     l.append(i)
# print(l)

# l=[i for i in range(11)]
# print(l)

# l=[i*2 for i in range(11)]
# print(l)

# l=[i*i for i in range(11)]
# print(l)

# l=[i for i in range(0,21) if i%2==0]
# print(l)

# name = ["ram", "banti", "chanti"]
# l=[i for i in name]
# print(l)

# name = ["ram", "banti", "chanti"]
# l=[i[0:2] for i in name]
# print(l)

# l=["ram", "banti", "chanti"]
# nl=[]
# for i in l:
#     nl.append(i[0]+i[-1])
# print(nl)

# l=[[10,20,30,],[40,50,60],[70,80,90]]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# for i in l:
#     print(i)
    
# names=["rama", "banti", "roji"]
# l=[i for i in names if 'a' in i]
# print(l)

# names=["rama", "banti", "roji"]
# l=[i if i!="banti" else "hello" for i in names]
# print(l)

# t=(10,20,30)
# l=[i for i in t]
# print(l)

# m=[[j for j in range(3)] for i in range(3)]
# print(m)