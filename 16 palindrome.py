n=int(input("Enter Number="))
copy=n
rev=0
while n!=0:
    ld=n%10
    rev=rev*10+ld
    n=n//10

if rev==copy:
      print(copy,"is palindrome")
else:
      print(copy,"is not palindrome")
      
