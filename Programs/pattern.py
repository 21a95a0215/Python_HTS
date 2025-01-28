# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#low to high
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#high to low
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        if j == i :
            print(chr(65+j),end="")
        else:
            print(" ",end=" ")
    for j in range(i,n-1):
        if j == n-2:
            print(chr(69),end=" ")
        else:
            print(" ",end=" ")
    print()