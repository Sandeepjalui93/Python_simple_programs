class Factorial:
 def fact(self,n):
     self.f=1
     for i in range(1,n+1):
         self.f*=i
     return self.f

a=int(input("Enter number"))
f1=Factorial()
print("factorial of",a,"is",f1.fact(a))
