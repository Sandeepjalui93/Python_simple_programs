#WAP to find factorial of a number using functions

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter number"))
print("factorial of",n,"is",fact(n))
