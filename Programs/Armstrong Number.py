n=int(input("Enter Number : "))
s=str(n)
a=0
b=0
for i in s:
    i=int(i)
    a=(i*i*i)
    b=b+a
if b==n:
    print("It is a Strong Number : ", b)
else:
    print("It is Not a Strong Number. The Output is : ",b)
    