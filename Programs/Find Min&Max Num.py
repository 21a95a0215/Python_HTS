
arr=eval(input("Enter Arr : "))

def setmin():
    min=sorted(arr)
    print(min[0])
    
def setmax():
    max=sorted(arr)
    print(max[-1])
    
def min_max():
    setmin()
    setmax()
min_max()
    