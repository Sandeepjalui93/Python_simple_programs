#WAP to print armstrong numbers from 1 to 100000

    
for i in range(1,100000):
    dig=0
    sum=0
    copy=n=i
    while n!=0:
        dig=dig+1
        n=n//10
    
    n = copy

    while n!=0:
      ld=n%10
      sum=sum+ld**dig
      n=n//10

    if sum==copy:
          print(copy)

