#WAP to print factorial of number

x=int(input("Enter number"))
fact=1
for i in range(1,x+1):
    fact = fact * i
print("Factorial of",x,"is ",fact)


