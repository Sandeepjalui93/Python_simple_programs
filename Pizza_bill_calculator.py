#Project 1

class Menu:
    
    def ShowMenuVeg(self):
        print("1) Double Cheese Margherita-----300\n2) Awesome Threesome-----350\n3) Spicy Paneer-----400\n4) Magic Mushroom-----450")
    
    def ShowMenuBase(self):
        print("1)Normal------Inclusive\n2)Wheat Crust-----50\n3)Thin Crust-----30\n4)Cheese Burst-----60")
    
    def ShowMenuToppings(self):
        print("1)Onion----20\n2)Corn----30\n3)Capsicum----40\n4)Cheese-----50\n5)Mushroom-----60\n6)Exit")
  
class UserDetails:
    
    def getData(self):
        self.Name=input("Enter  your name:-")
        self.MobileNo=int(input("Enter mobile number:-"))
        self.BillingAddress=input("Enter your Address:-")
        
    def ShowData(self):
        print("The Customer Name is ",self.Name)
        print("Mobile No. is ",self.MobileNo)
        print("The Customer Address is ",self.BillingAddress)
        
class Billing:
    
    def Bill(self):
       LiShowMenuVeg=[300,350,400,450]
       for i in range(0,4):
           if i+1==PizzaChoice:
              PC=LiShowMenuVeg[i]       
       LiShowMenuBase=[0,50,30,60]
       for i in range(0,4):
           if i+1==BreadChoice:
              BC=LiShowMenuBase[i]
       LiShowMenuToppings={1:20,2:30,3:40,4:50,5:60}
       T=0
       for i in ToppingsChoice:
           if i in LiShowMenuToppings.keys():
               T=T + LiShowMenuToppings.get(i)
       price=PC+BC+T
       tax=0.18*price
       net=price+tax
       print("The Pizza Price is ",price)
       print("The Taxable value is ",tax)
       print("The total Value is ",net)
       

class Main(Menu,UserDetails,Billing):
    pass
s1=Main()

print("Welcome TO Joey's Pizza")
print("Please fill the following details to help us understand your requirement")
s1.getData()
print("-------------------------------------------")

print("Here is the list of pizza available with us")
s1.ShowMenuVeg()
PizzaChoice=int(input("Enter your choice between 1 to 4="))

print("-------------------------------------------")

print("Here is the list of Bread Types")
s1.ShowMenuBase()
BreadChoice=int(input("Enter your choice between 1 to 4="))

print("-------------------------------------------")
s1.ShowMenuToppings()
ToppingsChoice=[]
n=int(input("Click 1 to 5 for any toppings or else click 6 for no toppings="))
if n!=6:
    ToppingsChoice.append(n)
while n!=6:
    s1.ShowMenuToppings()
    n=int(input("Enter choice"))
    ToppingsChoice.append(n)

s1.ShowData()
print("-------------------------------------------")
s1.Bill()
print("-------------------------------------------")
print("Thank You")

