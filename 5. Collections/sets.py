'''Sets'''

# s=eval(input())
# print(s)
# print(type(s))

# s={10,20,30,40,50}
# print(s)
# print(type(s))

# s={30,"Ram",65.4,True}
# print(s)
# print(type(s))

# l1=[10,20,30,40,50]
# s1=set(l1)
# print(s1)
# print(type(s1))

# s=set(range(10))
# print(s)
# print(type(s)

# name="Rama Krishna"
# s=set(name)
# print(s)
# print(type(s))

# t=(10,20,30,40,50)
# s=set(t)
# print(s)
# print(type(s))

# s={10,20,30,40,50}
# print(30 in s)
# print(60 not in s)

'''Add & Update'''

# s={1,3}
# print(s)
# s.add(2)
# print(s)
# s.update([2,3,4])
# print(s)
# s.update([4,5],{1,6,8},(9,10))
# s.update([68])
# print(s)

# s={10}
# l=[20,30]
# t=(40,30,50)
# s.update(l,t)
# print(s)
# s.update(l,range(10))
# print(s)

'''Remove method'''

# s={10,20,30,40,50}
# s.remove(30)
# print(s)

# s={10,20,30,40,50}
# s.remove(80)
# print(s)

'''Discard Method'''

# s={10,20,30,40,50}
# s.discard(80)
# print(s)

'''Pop Method'''

# s={10,20,30,40,50}
# s.pop()
# print(s)
# print(s.pop())

'''Copy Method'''

# s1={10,20,30,40,50}
# s2=s1.copy()
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
      
# s1.add((80))
# print(s1)
# print(s2)

# s1={10,20,30,40,50}
# s2=s1
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
# s1.add((80))
# print(s1)
# print(s2)

'''Clear Method'''

# s1={10,20,30,40,50}
# s1.clear()
# print(s1)

'''Enumarate Function'''

# x=('apple', 'banana','cherry')
# y=enumerate(x)
# print(list(y))
# z=set(x)
# print(z)

'''Union Method'''

# s1={10,20,30,40,50}
# s2={10,50,60,20}
# print(s1.union(s2))
# print(s1 | s2)

'''Intersection Method'''

# s1={10,20,30,40,50}
# s2={10,50,60,20}
# print(s1.intersection(s2))
# print(s1&s2)

'''Difference Method'''

# s1={10,20,30,40,50}
# s2={10,50,60,20}
# print(s1.difference(s2))
# print(s1-s2)

'''Symmetric Difference'''

# s1={10,20,30,40,50}
# s2={10,50,60,20}
# print(s1.symmetric_difference(s2))
# print(s1^s2)

'''Subset and Superset'''

# a={1,2,3,4,5,6,7,8}
# b={2,3,4}
# print(b.issubset(a))
# print(a.issuperset(b))

'''Disjiont'''

# a={1,2,3}
# b={4,5}
# print(a.isdisjoint(b))

'''Set Comprehention'''

# s=set()
# for i in range(11):
#     s.add(i)
# print(s)

# s={i for i in range(11)}
# print(s)

# s={i*2 for i in range(11)}
# print(s)

# l=[10,20,30]
# s={i*i for i in l}
# print(s)

# s={i for i in range(20,40) if i%4==0}
# print(s)

# name=["Rama", "Banti", "Chanti"]
# s={i for i in name}
# print(s)

# s={i[0] for i in name}
# print(s)

# s={i.upper() for i in name}
# print(s)

# name=["Raja","Rama","Raghu"]
# s={i if i !="Rama" else "Ram" for i in name}
# print(s)

'''Frozenset'''

# s={10,20,30,40}
# print(s)
# fs=frozenset(s)
# print(fs)
# print(type(fs))

# s={10,20,30,40}
# fs=frozenset(s)
# fs.remove(26)
# print(fs)

# s1={10,20,30,40,50}
# s2={60,"Rama"}
# s3={*s1 , *s2}
# print(s3)