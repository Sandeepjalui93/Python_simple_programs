#WAP to print and count all prime numbers between 1 to 100
dig = 0
for a in range(2,101):
    n=a
    i=2
    while n%i!=0:
        i=i+1
    if n==i:
        dig += 1
        print(n)


print("Total prime numbers are ",dig)
