#WAP to check entered number prime or not

n=int(input("Enter a number"))
i=2
while n%i!=0:
      i=i+1

if n==i:
      print(n,"is prime")


else :
      print(n,"is not prime")
