



'''  Leap Year  '''

l=int(input("Enter Year : "))
if (l%400==0) and (l%100==0)  :
    print(f"This Is Leap Year {l}")
elif (l%4==0) and (l%100!=0):
    print(f"This Is Leap Year {l}")
else:
    print(f"This is Not A Leap Year {l}")
    
    