def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter Choice(1/2/3/4) : ")
    if choice in ('1','2','3','4'):
        try :
            num1=float(input("Enter First Number : "))
            num2=float(input("Enter Second Number : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",addition(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtraction(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))
        
        next_cal=input("Let's do the next calculation? (yes/no) : ")
        if next_cal == 'no':
            break
        else:
            print("Invalid Input")