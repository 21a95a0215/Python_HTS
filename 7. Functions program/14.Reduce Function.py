from functools import reduce

x=[10,20,30,40]
def fun(a,b):
    return a+b
d=reduce(fun,x)
print(d)

