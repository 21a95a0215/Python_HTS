x=int(input("Enter x value:"))
lst=[]
nlst=[]
for n in range(x):  
    if (n==2 or n==3) or (n%2!=0 and n%3!=0):
        lst.append(n)
    else:
        nlst.append(n)       
print("Prime Numbers are : ", lst)
print("Non-Prime Numbers are : ",nlst)     


