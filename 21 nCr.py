#WAP to find nCr

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter n="))
r=int(input("Enter r="))

print("nCr is",fact(n)/(fact(r)*fact(n-r)))
