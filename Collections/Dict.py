'''Dictionary'''

# d={}
# print(d)

# d={}
# d['name']="Rama"
# print(d)

# d={1:'apple', 2:'ball'}
# print(d)
# print(d[1])

# d={'name':'John', 1:[2,4,3]}
# print(d)
# print(d['name'])
# print(d[1])

# d=dict({1:'apple', 2:'ball'})
# print(d)

# d=dict([(1, 'apple'), (2,'ball')])
# print(d)
# print(d.get('Address'))

# d={1:'Rama', 2:'Krishna'}
# print(2 in d)
# print(3 not in d)

# d={}
# while True:
#     key=input("Enter Key :")
#     value=input("Enter value :")
#     d[key]=value
#     choice=input("Enter choice you want to add more elements in to dictionary [Y/N] :")
#     if choice=='N':
#         break
# print(d)

# d={1:'Rama', 2:'Krishna'}
# for i in d:
#     print(i, d[i])
    
# d={1:'Rama', 2:'Krishna'}
# d[3]='Kutti'
# print(d)

# d[1]='Raju'
# print(d)

# d={1:'Rama', 2:'Krishna'}
# del d[1]
# print(d)
# del d
# print(d)

'''Get Method'''

# d={1:'Rama', 2:'Krishna'}
# print(d.get(1))
# print(d.get(3))
# print(d.get(3, "Unknown"))

'''Items Method'''

# d={1:'Rama', 2:'Krishna'}
# print(d.items())
# for i in d.items():
#     print(i)
# for i, j in d.items():
#     print(i, j)

'''Pop Method''' 

# d={1:'Ram', 2:'Krishna'} 
# d.pop(1)  
# print(d)
# d.pop() #key Error

'''PopItem Method'''


# d={1:'Rama', 2:'Krishna'}
# print(d.popitem())

'''Keys Method'''


# d={1:'Rama', 2:'Krishna'}
# print(d.keys())
# for i in d.keys():
#     print(i)

'''Value Method'''    


# d={1:'Rama', 2:'Krishna'}
# print(d.values())
# for i in d.values():
#     print(i)
    
'''SetDefault Method'''


# d={1:'Rama', 2:'Krishna'}
# print(d.setdefault(111, 'Thaher Alisha'))
# print(d)

# print(d.setdefault(2,'Gopal')) #Key And Value will not be modified.
# print(d)

'''Update Method'''


# d1={1:'Rama', 2:'Krishna'}
# d2={3:'Rama Krishna', 4:'Gopal'}
# d1.update(d2)
# print(d1)

# d1={1:'Rama', 2:'Krishna'}
# d2={2:'Rama Krishna', 4:'Gopal'}
# d1.update(d2)
# print(d1)

'''Copy Method'''

# d1={1:'Rama', 2:'Krishna'}
# d2=d1.copy()
# print(d1)
# print(d2)
# print(id(d1))
# print(id(d2))

# d1={1:'Rama', 2:'Krishna'}
# d2=d1
# print(d1)
# print(d2)
# print(id(d1))
# print(id(d2))

'''Clear ethod'''

# d1={1:'Rama', 2:'Krishna'}
# print(d1)
# d1.clear()
# print(d1)

'''Fromkeys Method'''

# l=[10,20,30]
# d=dict.fromkeys(l)
# print(d)

# t=(10,20,30)
# d=dict.fromkeys(l)
# print(d)

# r=range(5)
# d=dict.fromkeys(r)
# print(d)

# r=range(3)
# d=dict.fromkeys(r,"Hello")
# print(d)

# r=range(3)
# l=["Ram", "Banti", "Chanti"]
# d=dict.fromkeys(r,l)
# print(d)


'''..........................'''






# d={i:i for i in range(0,5)}
# print(d)
# print(type(d))

# d={i:i*i for i in range(0,5)}
# print(d)
# print(type(d))

# l=[10,20,30,40]
# d={i:3*i for i in l}
# print(d)

# name=["Rama", "Krishna", "Gopal"]
# d={i:len(i) for i in name}
# print(d)

'''Nested Dictionary'''

# s={1:{"name":"Rama Krishna","Place":"Kakinada"},2:{"name":"Rajaram","place":"rajahmundry"}}
# for i,j in s.items():
#     print("Student id is : ", i)
#     for k in j:
#         print(f"{k} is: {j[k]}")
#     print('_'*20)



# s="Rama"
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# print(d)
# for i,j in d.items():
#     print(f'{i} is present {j} times')


'''Merging Dict Elements'''

# d1={"name":"Rama"}
# d2={"place":"kakinada"}

# d3={**d1, **d2}
# print(d3)


'''Problems on Dict'''

'''Length of a Dict'''

# d={"a":1, "b":2, "c":3}
# L=sum(1 for i in d)  #sum(a,b)
# print(L)

# d={"person1":{"name":"John","age":25, "height":5.5 },
#    "person2" :{"name":"Alice", "age":30 , "height": 5.0},
#    "person3":{"name":"Bob", "age":20,"height":4.5}}
# cnt=0

# for key,val in d.items():
    # if isinstance(val,dict):
    #     for i in val:
    #         cnt+=1
    # else:
    #     cnt+=1
# print(cnt)
#     if True:
#         for i in val:
#             cnt+=1
# print(cnt)         

'''Check if a Key Exists'''

# d={'a':1,'b':2,'c':3}
# key='b'
# print(key in d)
# key='g'
# print(key in d)

# def checkkey(dic,key):
#     if key in dic.keys():
#         print("Present, ",end=" ")
#         print("value =" , dic[key])
#     else:
#         print("Not present")
# dic={'a':100, 'b':200, 'c':300}
# key = 'b'
# checkkey(dic,key)
# key = 'w'
# checkkey(dic,key)

# d={'a':100, 'b':200, 'c':300}
# if d.get('b')==None:
#     print("Not Present")
# else:
#     print("Present")

# dic={'a':100, 'b':200, 'c':300}
# try :
#     dic['d']
#     print('Found')
# except KeyError as error:
#     print("Not Found")

