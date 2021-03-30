a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=0
z=0
def add_cal(a,b):

    if a>0 and b>0:
        c=a+b

    return c

def multiply(a,b):
    c=a*b
    return c

def divide(a,b):
    ##c=a/b
    return a/b

def substract(a,b):
    c=abs(a-b)

z=add_cal(a,b)
print(z)