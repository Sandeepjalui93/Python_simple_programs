#WAP to check armstrong number

n=int(input("Enter number"))
sum1=0
copy=n

while n!=0:
    ld=n%10
    sum1=sum1+ld**3
    n=n//10

if sum1==copy:
    print(copy,"is armstrong")
else:
    print(copy,"is not armstrong")
    
