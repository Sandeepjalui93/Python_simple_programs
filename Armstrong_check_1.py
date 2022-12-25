n=int(input("enter number"))
copy=n
dig=0
sum=0
while n!=0:
      dig=dig+1
      n=n//10
n=copy

while n!=0:
      ld=n%10
      sum=sum+ld**dig
      n=n//10

if sum==copy:
      print(copy,"is armstrong")

else :
      print(copy,"is not armstrong")
