pn=int(input("Enter Number : "))
lst=[]
lstsum=[]
z=0
for i in range(pn+1):
    for j in range(pn+1):
        if i*j==pn:
            lst.append(i)
            lst.append(j)
            lst=list(set(lst))
            
        j+=1
    i+=1
lst.sort()
for k in lst:
    if k==lst[-1]:
        break
    z=z+k
    lstsum.append(z)
print(lst)
print(z)      