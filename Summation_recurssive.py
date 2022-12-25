#WAP to print sum of 1st natural numbers using recurssive functions

def summation(n):
    if(n==0):
        return 0
    else:
        return n + summation(n-1)


n=int(input("Enter number ="))
print("The sum of numbers is",summation(n))
