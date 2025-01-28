#Conditional Statement
# "if" statement

s=int(input("enter any num"))
if s<10:
    print("it is less then 10") 

a,b,c=map(int,input("Enter values :").split())
if a>b and a>c :
    print("A is Big")
if b>a and b>c :
    print("B is Big")
if c>a and c>b :
    print("C is Big")
    
a=float(input("Enter Value of A :"))
if a%2==0 :
    print("A is Even")
if a%2!=0 :
    print("A is Odd")
    
a=int(input("Enter Value :"))
if a>0:
    print("A is Positive")
if a<0:
    print("A is Negitive")
if a==0:
    print("A is Zero")
    
# "if, else" statement 

ch = input("Enter a Charecter : ")
vow = "a, e, i, o, u, A, E, I, O, U"
if ch in vow :
    print(f"{ch} is Vowel ")
else:
    print(f"{ch} is Not a Vowel ")
    
age = int(input("Enter Your Age :"))
if age>18:
    print("You Can Vote")
else:
    print("You Can Not Vote")

# "if, elif, else" statement
    
x=int(input("Enter Value : "))
if x>20:
    print("X is Higher than 20")
elif x in range(1,20):
    print("X is Lower than 20")
elif x==20 :
    print("X is Equal to 20")
elif x==0:
    print("X is Equal to Zero")
elif x<0:
    print("X is Negative Number")
else:
    print("X is Not a Integer")
    
x,y=map(int,input("Enter Values : ").split())
if x>y:
    print("X is greater than Y")
elif x<y:
    print("X is Less than Y")
else:
    print("X is Same as Y")
    
x,y=map(int,input("Enter Values : ").split())
print("X is Higher than Y") if x>y else print("X is Lower than Or Equal to Y")


'''Looping Statement
"While Loop"'''


i=1
sum=0
while i<10:
    sum=sum+i
    i=i+1
print(sum)

i=1
sum=1
while i<4:
    sum=sum*i
    i=i+1
print(sum)

a=int(input("Enter Value : "))
x=1
while x<11:
    print("%d*%d=%d"%(a,x,a*x))
    x=x+1

a=int(input("Enter Value : "))
x=1
while x<11:
    b=a*x
    print(f"{a}*{x} = {b}")
    x+=1
    
while False:
    print("infinity loop")
else:
    print("it is else") 

  


i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
    
i=int(input("Enter Value : "))
if i>=0:
    while i<6:
        print(i)
        i=i+1
    else:
        print("i is no longer than 6")
else:
    print("i is Negative value")
    
    
name =input("enter list name :")
num=0
while num<len(name):
    if name[num]=='s':
        break
    print(name[num],end="")
    num=num+1
    
s=1
while s==0:
    i=int(input("Enter N Value"))
    print(i)

i=1
while i<=5:
    print("*",end=" ")
    i=i+1


s=int(input("Enter Salary : "))
g=input("Enter your Gender : ")
if g=='m':
    bonus = s*0.05
else:
    bonus = s*0.10
if s<15000:
    bonus = bonus + s*0.03
s= s + bonus
print(s)


'''For Loop'''

for i in range(2,22,2):
    print(i,end=" ")

s=input("Enter Name : ")
for i in s:
    print(i,end="")

lst=eval(input("enter list values: "))
for i in lst:
    print(i)
    print(type(i))
    print(type(lst))

num=eval(input("Enter Value : "))
for i in range(1,11):
    sum=num*i
    #print(f"{num}*{i} = {sum}")
    #print("%d*%d=%d"%(num,i,num*i))
    print(sum)

def pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()
pattern(5)

def pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print(k+1,end="")
        print()
pattern(5)


if __name__=='_main_':
    n=int(input())
    for i in range(1,n+1):
        print(i,end="")



def hide_char():
    name = input()
    char='a'
    #count=0
    hidden_string=""
    for c in name:
        if c==char:
            hidden_string +=""
        else:
            hidden_string +=c
    print(hidden_string)
hide_char()


'''Nested Loopings'''

i=1
while(i<=3):
    print(i)
    j=1
    while(j<=3):
        print(j)
        j+=1
    i+=1


i=1
while(i<=3):
    print("ALisha")
    j=1
    while(j<=3):
        print("T")
        j+=1
    i+=1

# x = eval(input("Enter X : "))
# y = eval(input("Enter Y : "))
x,y=map(eval,input().split())
i = 0
while i < len(x):
    j = 0
    while j < len(y):     
        print(x[i], y[j])       
        j+=1
    i+=1


for i in range(1,11):
    for j in range(2,4):
        print(i*j,end=" ")
    print()

n = int(input("Enter rows : "))
i,j=0,0
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

adj = ["red", "big", "tasty"]
fruit = ["Apple", "Banana", "Cherry"]
for i in adj:
    adj[i]
    print(i)
    
    for j in fruit:
        print(j)
    adj=adj+i


adj = ["red", "big", "tasty"]
fruit = ["Apple", "Banana", "Cherry"]
for j in fruit:
    for i in adj:
      print(i,j)



adj = ["red", "big", "tasty"]
fruit = ["Apple", "Banana", "Cherry"]
i=0
while i < len(adj) or i<len(fruit):
    if adj[i] != fruit[i]:
        print(adj[i],fruit[i])  
    i+=1
        
        
'''break,pass,continue'''

for i in "python":
    if i=="k":
        pass
    print(i)
    